from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

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

@app.get("/cars")
def get_cars(page: int = Query(1, alias="page"), limit: int = Query(10, alias="limit")):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]

@app.get("/cars/{car_id}")
def get_car(car_id: int):
    car = next((car for car in cars if car["id"] == car_id), None)
    if not car:
        raise HTTPException(status_code=404, detail="Not found")
    return car

@app.get("/users", response_class=HTMLResponse)
def get_users(page: int = Query(1, alias="page"), limit: int = Query(10, alias="limit")):
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]
    
    html_content = """
    <html>
    <head><title>Users</title></head>
    <body>
    <table border="1">
    <tr><th>Username</th><th>Full Name</th></tr>
    """
    for user in paginated_users:
        html_content += f"""
        <tr>
            <td>{user['username']}</td>
            <td><a href='/users/{user['id']}'>{user['first_name']} {user['last_name']}</a></td>
        </tr>
        """
    html_content += "</table></body></html>"
    return HTMLResponse(content=html_content)

@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return HTMLResponse(content=f"""
    <html>
    <head><title>User {user['id']}</title></head>
    <body>
    <h1>{user['first_name']} {user['last_name']}</h1>
    <p><b>Email:</b> {user['email']}</p>
    <p><b>Username:</b> {user['username']}</p>
    </body>
    </html>
    """)