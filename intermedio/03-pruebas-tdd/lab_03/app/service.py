from decimal import Decimal

from app.models import Order
from app.notifications import NotificationGateway
from app.pricing import calculate_total, validate_discount


def confirm_order(order: Order) -> Order:
    if not order.items:
        raise ValueError("No se puede confirmar una orden sin items")

    validate_discount(order.discount_percent)
    order.status = "confirmed"
    return order


def mark_order_as_paid(order: Order) -> Order:
    if order.status != "confirmed":
        raise ValueError("Solo una orden confirmada puede marcarse como pagada")

    order.status = "paid"
    return order


def checkout(order: Order, gateway: NotificationGateway) -> Decimal:
    confirm_order(order)
    total = calculate_total(order.items, order.discount_percent)
    mark_order_as_paid(order)

    message = (
        f"Tu compra fue procesada correctamente. "
        f"Orden #{order.id}. Total pagado: {total}"
    )

    notification_sent = gateway.send(order.customer_email, message)
    if not notification_sent:
        raise RuntimeError("No se pudo enviar la notificación")

    return total
