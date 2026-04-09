from orders_clean_architecture.domain.entities import Order
from orders_clean_architecture.domain.repositories import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self, storage: dict[str, Order] | None = None) -> None:
        self.storage = storage if storage is not None else {}
        self.seen: list[Order] = []

    def _remember(self, order: Order) -> None:
        already_seen = any(existing.id == order.id for existing in self.seen)
        if not already_seen:
            self.seen.append(order)

    def add(self, order: Order) -> None:
        self.storage[order.id] = order
        self._remember(order)

    def get_by_id(self, order_id: str) -> Order | None:
        order = self.storage.get(order_id)
        if order is not None:
            self._remember(order)
        return order

    def list_all(self) -> list[Order]:
        orders = list(self.storage.values())
        for order in orders:
            self._remember(order)
        return orders
