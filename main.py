from fastapi import FastAPI
from database import Base, engine

Base.metadata.create_all(bind=engine) # создаем колонки в бд

app = FastAPI()

users_db = {}
bookings_db = []

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Server is up and running"}

@app.post("/register")
def register_user(email: str, password: str):
    users_db[email] = password
    return {"user": email}

@app.post("/login")
def login_user(email: str, password: str):
    if email not in users_db:
        return {"error": "User not found"}

    if users_db[email] != password:
        return {"error": "Invalid password"}

@app.post("/bookings")
def post_bookings(email: str, title: str):
    if email not in users_db:
        return {"error": "User not logged in"}
    else:
        bookings_db.append({"email": email, "title": title})

@app.get("/bookings")
def get_booking(email: str):
    if email not in users_db:
        return {"error": "User not logged in"}
    else:
        return [b for b in bookings_db if b["email"] == email]