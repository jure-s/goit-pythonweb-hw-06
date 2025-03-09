from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
import os

# Налаштування підключення до PostgreSQL
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:dthnbrfkm@localhost:5432/postgres")
engine = create_engine(DB_URL)

# Створення таблиць
Base.metadata.create_all(engine)

# Сесія для роботи з БД
SessionLocal = sessionmaker(bind=engine)
