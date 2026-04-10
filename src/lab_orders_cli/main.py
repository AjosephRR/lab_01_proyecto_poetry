from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer
from lab_orders_cli.client import ApiError, OrdersApiClient
from lab_orders_cli.config import get_settings
from lab_orders_cli.render import (
    pretty_json,
    print_config,
    print_created_order,
    print_deleted_order,
    print_orders,
)

app = typer.Typer(
    help="CLI para gestionar orders consumiendo la API.",
    no_args_is_help=True,
    add_completion=False,
)


def load_payload(payload_file: Path) -> dict[str, Any]:
    try:
        content = payload_file.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise typer.BadParameter(f"No se encontró el archivo: {payload_file}") from exc

    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter(
            f"JSON inválido en {payload_file}. Línea {exc.lineno}, columna {exc.colno}."
        ) from exc

    if not isinstance(data, dict):
        raise typer.BadParameter("El archivo JSON debe contener un objeto en la raíz.")

    return data


@app.command("config")
def show_config() -> None:
    settings = get_settings()
    print_config(settings)


@app.command("list")
def list_orders(
    raw: bool = typer.Option(
        False,
        "--raw",
        help="Muestra la respuesta en JSON completo.",
    ),
) -> None:
    settings = get_settings()
    client = OrdersApiClient(settings)

    try:
        orders = client.list_orders()
    except ApiError as exc:
        typer.secho(f"Error: {exc}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc

    if raw:
        typer.echo(pretty_json(orders))
        return

    print_orders(orders)


@app.command("create")
def create_order(
    payload_file: Path = typer.Option(
        ...,
        "--payload-file",
        exists=True,
        dir_okay=False,
        readable=True,
        help="Ruta al archivo JSON con el payload del POST /orders.",
    ),
) -> None:
    payload = load_payload(payload_file)
    settings = get_settings()
    client = OrdersApiClient(settings)

    try:
        created_order = client.create_order(payload)
    except ApiError as exc:
        typer.secho(f"Error: {exc}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc

    print_created_order(created_order)


@app.command("delete")
def delete_order(
    order_id: str = typer.Argument(..., help="ID de la order a eliminar."),
) -> None:
    settings = get_settings()
    client = OrdersApiClient(settings)

    try:
        client.delete_order(order_id)
    except ApiError as exc:
        typer.secho(f"Error: {exc}", fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc

    print_deleted_order(order_id)


if __name__ == "__main__":
    app()
