import pytest
from orders_clean_architecture.domain.entities import Order, OrderItem
from orders_clean_architecture.domain.events import OrderCreated


def test_order_create_calculates_total_and_generates_event() -> None:
    items = [
        OrderItem(sku="SKU-1", quantity=2, unit_price=10.0),
        OrderItem(sku="SKU-2", quantity=1, unit_price=5.0),
    ]

    order = Order.create(
        order_id="ORD-001",
        customer_email="test@example.com",
        items=items,
    )

    assert order.total == 25.0
    events = order.pull_events()
    assert len(events) == 1
    assert isinstance(events[0], OrderCreated)
    assert events[0].order_id == "ORD-001"


def test_order_create_raises_error_when_items_are_empty() -> None:
    with pytest.raises(ValueError, match="al menos un item"):
        Order.create(
            order_id="ORD-002",
            customer_email="test@example.com",
            items=[],
        )
