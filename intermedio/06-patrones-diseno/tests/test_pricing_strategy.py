from decimal import Decimal

import pytest
from lab_patterns.domain.models import Product
from lab_patterns.pricing.service import PricingContext
from lab_patterns.pricing.strategies import (
    FlatDiscountStrategy,
    NoDiscountStrategy,
    PercentageDiscountStrategy,
)


@pytest.fixture
def product() -> Product:
    return Product(
        sku="SKU-001",
        name="Teclado mecánico",
        base_price=Decimal("100.00"),
        currency="MXN",
    )


def test_no_discount_strategy_returns_same_price(product: Product) -> None:
    context = PricingContext(strategy=NoDiscountStrategy())

    assert context.final_price(product) == Decimal("100.00")


def test_percentage_discount_strategy(product: Product) -> None:
    context = PricingContext(strategy=PercentageDiscountStrategy(Decimal("0.10")))

    assert context.final_price(product) == Decimal("90.00")


def test_flat_discount_strategy(product: Product) -> None:
    context = PricingContext(strategy=FlatDiscountStrategy(Decimal("25.00")))

    assert context.final_price(product) == Decimal("75.00")


def test_flat_discount_never_goes_negative(product: Product) -> None:
    context = PricingContext(strategy=FlatDiscountStrategy(Decimal("150.00")))

    assert context.final_price(product) == Decimal("0.00")


def test_invalid_percentage_discount_raises_error() -> None:
    with pytest.raises(ValueError, match="entre 0 y 1"):
        PercentageDiscountStrategy(Decimal("1.50"))


def test_invalid_flat_discount_raises_error() -> None:
    with pytest.raises(ValueError, match="no puede ser negativo"):
        FlatDiscountStrategy(Decimal("-1.00"))
