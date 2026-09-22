from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, SessionLocal, engine, get_db
import app.crud as crud
import app.models as models
import app.schemas as schemas

Base.metadata.create_all(bind=engine)  # создаем колонки в бд

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


@app.post("/users/", response_model=schemas.UserResponse)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if (
        crud.get_user_by_email(db, email=user.email) != None
    ):  # если почта занята выбрасываем ошибку
        raise HTTPException(status_code=400, detail="Email already registered")
    else:  # иначе создаем нового пользователя
        new_user = crud.create_user(db=db, user=user)
        return new_user


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user == None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return db_user