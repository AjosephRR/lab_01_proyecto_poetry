import sys
from decimal import Decimal
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.models import Order, OrderItem  # noqa: E402


@pytest.fixture
def sample_items() -> list[OrderItem]:
    return [
        OrderItem(
            product_name="Teclado mecánico",
            quantity=1,
            unit_price=Decimal("1200.00"),
        ),
        OrderItem(
            product_name="Mouse",
            quantity=2,
            unit_price=Decimal("350.00"),
        ),
    ]


@pytest.fixture
def sample_order(sample_items: list[OrderItem]) -> Order:
    return Order(
        id=1,
        customer_email="joseph@example.com",
        items=sample_items,
        discount_percent=10,
        status="draft",
    )
