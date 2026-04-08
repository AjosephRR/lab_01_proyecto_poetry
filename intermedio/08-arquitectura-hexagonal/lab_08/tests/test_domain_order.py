from decimal import Decimal

import pytest

from app.domain.entities import Order


def test_order_calculates_total_amount() -> None:
    order = Order(
        order_id="ord-1",
        customer_email="cliente@example.com",
        item="Laptop",
        quantity=2,
        unit_price=Decimal("1500.00"),
    )

    assert order.total_amount == Decimal("3000.00")


def test_order_raises_error_when_quantity_is_invalid() -> None:
    with pytest.raises(ValueError, match="quantity"):
        Order(
            order_id="ord-2",
            customer_email="cliente@example.com",
            item="Mouse",
            quantity=0,
            unit_price=Decimal("500.00"),
        )
