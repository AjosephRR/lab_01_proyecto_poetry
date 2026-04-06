from decimal import Decimal

from lab_patterns.pricing.service import PricingContext
from lab_patterns.pricing.strategies import PercentageDiscountStrategy
from lab_patterns.providers.adapter import ExternalProductAdapter
from lab_patterns.providers.external_provider import ExternalCatalogProvider


def main() -> None:
    provider = ExternalCatalogProvider()
    adapter = ExternalProductAdapter(provider)

    product = adapter.get_product("EXT-001")

    pricing = PricingContext(strategy=PercentageDiscountStrategy(Decimal("0.15")))

    final_price = pricing.final_price(product)

    print(f"Producto: {product.name}")
    print(f"Precio base: {product.base_price} {product.currency}")
    print(f"Precio final: {final_price} {product.currency}")

    # Segunda llamada al mismo SKU: debería usar caché
    adapter.get_product("EXT-001")
    print(f"Llamadas reales al proveedor: {provider.call_count}")


if __name__ == "__main__":
    main()
