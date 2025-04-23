
from fastapi import FastAPI, templating,Form,Request,Response,Cookie
from fastapi.responses import RedirectResponse
from attrs import define 
from jose import JWTError, jwt
import json 


@define
class Purchase:
    id: int = None
    user_id: int = None
    flower_id: int = None

class PurchasesRepository:
    def __init__(self):
        self.purchases = []
        self._id_counter = 1

    def add_purchase(self, user_id: int, flower_id: int):
        purchase = Purchase(
            id=self._id_counter,
            user_id=int(user_id),
            flower_id=int(flower_id)
        )
        self._id_counter += 1
        self.purchases.append(purchase)

    def get_by_user(self, user_id: int):
        return [p for p in self.purchases if p.user_id == int(user_id)]

@define
class Flower:
    id: int = None
    name: str = "" 
    quantity: int = 0
    price: float = 0.0


class FlowersRepository:
    def __init__(self):
        self.flowers = [
            Flower(id=1, name="Rose", quantity=10, price=2.5),
            Flower(id=2, name="Tulip", quantity=5, price=1.5),
            Flower(id=3, name="Daisy", quantity=20, price=0.5),
            Flower(id=4, name="Lily", quantity=8, price=3.0),
            Flower(id=5, name="Sunflower", quantity=15, price=1.0),
            Flower(id=6, name="Orchid", quantity=12, price=4.0),
        ]
        self._id_counter = 1


    def add_flower(self, name: str, quantity: int, price: float):
        self._id_counter += 1  
        flower = Flower(
            id=self._id_counter,
            name=name,
            quantity=quantity,
            price=price
        )
        self.flowers.append(flower)
        return flower


    def get_all(self):
        return self.flowers

    def get_by_id(self, flower_id: int):
        for flower in self.flowers:
            if flower.id == flower_id:
                return flower
        return None


@define
class User:
    id: int = None
    login: str = ""
    password: str = ""

class UsersRepository:
    def __init__(self):
        self.users = [
            User(id=1, login="admin", password="admin"),
            User(id=2, login="user", password="user"),
        ]
    
    def save(self, user: User):
        user.id = len(self.users)+1
        self.users.append(user)

    def get_by_login(self,login ) -> User:
        for user in self.users:
            if login ==user.login:
                return user 
        return None

    def get_by_id(self, id: int) -> User:
        for user in self.users:
            if id ==user.id:
                return user 
        return None
    

app = FastAPI()
templates = templating.Jinja2Templates("templates")
repo = UsersRepository()
flowers_repo = FlowersRepository()
purchases_repo = PurchasesRepository()

@app.get("/registration")
def get_registration(request: Request):
    return templates.TemplateResponse("registration.html",{"request": request})

@app.post("/registration")
def post_registration(
    request: Request,
    login: str = Form(),
    password: str = Form(), 
):  
    user = User(login=login, password=password)
    repo.save(user)
    return RedirectResponse("/registration",status_code = 303)


def create_jwt(user: User):
    payload = {
        "user_id": user.id,
        "login": user.login,
    }
    token = jwt.encode(payload,"secret", algorithm="HS256")
    return token

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token,"secret", algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except jwt.JWTError:
        return None

@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html",{"request": request})

@app.post("/login")
def post_login(
    request: Request,
    login: str = Form(),
    password: str = Form(), 
):  
    user = repo.get_by_login(login)
    if user.password == password:
        response = Response("Logged in!")
        token = create_jwt(user)
        response.set_cookie("token", token)
        
        return response

    return Response("Invalid credentials", status_code=401)


@app.get("/profile")
def get_profile(
    request: Request,
    token: str = Cookie(),
):
    user_id = decode_jwt(token)
    user = repo.get_by_id(int(user_id))
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "user": user,
        }
    )

@app.get("/flowers")
def get_flowers(request: Request):
    flowers = flowers_repo.get_all()
    return templates.TemplateResponse(
        "flowers.html",
        {
            "request": request,
            "flowers": flowers,
        }
    )

@app.post(path="/flowers")
def post_flowers(
    request: Request,
    name: str = Form(),
    quantity: int = Form(),
    price: float = Form(),
):
    flower = flowers_repo.add_flower(name, quantity, price)
    return RedirectResponse("/flowers", status_code=303)


@app.post("/cart/items")
def add_to_cart(
    request: Request,
    flower_id: int = Form(),
):
    cart_cookie = request.cookies.get("cart", "[]")
    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        cart = []

    flower_id = int(flower_id)
    if flower_id not in cart:
        cart.append(flower_id)

    response = RedirectResponse("/flowers", status_code=302)
    response.set_cookie("cart", json.dumps(cart))
    return response


@app.get("/cart/items")
def get_cart(request: Request):
    cart_cookie = request.cookies.get("cart", "[]")
    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        cart = []

    cart = [int(f) for f in cart]  # гарантируем int

    flowers = flowers_repo.get_all()
    cart_items = [flower for flower in flowers if flower.id in cart]
    total = sum(flower.price for flower in cart_items)

    return templates.TemplateResponse(
        "cart.html",
        {
            "request": request,
            "cart_items": cart_items,
            "total": total
        }
    )


@app.post("/cart/checkout")
def checkout(request: Request):
    cart_cookie = request.cookies.get("cart", "[]")
    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        cart = []

    user_id = decode_jwt(request.cookies.get("token"))
    if user_id is None:
        return Response("Not logged in", status_code=401)

    for flower_id in cart:
        purchases_repo.add_purchase(user_id, flower_id)

    response = RedirectResponse("/flowers", status_code=302)
    response.set_cookie("cart", "[]")
    return response


@app.get("/purchases")
def get_purchases(request: Request):
    user_id = decode_jwt(request.cookies.get("token"))
    if user_id is None:
        return Response("Not logged in", status_code=401)

    purchases = purchases_repo.get_by_user(int(user_id))
    flower_ids = [p.flower_id for p in purchases]
    all_flowers = flowers_repo.get_all()
    purchased_flowers = [flower for flower in all_flowers if flower.id in flower_ids]

    return templates.TemplateResponse(
        "purchases.html",
        {
            "request": request,
            "purchased_flowers": purchased_flowers,
        }
    )
