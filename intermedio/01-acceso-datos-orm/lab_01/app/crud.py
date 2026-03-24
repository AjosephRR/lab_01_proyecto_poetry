from typing import Any

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from app.models import Order, OrderItem, User


def get_user_by_email(session: Session, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    return session.scalar(stmt)


def create_user(session: Session, name: str, email: str) -> User | None:
    user = User(name=name, email=email)
    session.add(user)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        return None

    session.refresh(user)
    return user


def create_order(
    session: Session,
    user_id: int,
    items: list[dict[str, Any]],
    status: str = "pending",
) -> Order | None:
    user = session.get(User, user_id)
    if user is None:
        return None

    order = Order(user_id=user_id, status=status)

    for item in items:
        order.items.append(
            OrderItem(
                product_name=item["product_name"],
                quantity=item["quantity"],
                unit_price=item["unit_price"],
            )
        )

    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def get_user_with_orders(session: Session, user_id: int) -> User | None:
    stmt = (
        select(User)
        .options(selectinload(User.orders).selectinload(Order.items))
        .where(User.id == user_id)
    )
    return session.scalar(stmt)


def list_orders(session: Session) -> list[Order]:
    stmt = (
        select(Order)
        .options(selectinload(Order.user), selectinload(Order.items))
        .order_by(Order.id)
    )
    return list(session.scalars(stmt).unique())


def update_order_status(
    session: Session,
    order_id: int,
    new_status: str,
) -> Order | None:
    order = session.get(Order, order_id)
    if order is None:
        return None

    order.status = new_status
    session.commit()
    session.refresh(order)
    return order


def delete_order(session: Session, order_id: int) -> bool:
    order = session.get(Order, order_id)
    if order is None:
        return False

    session.delete(order)
    session.commit()
    return True
