from fastapi.testclient import TestClient

from app.infrastructure.notifications.http_notification import (
    HttpNotificationAdapter,
    SimulatedHttpClient,
)
from app.infrastructure.persistence.memory_repository import InMemoryOrderRepository
from app.main import app, get_order_notifier, get_order_repository


def test_create_order_endpoint_end_to_end() -> None:
    repository = InMemoryOrderRepository()
    http_client = SimulatedHttpClient()
    notifier = HttpNotificationAdapter(
        endpoint_url="https://notifications.local/orders",
        http_client=http_client,
    )

    app.dependency_overrides[get_order_repository] = lambda: repository
    app.dependency_overrides[get_order_notifier] = lambda: notifier

    try:
        with TestClient(app) as client:
            response = client.post(
                "/orders",
                json={
                    "customer_email": "cliente@example.com",
                    "item": "Tablet",
                    "quantity": 3,
                    "unit_price": "1200.00",
                },
            )

        assert response.status_code == 201

        data = response.json()

        assert data["customer_email"] == "cliente@example.com"
        assert data["item"] == "Tablet"
        assert data["quantity"] == 3
        assert data["total_amount"] == "3600.00"
        assert repository.get_by_id(data["order_id"]) is not None
        assert len(http_client.requests) == 1
    finally:
        app.dependency_overrides.clear()
