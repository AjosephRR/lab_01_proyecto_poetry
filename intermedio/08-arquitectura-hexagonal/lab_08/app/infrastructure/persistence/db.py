from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.infrastructure.persistence.sqlalchemy_models import Base

LAB_ROOT = Path(__file__).resolve().parents[3]
ARTIFACTS_DIR = LAB_ROOT / "artifacts"
DEFAULT_DB_URL = f"sqlite:///{ARTIFACTS_DIR / 'orders.db'}"

ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

engine = create_engine(DEFAULT_DB_URL, future=True)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
