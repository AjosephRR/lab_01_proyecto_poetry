from dataclasses import dataclass, field
from typing import List

from pydantic import BaseModel, Field, ValidationError


@dataclass
class OrderItem:
    """
    Representa un producto dentro de una orden
    """

    product_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass(order=True)
class Order:
    """
    Entidad principal de una orden.
    Usa dataclass y soporta comparaciones por total.
    """

    sort_index: float = field(init=False, repr=False)
    order_id: str
    customer_name: str
    items: List[OrderItem] = field(default_factory=list)
    discount: float = 0.0

    def __post_init__(self) -> None:
        self.sort_index = self.total

    @property
    def subtotal(self) -> float:
        return sum(item.subtotal for item in self.items)

    @property
    def total(self) -> float:
        total_con_descuento = self.subtotal - self.discount
        return max(total_con_descuento, 0.0)

    @property
    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)
        self.sort_index = self.total

    def __str__(self) -> str:
        return (
            f"Order(order_id={self.order_id}, customer={self.customer_name}, "
            f"total_items={self.total_items}, total={self.total:.2f})"
        )


class OrderItemIn(BaseModel):
    """
    Modelo de entrada para item de orden.
    """

    product_name: str = Field(..., man_length=2)
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)


class OrderIn(BaseModel):
    """
    Modelo de entrada para una orden
    """

    order_id: str = Field(..., min_length=3)
    customer_name: str = Field(..., min_length=2)
    items: List[OrderItemIn] = Field(..., min_length=1)
    discount: float = Field(default=0.0, ge=0)


class OrderOut(BaseModel):
    """
    Modelo de salida serializable
    """

    order_id: str
    customer_name: str
    total_items: int
    subtotal: float
    discount: float
    total: float


def to_entity(order_in: OrderIn) -> Order:
    """
    Convierte un modelo de entrada validado en una entidad Order.
    """
    items = [
        OrderItem(
            product_name=item.product_name,
            quantity=item.quantity,
            unit_price=item.unit_price,
        )
        for item in order_in.items
    ]

    return Order(
        order_id=order_in.order_id,
        customer_name=order_in.customer_name,
        items=items,
        discount=order_in.discount,
    )


def to_output(order: Order) -> OrderOut:
    """
    Convierte una entidad Order en un modelo de salida.
    """
    return OrderOut(
        order_id=order.order_id,
        customer_name=order.customer_name,
        total_items=order.total_items,
        subtotal=order.subtotal,
        discount=order.discount,
        total=order.total,
    )


def main() -> None:
    print("=== MÓDULO 04 - OBJETOS Y MODELOS DE DATOS ===")

    raw_order = {
        "order_id": "ORD-1001",
        "customer_name": "Joseph Rivera",
        "items": [
            {"product_name": "Teclado", "quantity": 2, "unit_price": 750.0},
            {"product_name": "Mouse", "quantity": 1, "unit_price": 320.0},
        ],
        "discount": 100.0,
    }

    try:
        order_in = OrderIn(**raw_order)
        order_entity = to_entity(order_in)

        print("\nEntidad creada correctamente:")
        print(order_entity)
        print("\nDatos derivados de la orden:")
        print(f"Subtotal: {order_entity.subtotal:.2f}")
        print(f"Descuento: {order_entity.discount:.2f}")
        print(f"Total: {order_entity.total:.2f}")
        print(f"Cantidad total de artículos: {order_entity.total_items}")

        order_out = to_output(order_entity)

        print("\nModelo de salida serializado:")
        print(order_out.model_dump())

        otra_order = Order(
            order_id="ORD-1002",
            customer_name="Cliente Demo",
            items=[OrderItem("Monitor", 1, 4200.0)],
            discount=0.0,
        )

        print("\nComparación entre órdenes por total:")
        print(f"{order_entity.order_id} total: {order_entity.total:.2f}")
        print(f"{otra_order.order_id} total: {otra_order.total:.2f}")
        print(f"¿La primera orden es menor que la segunda? {order_entity < otra_order}")

    except ValidationError as error:
        print("\nError de validación en los datos de entrada:")
        print(error)


if __name__ == "__main__":
    main()
