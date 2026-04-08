from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class CreateOrderInputDTO:
    customer_email: str
    item: str
    quantity: int
    unit_price: Decimal


@dataclass(slots=True, frozen=True)
class OrderOutputDTO:
    order_id: str
    customer_email: str
    item: str
    quantity: int
    unit_price: Decimal
    total_amount: Decimal
