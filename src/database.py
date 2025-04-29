from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import config

engine = create_engine(str(config.DB_URL))
SessionFactory = sessionmaker(engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
