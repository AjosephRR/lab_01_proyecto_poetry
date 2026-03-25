import pytest


@pytest.mark.anyio
async def test_register_and_login(client) -> None:
    register_response = await client.post(
        "/auth/register",
        json={
            "username": "joseph",
            "full_name": "Joseph Rivera",
            "password": "MiClave123",
        },
    )

    assert register_response.status_code == 201
    assert register_response.json()["username"] == "joseph"

    login_response = await client.post(
        "/auth/login",
        data={
            "username": "joseph",
            "password": "MiClave123",
        },
    )

    assert login_response.status_code == 200
    body = login_response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"
