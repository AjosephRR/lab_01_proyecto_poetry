from fastapi import APIRouter, HTTPException, status

from app.deps import CurrentUser, DbSession
from app.models import Order
from app.schemas import OrderCreate, OrderRead, OrderUpdate

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(
    payload: OrderCreate,
    db: DbSession,
    current_user: CurrentUser,
) -> OrderRead:
    order = Order(
        title=payload.title,
        description=payload.description,
        total_amount=payload.total_amount,
        status=payload.status,
        owner_id=current_user.id,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("/", response_model=list[OrderRead])
def list_orders(
    db: DbSession,
    current_user: CurrentUser,
) -> list[OrderRead]:
    orders = (
        db.query(Order)
        .filter(Order.owner_id == current_user.id)
        .order_by(Order.id.asc())
        .all()
    )
    return orders


@router.get("/{order_id}", response_model=OrderRead)
def get_order(
    order_id: int,
    db: DbSession,
    current_user: CurrentUser,
) -> OrderRead:
    order = (
        db.query(Order)
        .filter(Order.id == order_id, Order.owner_id == current_user.id)
        .first()
    )
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada",
        )
    return order


@router.put("/{order_id}", response_model=OrderRead)
def update_order(
    order_id: int,
    payload: OrderUpdate,
    db: DbSession,
    current_user: CurrentUser,
) -> OrderRead:
    order = (
        db.query(Order)
        .filter(Order.id == order_id, Order.owner_id == current_user.id)
        .first()
    )
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada",
        )

    update_data = payload.model_dump(exclude_unset=True)

    for field_name, value in update_data.items():
        setattr(order, field_name, value)

    db.commit()
    db.refresh(order)
    return order


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(
    order_id: int,
    db: DbSession,
    current_user: CurrentUser,
) -> None:
    order = (
        db.query(Order)
        .filter(Order.id == order_id, Order.owner_id == current_user.id)
        .first()
    )
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada",
        )

    db.delete(order)
    db.commit()
    return None
