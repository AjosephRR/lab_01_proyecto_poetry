import pytest
from pydantic import ValidationError

from secure_app.settings import Settings


def test_settings_read_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_API_KEY", "super-secret")
    monkeypatch.setenv("APP_DATABASE_URL", "sqlite:///./test.db")
    monkeypatch.setenv(
        "APP_ALLOWED_ORIGINS",
        '["http://localhost:3000", "https://example.com"]',
    )

    settings = Settings(_env_file=None, _secrets_dir=None)

    assert settings.api_key.get_secret_value() == "super-secret"
    assert settings.database_url.get_secret_value() == "sqlite:///./test.db"
    assert settings.allowed_origins == [
        "http://localhost:3000",
        "https://example.com",
    ]


def test_missing_required_secrets_raises_validation_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("APP_API_KEY", raising=False)
    monkeypatch.delenv("APP_DATABASE_URL", raising=False)

    with pytest.raises(ValidationError):
        Settings(_env_file=None, _secrets_dir=None)
