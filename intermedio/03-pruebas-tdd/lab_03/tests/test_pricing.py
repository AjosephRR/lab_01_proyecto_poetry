from decimal import Decimal

import pytest

from app.models import OrderItem
from app.pricing import (
    apply_discount,
    calculate_subtotal,
    calculate_total,
    validate_item,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    "subtotal,discount_percent,expected",
    [
        (Decimal("100.00"), 0, Decimal("100.00")),
        (Decimal("100.00"), 10, Decimal("90.00")),
        (Decimal("250.00"), 20, Decimal("200.00")),
        (Decimal("50.00"), 100, Decimal("0.00")),
    ],
)
def test_apply_discount(
    subtotal: Decimal, discount_percent: int, expected: Decimal
) -> None:
    assert apply_discount(subtotal, discount_percent) == expected


@pytest.mark.unit
def test_apply_discount_rejects_invalid_percent() -> None:
    with pytest.raises(ValueError, match="descuento"):
        apply_discount(Decimal("100.00"), 120)


@pytest.mark.unit
def test_validate_item_rejects_empty_name() -> None:
    item = OrderItem(
        product_name="",
        quantity=1,
        unit_price=Decimal("100.00"),
    )

    with pytest.raises(ValueError, match="producto"):
        validate_item(item)


@pytest.mark.unit
def test_validate_item_rejects_zero_quantity() -> None:
    item = OrderItem(
        product_name="Producto X",
        quantity=0,
        unit_price=Decimal("100.00"),
    )

    with pytest.raises(ValueError, match="cantidad"):
        validate_item(item)


@pytest.mark.unit
def test_validate_item_rejects_invalid_price() -> None:
    item = OrderItem(
        product_name="Producto X",
        quantity=1,
        unit_price=Decimal("0"),
    )

    with pytest.raises(ValueError, match="precio"):
        validate_item(item)


@pytest.mark.unit
def test_calculate_subtotal(sample_items: list[OrderItem]) -> None:
    result = calculate_subtotal(sample_items)
    assert result == Decimal("1900.00")


@pytest.mark.unit
def test_calculate_total_with_discount(sample_items: list[OrderItem]) -> None:
    result = calculate_total(sample_items, discount_percent=10)
    assert result == Decimal("1710.00")


@pytest.mark.unit
def test_calculate_subtotal_without_items() -> None:
    with pytest.raises(ValueError, match="al menos un item"):
        calculate_subtotal([])
