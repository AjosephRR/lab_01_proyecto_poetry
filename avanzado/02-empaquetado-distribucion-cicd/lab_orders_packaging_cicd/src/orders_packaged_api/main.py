from fastapi import FastAPI, HTTPException, Response, status

from orders_packaged_api.schemas import CreateOrderRequest, CreateOrderResponse

app = FastAPI(title="Orders Packaged API", version="0.1.0")

# Base de datos en memoria para el laboratorio
ORDERS_DB: dict[str, dict] = {}


@app.get("/health", status_code=status.HTTP_200_OK)
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/orders", status_code=status.HTTP_201_CREATED, response_model=CreateOrderResponse
)
def create_order(payload: CreateOrderRequest) -> CreateOrderResponse:
    total = round(
        sum(item.quantity * item.unit_price for item in payload.items),
        2,
    )

    order = CreateOrderResponse(
        order_id=payload.order_id,
        customer_email=payload.customer_email,
        items_count=len(payload.items),
        total=total,
        status="CREATED",
    )

    # Guardar la order para poder listarla y borrarla después
    ORDERS_DB[payload.order_id] = order.model_dump()

    return order


@app.get("/orders", status_code=status.HTTP_200_OK)
def list_orders() -> list[dict]:
    return list(ORDERS_DB.values())


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: str) -> Response:
    if order_id not in ORDERS_DB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    del ORDERS_DB[order_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
