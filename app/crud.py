import app.schemas as schemas
import app.models as models


def get_user_by_email(db, email):
    return db.query(models.User).filter(models.User.email == email).first()
    # указываем на то, что ищем среди пользователей,
    # накладываем условие совпадения email
    # возвращаем объект User, если найден, None - если нет


def get_user(db, user_id):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # создаем объект модели Users

    db.add(db_user)  # добавляем объект в сессию
    db.commit()  # сохраняем изменения
    db.refresh(
        db_user
    )  # обновляем объект db_user, чтобы в него подгрузился id, который автоматически сгенерировала база

    return db_user
