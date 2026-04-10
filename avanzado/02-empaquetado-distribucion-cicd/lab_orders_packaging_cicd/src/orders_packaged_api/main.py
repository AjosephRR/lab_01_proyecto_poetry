from fastapi import FastAPI, status

from orders_packaged_api.schemas import CreateOrderRequest, CreateOrderResponse

app = FastAPI(title="Orders Packaged API", version="0.1.0")


@app.get("/health", status_code=status.HTTP_200_OK)
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/orders", status_code=status.HTTP_201_CREATED, response_model=CreateOrderResponse)
def create_order(payload: CreateOrderRequest) -> CreateOrderResponse:
    total = round(
        sum(item.quantity * item.unit_price for item in payload.items),
        2,
    )

    return CreateOrderResponse(
        order_id=payload.order_id,
        customer_email=payload.customer_email,
        items_count=len(payload.items),
        total=total,
        status="CREATED",
    )
