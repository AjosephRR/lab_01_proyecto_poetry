from app.domain import Customer
from app.ports import CustomerRepository


def test_repository_contract_save_and_get_by_email(
    customer_repository: CustomerRepository,
) -> None:
    saved = customer_repository.save(
        Customer(
            id=None,
            name="Joseph Rivera",
            email="joseph@example.com",
            active=True,
        )
    )

    loaded = customer_repository.get_by_email("joseph@example.com")

    assert saved.id is not None
    assert loaded is not None
    assert loaded.id == saved.id
    assert loaded.email == "joseph@example.com"
    assert loaded.active is True


def test_repository_contract_save_updates_existing_customer(
    customer_repository: CustomerRepository,
) -> None:
    customer_repository.save(
        Customer(
            id=None,
            name="Joseph Rivera",
            email="joseph@example.com",
            active=True,
        )
    )

    updated = customer_repository.save(
        Customer(
            id=None,
            name="Joseph Actualizado",
            email="joseph@example.com",
            active=False,
        )
    )

    loaded = customer_repository.get_by_email("joseph@example.com")

    assert updated.id is not None
    assert loaded is not None
    assert loaded.name == "Joseph Actualizado"
    assert loaded.active is False


def test_repository_contract_list_all_returns_persisted_customers(
    customer_repository: CustomerRepository,
) -> None:
    customer_repository.save(
        Customer(id=None, name="A", email="a@example.com", active=True)
    )
    customer_repository.save(
        Customer(id=None, name="B", email="b@example.com", active=False)
    )

    customers = customer_repository.list_all()

    assert len(customers) == 2
    emails = {customer.email for customer in customers}
    assert emails == {"a@example.com", "b@example.com"}
