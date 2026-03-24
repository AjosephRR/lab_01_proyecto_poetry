from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

LAB_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{LAB_DIR / 'app.db'}"


class Base(DeclarativeBase):
    pass


engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
