from __future__ import annotations

import json
from typing import Any

import typer
from lab_orders_cli.config import Settings


def pretty_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, default=str)


def print_config(settings: Settings) -> None:
    typer.echo(f"Base URL : {settings.base_url}")
    typer.echo(f"Timeout  : {settings.timeout} segundos")


def print_orders(orders: list[dict[str, Any]]) -> None:
    if not orders:
        typer.secho("No hay orders registradas.", fg=typer.colors.YELLOW)
        return

    for index, order in enumerate(orders, start=1):
        order_id = order.get("id") or order.get("order_id") or "(sin id)"
        typer.secho(f"[{index}] Order: {order_id}", fg=typer.colors.GREEN)
        typer.echo(pretty_json(order))
        typer.echo("-" * 50)


def print_created_order(order: dict[str, Any]) -> None:
    typer.secho("Order creada correctamente.", fg=typer.colors.GREEN)
    typer.echo(pretty_json(order))


def print_deleted_order(order_id: str) -> None:
    typer.secho(
        f"Order '{order_id}' eliminada correctamente.",
        fg=typer.colors.GREEN,
    )
