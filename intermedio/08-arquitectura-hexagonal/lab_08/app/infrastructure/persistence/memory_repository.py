from dataclasses import dataclass, field

from app.domain.entities import Order


@dataclass
class InMemoryOrderRepository:
    _orders: dict[str, Order] = field(default_factory=dict)

    def save(self, order: Order) -> Order:
        self._orders[order.order_id] = order
        return order

    def get_by_id(self, order_id: str) -> Order | None:
        return self._orders.get(order_id)

    def list_all(self) -> list[Order]:
        return list(self._orders.values())
