from dataclasses import dataclass


@dataclass(slots=True)
class CreateOrderItemInput:
    sku: str
    quantity: int
    unit_price: float


@dataclass(slots=True)
class CreateOrderInput:
    order_id: str
    customer_email: str
    items: list[CreateOrderItemInput]


@dataclass(slots=True)
class CreateOrderOutput:
    order_id: str
    customer_email: str
    total: float
    status: str
    message: str
