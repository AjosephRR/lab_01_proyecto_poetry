import pytest


async def create_user_and_token(client) -> str:
    await client.post(
        "/auth/register",
        json={
            "username": "joseph",
            "full_name": "Joseph Rivera",
            "password": "MiClave123",
        },
    )

    login_response = await client.post(
        "/auth/login",
        data={
            "username": "joseph",
            "password": "MiClave123",
        },
    )

    return login_response.json()["access_token"]


@pytest.mark.anyio
async def test_orders_crud_flow(client) -> None:
    token = await create_user_and_token(client)
    headers = {"Authorization": f"Bearer {token}"}

    create_response = await client.post(
        "/orders/",
        json={
            "title": "Compra de audífonos",
            "description": "Pedido interno",
            "total_amount": 2499.99,
            "status": "pending",
        },
        headers=headers,
    )

    assert create_response.status_code == 201
    created_order = create_response.json()
    order_id = created_order["id"]

    list_response = await client.get("/orders/", headers=headers)
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    detail_response = await client.get(f"/orders/{order_id}", headers=headers)
    assert detail_response.status_code == 200
    assert detail_response.json()["title"] == "Compra de audífonos"

    update_response = await client.put(
        f"/orders/{order_id}",
        json={"status": "paid", "total_amount": 2599.99},
        headers=headers,
    )
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "paid"

    delete_response = await client.delete(f"/orders/{order_id}", headers=headers)
    assert delete_response.status_code == 204

    final_list_response = await client.get("/orders/", headers=headers)
    assert final_list_response.status_code == 200
    assert final_list_response.json() == []


@pytest.mark.anyio
async def test_orders_requires_auth(client) -> None:
    response = await client.get("/orders/")
    assert response.status_code == 401


@pytest.mark.anyio
async def test_order_validation(client) -> None:
    token = await create_user_and_token(client)
    headers = {"Authorization": f"Bearer {token}"}

    response = await client.post(
        "/orders/",
        json={
            "title": "OK",
            "description": "Demasiado corto en title",
            "total_amount": -50,
            "status": "unknown",
        },
        headers=headers,
    )

    assert response.status_code == 422
