from pydantic import BaseModel, Field


class OrderItemRequest(BaseModel):
    sku: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)


class CreateOrderRequest(BaseModel):
    order_id: str = Field(min_length=1)
    customer_email: str = Field(min_length=3)
    items: list[OrderItemRequest] = Field(min_length=1)


class CreateOrderResponse(BaseModel):
    order_id: str
    customer_email: str
    items_count: int
    total: float
    status: str
