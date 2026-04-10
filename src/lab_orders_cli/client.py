from __future__ import annotations

from typing import Any

import httpx
from lab_orders_cli.config import Settings


class ApiError(Exception):
    """Error controlado para mostrar mensajes claros en el CLI."""


class OrdersApiClient:
    def __init__(self, settings: Settings) -> None:
        self.base_url = settings.base_url.rstrip("/")
        self.timeout = settings.timeout

    def list_orders(self) -> list[dict[str, Any]]:
        data = self._request("GET", "/orders")

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            for key in ("items", "data", "orders"):
                value = data.get(key)
                if isinstance(value, list):
                    return value

        raise ApiError(
            "La respuesta de GET /orders no tiene el formato esperado. "
            "Revisa el schema real de tu API."
        )

    def create_order(self, payload: dict[str, Any]) -> dict[str, Any]:
        data = self._request("POST", "/orders", json_body=payload)

        if not isinstance(data, dict):
            raise ApiError("La respuesta de POST /orders no devolvió un objeto JSON.")

        return data

    def delete_order(self, order_id: str) -> None:
        self._request("DELETE", f"/orders/{order_id}")

    def _request(
        self,
        method: str,
        path: str,
        json_body: dict[str, Any] | None = None,
    ) -> Any:
        try:
            with httpx.Client(base_url=self.base_url, timeout=self.timeout) as client:
                response = client.request(method, path, json=json_body)
                response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            detail = self._extract_detail(exc.response)
            raise ApiError(
                f"{method} {path} respondió {exc.response.status_code}. {detail}"
            ) from exc
        except httpx.RequestError as exc:
            raise ApiError(
                f"No se pudo conectar a la API en {self.base_url}. "
                "Revisa que la API esté levantada y que "
                "ORDERS_API_BASE_URL sea correcto."
            ) from exc

        if response.status_code == 204:
            return None

        if not response.text.strip():
            return None

        try:
            return response.json()
        except ValueError as exc:
            raise ApiError("La API respondió algo que no es JSON válido.") from exc

    @staticmethod
    def _extract_detail(response: httpx.Response) -> str:
        try:
            data = response.json()
            if isinstance(data, dict) and "detail" in data:
                return str(data["detail"])
            return str(data)
        except ValueError:
            text = response.text.strip()
            return text[:300] if text else "Sin detalle en la respuesta."
