from dataclasses import dataclass, field
from typing import Any

from lab_patterns.utils.cache import cache_result


class ExternalProviderError(Exception):
    pass


@dataclass(slots=True)
class ExternalCatalogProvider:
    call_count: int = 0
    _catalog: dict[str, dict[str, Any]] = field(
        default_factory=lambda: {
            "EXT-001": {
                "sku_code": "EXT-001",
                "description": "Laptop Pro 14",
                "unit_price": 25000,
                "currency": "MXN",
            },
            "EXT-002": {
                "sku_code": "EXT-002",
                "description": "Monitor 27 pulgadas",
                "unit_price": 5800,
                "currency": "MXN",
            },
        }
    )

    @cache_result
    def fetch_product(self, external_sku: str) -> dict[str, Any]:
        self.call_count += 1

        if external_sku not in self._catalog:
            raise ExternalProviderError(f"Producto no encontrado: {external_sku}")

        return self._catalog[external_sku]
