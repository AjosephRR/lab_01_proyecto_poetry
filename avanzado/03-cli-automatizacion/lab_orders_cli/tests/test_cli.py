from __future__ import annotations

from pathlib import Path

from lab_orders_cli.main import app
from typer.testing import CliRunner

runner = CliRunner()


class FakeClient:
    def __init__(self, settings) -> None:
        self.settings = settings

    def list_orders(self):
        return [{"id": "ORD-001", "status": "created"}]

    def create_order(self, payload):
        return {"id": "ORD-002", **payload}

    def delete_order(self, order_id):
        return None


def test_list_orders(monkeypatch) -> None:
    monkeypatch.setattr("lab_orders_cli.main.OrdersApiClient", FakeClient)

    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    assert "ORD-001" in result.stdout


def test_create_order(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setattr("lab_orders_cli.main.OrdersApiClient", FakeClient)

    payload_file = tmp_path / "order.json"
    payload_file.write_text(
        '{"customer_email": "demo@example.com", "items": []}',
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        ["create", "--payload-file", str(payload_file)],
    )

    assert result.exit_code == 0
    assert "ORD-002" in result.stdout


def test_delete_order(monkeypatch) -> None:
    monkeypatch.setattr("lab_orders_cli.main.OrdersApiClient", FakeClient)

    result = runner.invoke(app, ["delete", "ORD-001"])

    assert result.exit_code == 0
    assert "ORD-001" in result.stdout


def test_create_order_fails_with_invalid_json(tmp_path: Path) -> None:
    payload_file = tmp_path / "bad.json"
    payload_file.write_text('{"customer_email"', encoding="utf-8")

    result = runner.invoke(
        app,
        ["create", "--payload-file", str(payload_file)],
    )

    assert result.exit_code != 0
    assert "JSON inválido" in result.stdout
