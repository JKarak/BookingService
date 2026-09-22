from pydantic import BaseModel


class UserCreate(BaseModel):  # то что отправляет клиент при регистрации
    email: str
    password: str


class UserResponse(BaseModel):  # то что отправляем ему
    id: int
    email: str

    class Config:
        from_attributes = (
            True  # чтобы Pydantic умел читать данные прямо из SQLAlchemy-моделей
        )
