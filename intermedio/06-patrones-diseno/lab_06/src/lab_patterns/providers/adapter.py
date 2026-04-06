from dataclasses import dataclass
from decimal import Decimal

from lab_patterns.domain.models import Product
from lab_patterns.providers.external_provider import ExternalCatalogProvider


@dataclass(slots=True, frozen=True)
class ExternalProductAdapter:
    provider: ExternalCatalogProvider

    def get_product(self, external_sku: str) -> Product:
        payload = self.provider.fetch_product(external_sku)

        return Product(
            sku=payload["sku_code"],
            name=payload["description"],
            base_price=Decimal(str(payload["unit_price"])),
            currency=payload["currency"],
        )
