from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field, field_validator

ALLOWED_STATUSES = {"pending", "paid", "cancelled"}


class UserCreate(BaseModel):
    username: str = Field(min_length=4, max_length=50, examples=["joseph"])
    full_name: str = Field(min_length=3, max_length=120, examples=["Joseph Rivera"])
    password: str = Field(min_length=6, max_length=64, examples=["MiClave123"])

    @field_validator("username")
    @classmethod
    def username_without_spaces(cls, value: str) -> str:
        value = value.strip().lower()
        if " " in value:
            raise ValueError("El username no debe contener espacios")
        return value


class UserRead(BaseModel):
    id: int
    username: str
    full_name: str
    is_active: bool

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str


class OrderCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120, examples=["Compra de periféricos"])
    description: str | None = Field(default=None, max_length=500)
    total_amount: Decimal = Field(gt=0, examples=[1500.50])
    status: Literal["pending", "paid", "cancelled"] = "pending"


class OrderUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    total_amount: Decimal | None = Field(default=None, gt=0)
    status: Literal["pending", "paid", "cancelled"] | None = None


class OrderRead(BaseModel):
    id: int
    title: str
    description: str | None
    total_amount: Decimal
    status: str
    owner_id: int

    model_config = {"from_attributes": True}
