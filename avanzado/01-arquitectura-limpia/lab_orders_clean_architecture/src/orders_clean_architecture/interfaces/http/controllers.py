from fastapi import APIRouter, Depends, FastAPI, status
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
from orders_clean_architecture.domain.entities import Order
from orders_clean_architecture.domain.events import OrderCreated
from orders_clean_architecture.infrastructure.uow.in_memory_unit_of_work import (
    InMemoryUnitOfWork,
)
from pydantic import BaseModel, Field


class CreateOrderItemRequest(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)


class CreateOrderRequest(BaseModel):
    order_id: str = Field(min_length=1)
    customer_email: str = Field(min_length=3)
    items: list[CreateOrderItemRequest] = Field(min_length=1)


ORDER_STORAGE: dict[str, Order] = {}
AUDIT_LOG = InMemoryAuditLog()
EVENT_DISPATCHER = EventDispatcher()
EVENT_DISPATCHER.register(OrderCreated, OrderCreatedAuditHandler(AUDIT_LOG))


def build_create_order_use_case() -> CreateOrderUseCase:
    return CreateOrderUseCase(
        uow=InMemoryUnitOfWork(ORDER_STORAGE),
        presenter=JsonCreateOrderPresenter(),
        event_dispatcher=EVENT_DISPATCHER,
    )


router = APIRouter()


@router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(
    request: CreateOrderRequest,
    use_case: CreateOrderUseCase = Depends(build_create_order_use_case),
) -> dict[str, object]:
    input_data = CreateOrderInput(
        order_id=request.order_id,
        customer_email=request.customer_email,
        items=[
            CreateOrderItemInput(
                sku=item.sku,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
            for item in request.items
        ],
    )
    return use_case.execute(input_data)


@router.get("/audit-log", status_code=status.HTTP_200_OK)
def get_audit_log() -> dict[str, list[str]]:
    return {"entries": AUDIT_LOG.entries}


app = FastAPI(title="Orders Clean Architecture Lab")
app.include_router(router)
