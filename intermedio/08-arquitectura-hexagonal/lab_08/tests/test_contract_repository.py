from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.domain.entities import Order
from app.domain.ports import OrderRepository
from app.infrastructure.persistence.memory_repository import InMemoryOrderRepository
from app.infrastructure.persistence.sqlalchemy_models import Base
from app.infrastructure.persistence.sqlalchemy_repository import (
    SQLAlchemyOrderRepository,
)


def build_order(order_id: str) -> Order:
    return Order(
        order_id=order_id,
        customer_email=f"{order_id}@example.com",
        item="Monitor",
        quantity=1,
        unit_price=Decimal("3200.00"),
    )


@pytest.fixture(params=["memory", "sqlite"])
def repository(request: pytest.FixtureRequest):
    if request.param == "memory":
        yield InMemoryOrderRepository()
        return

    engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
    Base.metadata.create_all(bind=engine)
    session_local = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
    session: Session = session_local()

    repo = SQLAlchemyOrderRepository(session)

    try:
        yield repo
    finally:
        session.close()


def test_repository_contract_save_and_get_by_id(
    repository: OrderRepository,
) -> None:
    order = build_order("ord-contract-1")

    repository.save(order)
    recovered = repository.get_by_id("ord-contract-1")

    assert recovered is not None
    assert recovered.order_id == order.order_id
    assert recovered.customer_email == order.customer_email
    assert recovered.total_amount == order.total_amount


def test_repository_contract_list_all_returns_saved_orders(
    repository: OrderRepository,
) -> None:
    first = build_order("ord-contract-2")
    second = build_order("ord-contract-3")

    repository.save(first)
    repository.save(second)

    all_orders = repository.list_all()
    ids = {order.order_id for order in all_orders}

    assert "ord-contract-2" in ids
    assert "ord-contract-3" in ids
