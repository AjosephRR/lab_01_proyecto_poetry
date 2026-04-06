from dataclasses import dataclass
from decimal import Decimal

from lab_patterns.domain.models import Product
from lab_patterns.pricing.strategies import PricingStrategy


@dataclass(slots=True)
class PricingContext:
    strategy: PricingStrategy

    def final_price(self, product: Product) -> Decimal:
        return self.strategy.calculate(product)

    def change_strategy(self, strategy: PricingStrategy) -> None:
        self.strategy = strategy
