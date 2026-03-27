from decimal import Decimal

import pytest
from hypothesis import given
from hypothesis import strategies as st

from app.models import OrderItem
from app.pricing import apply_discount, calculate_total

decimal_strategy = st.decimals(
    min_value=Decimal("0.01"),
    max_value=Decimal("10000.00"),
    places=2,
)
quantity_strategy = st.integers(min_value=1, max_value=100)
discount_strategy = st.integers(min_value=0, max_value=100)


@pytest.mark.property
@given(subtotal=decimal_strategy, discount_percent=discount_strategy)
def test_discount_never_makes_total_greater_than_subtotal(
    subtotal: Decimal, discount_percent: int
) -> None:
    total = apply_discount(subtotal, discount_percent)
    assert total <= subtotal


@pytest.mark.property
@given(unit_price=decimal_strategy, quantity=quantity_strategy)
def test_total_is_positive_when_items_are_valid(
    unit_price: Decimal, quantity: int
) -> None:
    items = [
        OrderItem(
            product_name="Producto prueba",
            quantity=quantity,
            unit_price=unit_price,
        )
    ]

    total = calculate_total(items, discount_percent=0)
    assert total > Decimal("0.00")


@pytest.mark.property
@given(subtotal=decimal_strategy)
def test_zero_discount_keeps_same_total(subtotal: Decimal) -> None:
    total = apply_discount(subtotal, 0)
    assert total == subtotal
