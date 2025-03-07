from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, nfactorial!"}

@app.post("/meaning-of-life")
def meaning_of_life():
    return {"meaning": "42"}

@app.get("/{num}")
def factorial(num: int):
    return {"nfactorial": math.factorial(num)}
