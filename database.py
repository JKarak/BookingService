from sqlalchemy import create_engine # для подключения к бд
from sqlalchemy.orm import declarative_base, sessionmaker
# declarative_base для создания класса моделей
# sessionmaker для настройки сессий

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) # объект для управления соединениями с бд

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# создаем класс для сессий, autocommit=False отключает автокоммит,
# autoflush=False отключает автоматический сброс изменений в БД перед запросами,
# bind=engine связывает эту фабрику сессий с созданным ранее движком

Base = declarative_base()
# Создает базовый класс (Base), от которого будут наследоваться все будущие ORM-модели (классы таблиц)