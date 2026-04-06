from decimal import Decimal

import pytest
from lab_patterns.providers.adapter import ExternalProductAdapter
from lab_patterns.providers.external_provider import (
    ExternalCatalogProvider,
    ExternalProviderError,
)


def test_adapter_maps_external_payload_to_product() -> None:
    provider = ExternalCatalogProvider()
    adapter = ExternalProductAdapter(provider)

    product = adapter.get_product("EXT-002")

    assert product.sku == "EXT-002"
    assert product.name == "Monitor 27 pulgadas"
    assert product.base_price == Decimal("5800")
    assert product.currency == "MXN"


def test_adapter_raises_when_product_not_found() -> None:
    provider = ExternalCatalogProvider()
    adapter = ExternalProductAdapter(provider)

    with pytest.raises(ExternalProviderError, match="Producto no encontrado"):
        adapter.get_product("NO-EXISTE")
