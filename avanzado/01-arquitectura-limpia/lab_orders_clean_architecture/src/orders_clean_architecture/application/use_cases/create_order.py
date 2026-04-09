from orders_clean_architecture.application.dtos import (
    CreateOrderInput,
    CreateOrderOutput,
)
from orders_clean_architecture.application.event_bus import EventDispatcher
from orders_clean_architecture.application.presenters import CreateOrderPresenter
from orders_clean_architecture.domain.entities import Order, OrderItem
from orders_clean_architecture.domain.unit_of_work import AbstractUnitOfWork


class CreateOrderUseCase:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
        presenter: CreateOrderPresenter,
        event_dispatcher: EventDispatcher,
    ) -> None:
        self.uow = uow
        self.presenter = presenter
        self.event_dispatcher = event_dispatcher

    def execute(self, input_data: CreateOrderInput) -> dict[str, object]:
        items = [
            OrderItem(
                sku=item.sku,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
            for item in input_data.items
        ]

        with self.uow as uow:
            order = Order.create(
                order_id=input_data.order_id,
                customer_email=input_data.customer_email,
                items=items,
            )
            uow.orders.add(order)
            uow.commit()
            events = list(uow.collect_new_events())

        self.event_dispatcher.publish(events)

        output = CreateOrderOutput(
            order_id=order.id,
            customer_email=order.customer_email,
            total=order.total,
            status=order.status,
            message="Order created successfully",
        )
        return self.presenter.present(output)
