from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OrderCreated:
    order_id: str
    customer_email: str
    total: float
