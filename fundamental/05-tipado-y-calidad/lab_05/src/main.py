from dataclasses import dataclass, field
from typing import Literal, Protocol, TypedDict

OrderStatus = Literal["drift", "paid", "cancelled"]


class OrderItemPayload(TypedDict):
    product_name: str
    quantity: int
    unit_price: float


class OrderPayload(TypedDict):
    order_id: str
    customer_name: str
    items: list[OrderItemPayload]
    discount: float | int | None
    status: OrderStatus


class SupportsSummary(Protocol):
    def summary(self) -> str: ...


@dataclass
class OrderItem:
    product_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Order:
    order_id: str
    customer_name: str
    status: OrderStatus
    items: list[OrderItem] = field(default_factory=list)
    discount: float = 0.0

    @property
    def subtotal(self) -> float:
        return sum(item.subtotal for item in self.items)

    @property
    def total(self) -> float:
        total_con_descuento = self.subtotal - self.discount
        return max(total_con_descuento, 0.0)

    def summary(self) -> str:
        return (
            f"Order(id={self.order_id}, customer={self.customer_name}, "
            f"status={self.status}, total={self.total:.2f})"
        )


def normalize_discount(value: float | int | None) -> float:
    """
    Ejemplo de Union usando la sintaxis moderna con |.
    """

    if value is None:
        return 0.0
    return float(value)


def to_entity(payload: OrderPayload) -> Order:
    items = [
        OrderItem(
            product_name=item["product_name"],
            quantity=item["quantity"],
            unit_price=item["unit_price"],
        )
        for item in payload["items"]
    ]

    return Order(
        order_id=payload["order_id"],
        customer_name=payload["customer_name"],
        status=payload["status"],
        items=items,
        discount=normalize_discount(payload["discount"]),
    )


def print_summary(entity: SupportsSummary) -> None:
    """
    Ejemplo de Protocol:
    aceota cualquier objeto que tenga summary().
    """

    print(entity.summary())


def main() -> None:
    print("=== MÓDULO 05 - TIPADO ESTÁTICO OPCIONAL Y CALIDAD ===")

    raw_order: OrderPayload = {
        "order_id": "ORD-2001",
        "customer_name": "Joseph Rivera",
        "items": [
            {"product_name": "Laptop Stand", "quantity": 1, "unit_price": 899.0},
            {"product_name": "UDB Hub", "quantity": 2, "unit_price": 350.0},
        ],
        "discount": 99,
        "status": "paid",
    }

    order = to_entity(raw_order)

    print("\nResumen de la orden:")
    print_summary(order)

    print("\nDatos derivados:")
    print(f"Subtotal: {order.subtotal:.2f}")
    print(f"Descuento: {order.discount:.2f}")
    print(f"Total: {order.total:.2f}")


if __name__ == "__main__":
    main()
