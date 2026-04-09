from dataclasses import dataclass, field

from orders_clean_architecture.domain.events import OrderCreated


@dataclass(slots=True)
class InMemoryAuditLog:
    entries: list[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.entries.append(message)


class OrderCreatedAuditHandler:
    def __init__(self, audit_log: InMemoryAuditLog) -> None:
        self.audit_log = audit_log

    def __call__(self, event: OrderCreated) -> None:
        self.audit_log.add(
            f"ORDER_CREATED::{event.order_id}::{event.customer_email}::{event.total:.2f}"
        )
