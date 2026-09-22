from app.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # создаем колонку с id
    email = Column(String, unique=True, index=True)  # создаем колонку с почтами
    hashed_password = Column(String)  # создаем колонку с паролем
