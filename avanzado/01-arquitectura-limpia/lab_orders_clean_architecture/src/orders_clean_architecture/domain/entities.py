from dataclasses import dataclass, field

from orders_clean_architecture.domain.events import OrderCreated


@dataclass(slots=True)
class OrderItem:
    sku: str
    quantity: int
    unit_price: float

    def __post_init__(self) -> None:
        if not self.sku.strip():
            raise ValueError("sku vacío")
        if self.quantity <= 0:
            raise ValueError("quantity debe ser mayor que 0")
        if self.unit_price <= 0:
            raise ValueError("unit_price debe ser mayor que 0")

    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_price, 2)


@dataclass(slots=True)
class Order:
    id: str
    customer_email: str
    items: list[OrderItem]
    status: str = "PENDING"
    _events: list[object] = field(default_factory=list, init=False, repr=False)

    @classmethod
    def create(
        cls,
        order_id: str,
        customer_email: str,
        items: list[OrderItem],
    ) -> "Order":
        if not order_id.strip():
            raise ValueError("order_id vacío")
        if "@" not in customer_email:
            raise ValueError("customer_email inválido")
        if not items:
            raise ValueError("La orden debe tener al menos un item")

        order = cls(
            id=order_id,
            customer_email=customer_email,
            items=items,
        )

        order._events.append(
            OrderCreated(
                order_id=order.id,
                customer_email=order.customer_email,
                total=order.total,
            )
        )
        return order

    @property
    def total(self) -> float:
        return round(sum(item.subtotal for item in self.items), 2)

    def pull_events(self) -> list[object]:
        events = self._events[:]
        self._events.clear()
        return events
