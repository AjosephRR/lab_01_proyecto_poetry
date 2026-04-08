from typing import Protocol

from app.domain.entities import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> Order: ...

    def get_by_id(self, order_id: str) -> Order | None: ...

    def list_all(self) -> list[Order]: ...


class OrderNotifier(Protocol):
    def notify_order_created(self, order: Order) -> None: ...
