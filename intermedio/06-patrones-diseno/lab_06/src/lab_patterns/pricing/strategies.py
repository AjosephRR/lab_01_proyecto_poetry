from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Protocol

from lab_patterns.domain.models import Product

TWOPLACES = Decimal("0.01")


def money(value: Decimal) -> Decimal:
    return value.quantize(TWOPLACES, rounding=ROUND_HALF_UP)


class PricingStrategy(Protocol):
    def calculate(self, product: Product) -> Decimal: ...


@dataclass(slots=True, frozen=True)
class NoDiscountStrategy:
    def calculate(self, product: Product) -> Decimal:
        return money(product.base_price)


@dataclass(slots=True, frozen=True)
class PercentageDiscountStrategy:
    discount: Decimal

    def __post_init__(self) -> None:
        if self.discount < Decimal("0") or self.discount > Decimal("1"):
            raise ValueError("discount debe estar entre 0 y 1.")

    def calculate(self, product: Product) -> Decimal:
        final_price = product.base_price * (Decimal("1") - self.discount)
        return money(max(final_price, Decimal("0")))


@dataclass(slots=True, frozen=True)
class FlatDiscountStrategy:
    amount: Decimal

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise ValueError("amount no puede ser negativo.")

    def calculate(self, product: Product) -> Decimal:
        final_price = product.base_price - self.amount
        return money(max(final_price, Decimal("0")))
