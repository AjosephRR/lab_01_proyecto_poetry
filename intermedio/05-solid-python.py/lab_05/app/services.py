from app.domain import Customer, CustomerNotFoundError, DuplicateCustomerError
from app.ports import CustomerReader, CustomerWriter


class RegisterCustomerService:
    def __init__(self, reader: CustomerReader, writer: CustomerWriter) -> None:
        self._reader = reader
        self._writer = writer

    def execute(self, name: str, email: str) -> Customer:
        if not name.strip():
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in email:
            raise ValueError("El email no es válido")

        existing = self._reader.get_by_email(email)
        if existing is not None:
            raise DuplicateCustomerError("Ya existe un cliente con ese email")

        customer = Customer(
            id=None, name=name.strip(), email=email.strip(), active=True
        )
        return self._writer.save(customer)


class ListActiveCustomersService:
    def __init__(self, reader: CustomerReader) -> None:
        self._reader = reader

    def execute(self) -> list[Customer]:
        return [customer for customer in self._reader.list_all() if customer.active]


class DeactivateCustomerService:
    def __init__(self, reader: CustomerReader, writer: CustomerWriter) -> None:
        self._reader = reader
        self._writer = writer

    def execute(self, email: str) -> Customer:
        customer = self._reader.get_by_email(email)
        if customer is None:
            raise CustomerNotFoundError("Cliente no encontrado")

        updated = Customer(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            active=False,
        )
        return self._writer.save(updated)
