from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities import Order
from app.infrastructure.persistence.sqlalchemy_models import OrderModel


class SQLAlchemyOrderRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, order: Order) -> Order:
        model = OrderModel(
            order_id=order.order_id,
            customer_email=order.customer_email,
            item=order.item,
            quantity=order.quantity,
            unit_price=order.unit_price,
        )

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return self._to_entity(model)

    def get_by_id(self, order_id: str) -> Order | None:
        model = self.session.get(OrderModel, order_id)

        if model is None:
            return None

        return self._to_entity(model)

    def list_all(self) -> list[Order]:
        models = self.session.scalars(
            select(OrderModel).order_by(OrderModel.order_id)
        ).all()

        return [self._to_entity(model) for model in models]

    @staticmethod
    def _to_entity(model: OrderModel) -> Order:
        return Order(
            order_id=model.order_id,
            customer_email=model.customer_email,
            item=model.item,
            quantity=model.quantity,
            unit_price=model.unit_price,
        )
