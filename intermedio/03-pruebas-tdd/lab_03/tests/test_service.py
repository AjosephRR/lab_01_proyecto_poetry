from decimal import Decimal
from unittest.mock import Mock

import pytest

from app.models import Order
from app.service import checkout, confirm_order, mark_order_as_paid


@pytest.mark.unit
def test_confirm_order_changes_status(sample_order: Order) -> None:
    result = confirm_order(sample_order)
    assert result.status == "confirmed"


@pytest.mark.unit
def test_mark_order_as_paid_requires_confirmed_status(sample_order: Order) -> None:
    with pytest.raises(ValueError, match="confirmada"):
        mark_order_as_paid(sample_order)


@pytest.mark.unit
def test_checkout_marks_order_as_paid_and_sends_notification(
    sample_order: Order,
) -> None:
    gateway = Mock()
    gateway.send.return_value = True

    total = checkout(sample_order, gateway)

    assert total == Decimal("1710.00")
    assert sample_order.status == "paid"
    gateway.send.assert_called_once()

    called_email = gateway.send.call_args.args[0]
    called_message = gateway.send.call_args.args[1]

    assert called_email == "joseph@example.com"
    assert "Orden #1" in called_message
    assert "1710.00" in called_message


@pytest.mark.unit
def test_checkout_raises_if_notification_fails(sample_order: Order) -> None:
    gateway = Mock()
    gateway.send.return_value = False

    with pytest.raises(RuntimeError, match="notificación"):
        checkout(sample_order, gateway)
