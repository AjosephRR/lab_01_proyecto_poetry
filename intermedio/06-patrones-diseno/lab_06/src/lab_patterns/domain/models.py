from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class Product:
    sku: str
    name: str
    base_price: Decimal
    currency: str = "MXN"
