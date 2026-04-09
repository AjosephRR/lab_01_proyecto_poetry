from collections.abc import Callable, Iterable
from typing import TypeVar, cast

T = TypeVar("T")


class EventDispatcher:
    def __init__(self) -> None:
        self._handlers: dict[type[object], list[Callable[[object], None]]] = {}

    def register(self, event_type: type[T], handler: Callable[[T], None]) -> None:
        handlers = self._handlers.setdefault(event_type, [])
        handlers.append(cast(Callable[[object], None], handler))

    def publish(self, events: Iterable[object]) -> None:
        for event in events:
            for handler in self._handlers.get(type(event), []):
                handler(event)
