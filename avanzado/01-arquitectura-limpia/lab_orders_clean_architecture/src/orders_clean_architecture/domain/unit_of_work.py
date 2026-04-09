from abc import ABC, abstractmethod
from collections.abc import Generator

from orders_clean_architecture.domain.repositories import OrderRepository


class AbstractUnitOfWork(ABC):
    orders: OrderRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is not None:
            self.rollback()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError

    def collect_new_events(self) -> Generator[object, None, None]:
        seen = getattr(self.orders, "seen", [])
        for aggregate in seen:
            yield from aggregate.pull_events()
