from fastapi import FastAPI, Depends, HTTPException, status, Form, Request, Response, Cookie
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from jose import JWTError, jwt
from typing import Optional, List
from pydantic import BaseModel
import json
import time

# -------------------- База данных --------------------
DATABASE_URL = "sqlite:///./flowers.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    purchases = relationship("Purchase", back_populates="owner")


class Flower(Base):
    __tablename__ = "flowers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)


class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flower_id = Column(Integer, ForeignKey("flowers.id"))
    owner = relationship("User", back_populates="purchases")
    flower = relationship("Flower")


Base.metadata.create_all(bind=engine)

# -------------------- JWT --------------------
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode["exp"] = time.time() + 3600
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> Optional[int]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("user_id")
    except JWTError:
        return None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# -------------------- FastAPI --------------------
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------- Pydantic --------------------
class FlowerOut(BaseModel):
    id: int
    name: str
    price: float
    class Config:
        orm_mode = True

class ProfileOut(BaseModel):
    id: int
    username: str


# -------------------- Auth --------------------
@app.post("/signup")
def signup(username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    if db.query(User).filter_by(username=username).first():
        raise HTTPException(400, "Username taken")
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    return {"message": "User created"}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(401, "Invalid credentials")
    token = create_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/profile", response_model=ProfileOut)
def get_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(401, "Invalid token")
    return user


# -------------------- Flowers --------------------
@app.get("/flowers", response_model=List[FlowerOut])
def list_flowers(db: Session = Depends(get_db)):
    return db.query(Flower).all()


@app.post("/flowers")
def add_flower(name: str = Form(), quantity: int = Form(), price: float = Form(), db: Session = Depends(get_db)):
    flower = Flower(name=name, quantity=quantity, price=price)
    db.add(flower)
    db.commit()
    return {"flower_id": flower.id}


@app.patch("/flowers/{flower_id}")
def update_flower(flower_id: int, name: str = Form(), quantity: int = Form(), price: float = Form(), db: Session = Depends(get_db)):
    flower = db.query(Flower).get(flower_id)
    if not flower:
        raise HTTPException(404, "Flower not found")
    flower.name = name
    flower.quantity = quantity
    flower.price = price
    db.commit()
    return {"message": "Updated"}


@app.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    flower = db.query(Flower).get(flower_id)
    if not flower:
        raise HTTPException(404, "Flower not found")
    db.delete(flower)
    db.commit()
    return {"message": "Deleted"}


# -------------------- Cart (в cookie) --------------------
@app.post("/cart/items")
def add_to_cart(flower_id: int = Form(), request: Request = None, response: Response = None):
    cart = request.cookies.get("cart")
    items = json.loads(cart) if cart else []
    items.append(flower_id)
    response.set_cookie("cart", json.dumps(items))
    return {"message": "Added to cart"}


@app.get("/cart/items")
def get_cart_items(request: Request, db: Session = Depends(get_db)):
    cart = request.cookies.get("cart")
    flower_ids = json.loads(cart) if cart else []
    flowers = db.query(Flower).filter(Flower.id.in_(flower_ids)).all()
    total = sum(f.price for f in flowers)
    return {"items": flowers, "total": total}


# -------------------- Purchased --------------------
@app.post("/purchased")
def make_purchase(request: Request, response: Response, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)
    if not user_id:
        raise HTTPException(401, "Invalid token")
    cart = request.cookies.get("cart")
    flower_ids = json.loads(cart) if cart else []
    for fid in flower_ids:
        db.add(Purchase(user_id=user_id, flower_id=fid))
    db.commit()
    response.delete_cookie("cart")
    return {"message": "Purchased"}


@app.get("/purchased")
def list_purchases(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)
    if not user_id:
        raise HTTPException(401, "Invalid token")
    purchases = db.query(Purchase).filter_by(user_id=user_id).all()
    return [
        {"name": p.flower.name, "price": p.flower.price}
        for p in purchases
    ]
