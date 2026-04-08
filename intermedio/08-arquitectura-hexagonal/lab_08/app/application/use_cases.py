from uuid import uuid4

from app.application.dto import CreateOrderInputDTO, OrderOutputDTO
from app.domain.entities import Order
from app.domain.ports import OrderNotifier, OrderRepository


class CreateOrderUseCase:
    def __init__(
        self,
        repository: OrderRepository,
        notifier: OrderNotifier,
    ) -> None:
        self.repository = repository
        self.notifier = notifier

    def execute(self, input_dto: CreateOrderInputDTO) -> OrderOutputDTO:
        order = Order(
            order_id=str(uuid4()),
            customer_email=input_dto.customer_email,
            item=input_dto.item,
            quantity=input_dto.quantity,
            unit_price=input_dto.unit_price,
        )

        saved_order = self.repository.save(order)
        self.notifier.notify_order_created(saved_order)

        return OrderOutputDTO(
            order_id=saved_order.order_id,
            customer_email=saved_order.customer_email,
            item=saved_order.item,
            quantity=saved_order.quantity,
            unit_price=saved_order.unit_price,
            total_amount=saved_order.total_amount,
        )
