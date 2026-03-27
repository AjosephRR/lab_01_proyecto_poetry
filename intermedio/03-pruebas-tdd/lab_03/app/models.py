from dataclasses import dataclass
from decimal import Decimal
from typing import Literal

OrderStatus = Literal["draft", "confirmed", "paid"]


@dataclass(frozen=True)
class OrderItem:
    product_name: str
    quantity: int
    unit_price: Decimal


@dataclass
class Order:
    id: int
    customer_email: str
    items: list[OrderItem]
    discount_percent: int = 0
    status: OrderStatus = "draft"
