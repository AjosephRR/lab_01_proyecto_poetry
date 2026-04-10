from fastapi.testclient import TestClient

from orders_packaged_api.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_order_returns_201_and_total() -> None:
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-200",
            "customer_email": "packaging@example.com",
            "items": [
                {"sku": "SKU-1", "quantity": 2, "unit_price": 10.0},
                {"sku": "SKU-2", "quantity": 1, "unit_price": 15.0},
            ],
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "order_id": "ORD-200",
        "customer_email": "packaging@example.com",
        "items_count": 2,
        "total": 35.0,
        "status": "CREATED",
    }
