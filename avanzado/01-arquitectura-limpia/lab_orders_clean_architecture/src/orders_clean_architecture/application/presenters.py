from typing import Protocol

from orders_clean_architecture.application.dtos import CreateOrderOutput


class CreateOrderPresenter(Protocol):
    def present(self, output: CreateOrderOutput) -> dict[str, object]: ...


class JsonCreateOrderPresenter:
    def present(self, output: CreateOrderOutput) -> dict[str, object]:
        return {
            "order_id": output.order_id,
            "customer_email": output.customer_email,
            "total": output.total,
            "status": output.status,
            "message": output.message,
        }
