from app.crud import (
    create_order,
    create_user,
    get_user_by_email,
    get_user_with_orders,
    list_orders,
    update_order_status,
)
from app.db import SessionLocal


def main() -> None:
    with SessionLocal() as session:
        email = "joseph@example.com"

        user = create_user(session, name="Joseph", email=email)
        if user is None:
            print("El usuario ya existía. Lo voy a reutilizar.")
            user = get_user_by_email(session, email)

        if user is None:
            print("No se pudo obtener el usuario.")
            return

        order = create_order(
            session=session,
            user_id=user.id,
            items=[
                {
                    "product_name": "Teclado mecánico",
                    "quantity": 1,
                    "unit_price": 1200.0,
                },
                {"product_name": "Mouse", "quantity": 2, "unit_price": 350.0},
            ],
        )

        if order is None:
            print("No se pudo crear la orden.")
            return

        print(f"Orden creada con ID: {order.id}")
        print(f"Total calculado de la orden: {order.total}")

        updated_order = update_order_status(session, order.id, "paid")
        if updated_order is not None:
            print(f"Estado actualizado: {updated_order.status}")

        loaded_user = get_user_with_orders(session, user.id)
        if loaded_user is not None:
            print(f"Usuario: {loaded_user.name} | Órdenes: {len(loaded_user.orders)}")

        all_orders = list_orders(session)
        print(f"Órdenes registradas: {len(all_orders)}")


if __name__ == "__main__":
    main()
