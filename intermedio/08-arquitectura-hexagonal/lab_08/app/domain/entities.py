from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

TWOPLACES = Decimal("0.01")


def money(value: Decimal) -> Decimal:
    return value.quantize(TWOPLACES, rounding=ROUND_HALF_UP)


@dataclass(slots=True, frozen=True)
class Order:
    order_id: str
    customer_email: str
    item: str
    quantity: int
    unit_price: Decimal

    def __post_init__(self) -> None:
        if not self.order_id.strip():
            raise ValueError("order_id no puede estar vacío.")

        if "@" not in self.customer_email:
            raise ValueError("customer_email no es válido.")

        if not self.item.strip():
            raise ValueError("item no puede estar vacío.")

        if self.quantity <= 0:
            raise ValueError("quantity debe ser mayor que 0.")

        if self.unit_price <= Decimal("0"):
            raise ValueError("unit_price debe ser mayor que 0.")

    @property
    def total_amount(self) -> Decimal:
        return money(self.unit_price * Decimal(self.quantity))
