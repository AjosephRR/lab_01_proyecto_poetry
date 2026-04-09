from fastapi.testclient import TestClient
from orders_clean_architecture.interfaces.http.controllers import (
    AUDIT_LOG,
    ORDER_STORAGE,
    app,
)

client = TestClient(app)


def setup_function() -> None:
    ORDER_STORAGE.clear()
    AUDIT_LOG.entries.clear()


def test_create_order_endpoint_returns_201_and_writes_audit_log() -> None:
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-HTTP-1",
            "customer_email": "http@example.com",
            "items": [
                {"sku": "SKU-1", "quantity": 2, "unit_price": 15.0},
                {"sku": "SKU-2", "quantity": 1, "unit_price": 5.0},
            ],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["order_id"] == "ORD-HTTP-1"
    assert body["total"] == 35.0
    assert AUDIT_LOG.entries == ["ORDER_CREATED::ORD-HTTP-1::http@example.com::35.00"]
