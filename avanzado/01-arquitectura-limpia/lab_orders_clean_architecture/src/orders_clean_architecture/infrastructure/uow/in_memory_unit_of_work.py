from orders_clean_architecture.domain.entities import Order
from orders_clean_architecture.domain.unit_of_work import AbstractUnitOfWork

from ..repositories.in_memory_order_repository import InMemoryOrderRepository


class InMemoryUnitOfWork(AbstractUnitOfWork):
    def __init__(self, storage: dict[str, Order] | None = None) -> None:
        self.storage = storage if storage is not None else {}
        self.orders = InMemoryOrderRepository(self.storage)
        self.committed = False
        self.rolled_back = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        self.rolled_back = True
