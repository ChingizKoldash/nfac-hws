from fastapi import FastAPI, HTTPException, Query, Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

cars = [
    {"id": i, "name": f"Car {i}", "year": str(2000 + (i % 23))} for i in range(1, 101)
]

users = [
    {
        "id": i,
        "email": f"user{i}@example.com",
        "first_name": f"First{i}",
        "last_name": f"Last{i}",
        "username": f"user_{i}"
    } for i in range(1, 51)
]

@app.get("/cars", response_class=HTMLResponse)
def get_cars(
    request: Request,
    page: int = Query(1, alias="page"),
    limit: int = Query(10, alias="limit"),
    name: Optional[str] = Query(None, alias="name")
):
    start = (page - 1) * limit
    end = start + limit
    filtered_cars = [car for car in cars if name.lower() in car['name'].lower()] if name else cars
    return templates.TemplateResponse("cars/cars.html", {"request": request, "cars": filtered_cars[start:end],"page": page, "limit": limit})

@app.get("/cars/search", response_class=HTMLResponse)
def search_cars(request: Request, car_name: Optional[str] = Query(None, alias="car_name")):
    filtered_cars = [car for car in cars if car_name.lower() in car['name'].lower()] if car_name else cars
    return templates.TemplateResponse("cars/search.html", {"request": request, "cars": filtered_cars, "car_name": car_name})

@app.get("/cars/new", response_class=HTMLResponse)
def new_car_form(request: Request):
    return templates.TemplateResponse("cars/new.html", {"request": request})

@app.post("/cars/new")
def add_car(name: str = Form(...), year: str = Form(...)):
    new_id = max(car["id"] for car in cars) + 1
    cars.append({"id": new_id, "name": name, "year": year})
    return RedirectResponse(url="/cars", status_code=303)

@app.get("/cars/{car_id}", response_class=HTMLResponse)
def get_car(request: Request, car_id: int):
    car = next((car for car in cars if car["id"] == car_id), None)
    if not car:
        raise HTTPException(status_code=404, detail={"message": "Car not found", "car_id": car_id})
    return templates.TemplateResponse("cars/car.html", {"request": request, "car": car})

@app.get("/users", response_class=HTMLResponse)
def get_users(request: Request, page: int = Query(1, alias="page"), limit: int = Query(10, alias="limit")):
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]
    return templates.TemplateResponse("users.html", {"request": request, "users": paginated_users, "page": page, "limit": limit})

@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail={"message": "User not found", "user_id": user_id})
    return templates.TemplateResponse("user.html", {"request": request, "user": user})
