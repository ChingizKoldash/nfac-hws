from fastapi import FastAPI, Depends, HTTPException, status, Form, Request, Response, Cookie
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import jwt, JWTError
from typing import List
from uuid import uuid4
import json

SECRET_KEY = "secret"
ALGORITHM = "HS256"

class User(BaseModel):
    id: int
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class Flower(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

class Purchase(BaseModel):
    user_id: int
    flower_id: int

# Репозитории
class UsersRepository:
    def __init__(self):
        self.users: List[User] = []
        self._id_counter = 1

    def save(self, username: str, password: str) -> User:
        user = User(id=self._id_counter, username=username, password=password)
        self._id_counter += 1
        self.users.append(user)
        return user

    def get_by_username(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

class FlowersRepository:
    def __init__(self):
        self.flowers: List[Flower] = []
        self._id_counter = 1

    def add_flower(self, name: str, quantity: int, price: float) -> Flower:
        flower = Flower(id=self._id_counter, name=name, quantity=quantity, price=price)
        self._id_counter += 1
        self.flowers.append(flower)
        return flower

    def get_all(self) -> List[Flower]:
        return self.flowers

    def get_by_id(self, flower_id: int) -> Flower | None:
        for flower in self.flowers:
            if flower.id == flower_id:
                return flower
        return None

class PurchasesRepository:
    def __init__(self):
        self.purchases: List[Purchase] = []

    def add_purchase(self, user_id: int, flower_id: int):
        purchase = Purchase(user_id=user_id, flower_id=flower_id)
        self.purchases.append(purchase)

    def get_by_user(self, user_id: int):
        return [p for p in self.purchases if p.user_id == user_id]

# Инициализация
app = FastAPI()
users_repo = UsersRepository()
flowers_repo = FlowersRepository()
purchases_repo = PurchasesRepository()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("user_id")
    except JWTError:
        return None


@app.post("/signup")
def signup(username: str = Form(), password: str = Form()):
    user_exists = users_repo.get_by_username(username)
    if user_exists:
        raise HTTPException(status_code=400, detail="User already exists")

    user = users_repo.save(username=username, password=password)
    return {"message": "User created", "user_id": user.id}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_repo.get_by_username(form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token({"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

# Получить текущего пользователя
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = users_repo.get_by_id(int(user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@app.get("/profile", response_model=UserOut)
def profile(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/flowers")
def add_flower(name: str = Form(), quantity: int = Form(), price: float = Form()):
    flower = flowers_repo.add_flower(name=name, quantity=quantity, price=price)
    return {"flower_id": flower.id}

@app.get("/flowers", response_model=List[Flower])
def get_flowers():
    return flowers_repo.get_all()

@app.post("/cart/items")
def add_to_cart( request: Request,flower_id: int = Form()):
    cart_cookie = request.cookies.get("cart", "[]")
    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        cart = []

    if flower_id not in cart:
        cart.append(flower_id)

    response = Response("Item added to cart")
    response.set_cookie("cart", json.dumps(cart))
    return response

@app.get("/cart/items")
def get_cart(request: Request):
    cart_cookie = request.cookies.get("cart", "[]")
    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        cart = []

    cart_items = [flowers_repo.get_by_id(flower_id) for flower_id in cart]
    total = sum(flower.price for flower in cart_items if flower)

    return {"cart_items": cart_items, "total": total}

# Оформление покупки
@app.post("/purchased")
def purchased(request: Request):
    cart_cookie = request.cookies.get("cart", "[]")
    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        cart = []

    user_id = decode_access_token(request.cookies.get("token"))
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not logged in")

    for flower_id in cart:
        purchases_repo.add_purchase(user_id, flower_id)

    response = Response("Purchase completed")
    response.set_cookie("cart", "[]")  # Очищаем корзину
    return response

@app.get("/purchased")
def get_purchased(request: Request):
    user_id = decode_access_token(request.cookies.get("token"))
    if user_id is None:
        raise HTTPException(status_code=401, detail="Not logged in")

    purchases = purchases_repo.get_by_user(user_id)
    purchased_flowers = [flowers_repo.get_by_id(p.flower_id) for p in purchases]

    total = sum(flower.price for flower in purchased_flowers if flower)

    return {"purchased_flowers": purchased_flowers, "total": total}
