from typing import Literal

from app.ports import CustomerRepository
from app.repositories import InMemoryCustomerRepository, SqliteCustomerRepository


def build_customer_repository(
    kind: Literal["memory", "sqlite"],
    db_path: str | None = None,
) -> CustomerRepository:
    if kind == "memory":
        return InMemoryCustomerRepository()

    if kind == "sqlite":
        if db_path is None:
            raise ValueError("db_path es obligatorio para el repositorio sqlite")
        return SqliteCustomerRepository(db_path=db_path)

    raise ValueError(f"Tipo de repositorio no soportado: {kind}")
