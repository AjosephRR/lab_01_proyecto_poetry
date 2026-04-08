from decimal import Decimal

from fastapi import Depends, FastAPI, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from app.application.dto import CreateOrderInputDTO
from app.application.use_cases import CreateOrderUseCase
from app.domain.ports import OrderNotifier, OrderRepository
from app.infrastructure.notifications.http_notification import (
    HttpNotificationAdapter,
    SimulatedHttpClient,
)
from app.infrastructure.persistence.db import get_session, init_db
from app.infrastructure.persistence.sqlalchemy_repository import (
    SQLAlchemyOrderRepository,
)

app = FastAPI(title="Lab 08 - Arquitectura Hexagonal")

_simulated_http_client = SimulatedHttpClient()
_notification_adapter = HttpNotificationAdapter(
    endpoint_url="https://notifications.local/orders",
    http_client=_simulated_http_client,
)


class CreateOrderRequest(BaseModel):
    customer_email: str
    item: str
    quantity: int
    unit_price: Decimal


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    order_id: str
    customer_email: str
    item: str
    quantity: int
    unit_price: Decimal
    total_amount: Decimal


@app.on_event("startup")
def on_startup() -> None:
    init_db()


def get_order_repository(
    session: Session = Depends(get_session),
) -> OrderRepository:
    return SQLAlchemyOrderRepository(session)


def get_order_notifier() -> OrderNotifier:
    return _notification_adapter


def get_create_order_use_case(
    repository: OrderRepository = Depends(get_order_repository),
    notifier: OrderNotifier = Depends(get_order_notifier),
) -> CreateOrderUseCase:
    return CreateOrderUseCase(repository=repository, notifier=notifier)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/orders",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    request: CreateOrderRequest,
    use_case: CreateOrderUseCase = Depends(get_create_order_use_case),
) -> OrderResponse:
    output = use_case.execute(
        CreateOrderInputDTO(
            customer_email=request.customer_email,
            item=request.item,
            quantity=request.quantity,
            unit_price=request.unit_price,
        )
    )

    return OrderResponse(
        order_id=output.order_id,
        customer_email=output.customer_email,
        item=output.item,
        quantity=output.quantity,
        unit_price=output.unit_price,
        total_amount=output.total_amount,
    )
