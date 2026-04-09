from orders_clean_architecture.application.dtos import (
    CreateOrderInput,
    CreateOrderItemInput,
)
from orders_clean_architecture.application.event_bus import EventDispatcher
from orders_clean_architecture.application.event_handlers import (
    InMemoryAuditLog,
    OrderCreatedAuditHandler,
)
from orders_clean_architecture.application.presenters import JsonCreateOrderPresenter
from orders_clean_architecture.application.use_cases.create_order import (
    CreateOrderUseCase,
)
from orders_clean_architecture.domain.events import OrderCreated
from orders_clean_architecture.infrastructure.uow.in_memory_unit_of_work import (
    InMemoryUnitOfWork,
)


def test_create_order_use_case_persists_order_and_publishes_event() -> None:
    storage = {}
    audit_log = InMemoryAuditLog()
    dispatcher = EventDispatcher()
    dispatcher.register(OrderCreated, OrderCreatedAuditHandler(audit_log))

    use_case = CreateOrderUseCase(
        uow=InMemoryUnitOfWork(storage),
        presenter=JsonCreateOrderPresenter(),
        event_dispatcher=dispatcher,
    )

    response = use_case.execute(
        CreateOrderInput(
            order_id="ORD-100",
            customer_email="clean@example.com",
            items=[
                CreateOrderItemInput(sku="A-1", quantity=2, unit_price=10.0),
                CreateOrderItemInput(sku="B-1", quantity=1, unit_price=20.0),
            ],
        )
    )

    assert response["order_id"] == "ORD-100"
    assert response["total"] == 40.0
    assert "ORD-100" in storage
    assert storage["ORD-100"].total == 40.0
    assert audit_log.entries == ["ORDER_CREATED::ORD-100::clean@example.com::40.00"]
