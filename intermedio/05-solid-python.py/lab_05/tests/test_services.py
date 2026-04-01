import pytest

from app.domain import Customer, CustomerNotFoundError, DuplicateCustomerError
from app.ports import CustomerRepository
from app.services import (
    DeactivateCustomerService,
    ListActiveCustomersService,
    RegisterCustomerService,
)


def test_register_customer_creates_customer(
    customer_repository: CustomerRepository,
) -> None:
    service = RegisterCustomerService(
        reader=customer_repository,
        writer=customer_repository,
    )

    customer = service.execute(name="Joseph Rivera", email="joseph@example.com")

    assert customer.id is not None
    assert customer.name == "Joseph Rivera"
    assert customer.email == "joseph@example.com"
    assert customer.active is True


def test_register_customer_rejects_duplicate_email(
    customer_repository: CustomerRepository,
) -> None:
    service = RegisterCustomerService(
        reader=customer_repository,
        writer=customer_repository,
    )

    service.execute(name="Joseph Rivera", email="joseph@example.com")

    with pytest.raises(DuplicateCustomerError, match="ya existe|Ya existe"):
        service.execute(name="Otro Nombre", email="joseph@example.com")


def test_list_active_customers_returns_only_active(
    customer_repository: CustomerRepository,
) -> None:
    customer_repository.save(
        Customer(id=None, name="Activo 1", email="activo1@example.com", active=True)
    )
    customer_repository.save(
        Customer(id=None, name="Activo 2", email="activo2@example.com", active=True)
    )
    customer_repository.save(
        Customer(id=None, name="Inactivo", email="inactivo@example.com", active=False)
    )

    service = ListActiveCustomersService(reader=customer_repository)
    active_customers = service.execute()

    assert len(active_customers) == 2
    assert all(customer.active is True for customer in active_customers)


def test_deactivate_customer_changes_state(
    customer_repository: CustomerRepository,
) -> None:
    customer_repository.save(
        Customer(id=None, name="Joseph", email="joseph@example.com", active=True)
    )

    service = DeactivateCustomerService(
        reader=customer_repository,
        writer=customer_repository,
    )

    updated = service.execute("joseph@example.com")

    assert updated.active is False
    assert customer_repository.get_by_email("joseph@example.com") is not None
    assert customer_repository.get_by_email("joseph@example.com").active is False


def test_deactivate_customer_raises_if_not_found(
    customer_repository: CustomerRepository,
) -> None:
    service = DeactivateCustomerService(
        reader=customer_repository,
        writer=customer_repository,
    )

    with pytest.raises(CustomerNotFoundError, match="Cliente no encontrado"):
        service.execute("missing@example.com")
