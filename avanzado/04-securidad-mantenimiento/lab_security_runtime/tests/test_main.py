from fastapi.testclient import TestClient

from secure_app.main import app, get_settings
from secure_app.settings import Settings


def build_test_settings() -> Settings:
    return Settings(
        app_name="secure-runtime-app",
        environment="test",
        debug=False,
        host="0.0.0.0",
        port=8000,
        log_level="INFO",
        api_key="test-secret",
        database_url="sqlite:///./test.db",
        allowed_origins=["http://localhost:3000"],
        _env_file=None,
        _secrets_dir=None,
    )


def test_health() -> None:
    app.dependency_overrides[get_settings] = build_test_settings
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["environment"] == "test"

    app.dependency_overrides.clear()


def test_config_check_does_not_expose_secret_values() -> None:
    app.dependency_overrides[get_settings] = build_test_settings
    client = TestClient(app)

    response = client.get("/config-check")
    payload = response.json()

    assert response.status_code == 200
    assert payload["api_key_configured"] is True
    assert payload["database_url_configured"] is True
    assert "test-secret" not in str(payload)
    assert "sqlite:///./test.db" not in str(payload)

    app.dependency_overrides.clear()
