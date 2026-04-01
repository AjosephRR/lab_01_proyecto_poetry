from typing import Protocol

from app.domain import Customer


class CustomerReader(Protocol):
    def get_by_email(self, email: str) -> Customer | None: ...

    def list_all(self) -> list[Customer]: ...


class CustomerWriter(Protocol):
    def save(self, customer: Customer) -> Customer: ...


class CustomerRepository(CustomerReader, CustomerWriter, Protocol):
    pass
