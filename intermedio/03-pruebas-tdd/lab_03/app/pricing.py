from decimal import ROUND_HALF_UP, Decimal

from app.models import OrderItem

TWOPLACES = Decimal("0.01")


def validate_discount(discount_percent: int) -> None:
    if not 0 <= discount_percent <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")


def validate_item(item: OrderItem) -> None:
    if not item.product_name.strip():
        raise ValueError("El nombre del producto no puede estar vacío")

    if item.quantity <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    if item.unit_price <= Decimal("0"):
        raise ValueError("El precio unitario debe ser mayor que cero")


def calculate_subtotal(items: list[OrderItem]) -> Decimal:
    if not items:
        raise ValueError("La orden debe tener al menos un item")

    subtotal = Decimal("0.00")

    for item in items:
        validate_item(item)
        subtotal += item.unit_price * item.quantity

    return subtotal.quantize(TWOPLACES, rounding=ROUND_HALF_UP)


def apply_discount(subtotal: Decimal, discount_percent: int) -> Decimal:
    if subtotal < Decimal("0"):
        raise ValueError("El subtotal no puede ser negativo")

    validate_discount(discount_percent)

    discount_amount = subtotal * Decimal(discount_percent) / Decimal("100")
    total = subtotal - discount_amount
    return total.quantize(TWOPLACES, rounding=ROUND_HALF_UP)


def calculate_total(items: list[OrderItem], discount_percent: int = 0) -> Decimal:
    subtotal = calculate_subtotal(items)
    return apply_discount(subtotal, discount_percent)
