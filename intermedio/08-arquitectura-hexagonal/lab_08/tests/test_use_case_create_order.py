from decimal import Decimal

from app.application.dto import CreateOrderInputDTO
from app.application.use_cases import CreateOrderUseCase
from app.infrastructure.notifications.http_notification import (
    HttpNotificationAdapter,
    SimulatedHttpClient,
)
from app.infrastructure.persistence.memory_repository import InMemoryOrderRepository


def test_create_order_use_case_saves_and_notifies() -> None:
    repository = InMemoryOrderRepository()
    http_client = SimulatedHttpClient()
    notifier = HttpNotificationAdapter(
        endpoint_url="https://notifications.local/orders",
        http_client=http_client,
    )

    use_case = CreateOrderUseCase(
        repository=repository,
        notifier=notifier,
    )

    result = use_case.execute(
        CreateOrderInputDTO(
            customer_email="cliente@example.com",
            item="Teclado",
            quantity=2,
            unit_price=Decimal("850.00"),
        )
    )

    saved_order = repository.get_by_id(result.order_id)

    assert saved_order is not None
    assert saved_order.item == "Teclado"
    assert result.total_amount == Decimal("1700.00")
    assert len(http_client.requests) == 1
    assert http_client.requests[0]["json"]["order_id"] == result.order_id
