from dataclasses import dataclass, field
from typing import Any, Protocol

from app.domain.entities import Order


class HttpClient(Protocol):
    def post(self, url: str, json: dict[str, Any], timeout: float = 5.0) -> None: ...


@dataclass
class SimulatedHttpClient:
    requests: list[dict[str, Any]] = field(default_factory=list)

    def post(self, url: str, json: dict[str, Any], timeout: float = 5.0) -> None:
        self.requests.append(
            {
                "url": url,
                "json": json,
                "timeout": timeout,
            }
        )


@dataclass(slots=True)
class HttpNotificationAdapter:
    endpoint_url: str
    http_client: HttpClient

    def notify_order_created(self, order: Order) -> None:
        payload = {
            "order_id": order.order_id,
            "customer_email": order.customer_email,
            "item": order.item,
            "quantity": order.quantity,
            "unit_price": str(order.unit_price),
            "total_amount": str(order.total_amount),
        }

        self.http_client.post(
            self.endpoint_url,
            json=payload,
            timeout=5.0,
        )
