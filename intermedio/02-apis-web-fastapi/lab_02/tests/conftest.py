import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db import Base, get_db
from app.main import app


@pytest.fixture
def test_db_session() -> Generator[Session, None, None]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        db_path = Path(tmp_dir) / "test.db"
        test_database_url = f"sqlite:///{db_path}"

        engine = create_engine(
            test_database_url,
            connect_args={"check_same_thread": False},
        )
        TestingSessionLocal = sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False,
        )

        Base.metadata.create_all(bind=engine)

        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()
            Base.metadata.drop_all(bind=engine)
            engine.dispose()


@pytest.fixture
async def client(test_db_session: Session) -> Generator[AsyncClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        yield test_db_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as async_client:
        yield async_client

    app.dependency_overrides.clear()
