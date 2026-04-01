import sqlite3
from contextlib import closing
from pathlib import Path

from app.domain import Customer
from app.ports import CustomerRepository


class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self) -> None:
        self._items_by_email: dict[str, Customer] = {}
        self._next_id = 1

    def save(self, customer: Customer) -> Customer:
        existing = self._items_by_email.get(customer.email)

        if existing is None:
            saved = Customer(
                id=self._next_id,
                name=customer.name,
                email=customer.email,
                active=customer.active,
            )
            self._next_id += 1
        else:
            saved = Customer(
                id=existing.id,
                name=customer.name,
                email=customer.email,
                active=customer.active,
            )

        self._items_by_email[saved.email] = saved
        return saved

    def get_by_email(self, email: str) -> Customer | None:
        return self._items_by_email.get(email)

    def list_all(self) -> list[Customer]:
        return sorted(
            self._items_by_email.values(),
            key=lambda customer: customer.id or 0,
        )


class SqliteCustomerRepository(CustomerRepository):
    def __init__(self, db_path: str) -> None:
        self._db_path = Path(db_path)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with closing(self._connect()) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    active INTEGER NOT NULL
                )
                """
            )
            connection.commit()

    def save(self, customer: Customer) -> Customer:
        with closing(self._connect()) as connection:
            existing = connection.execute(
                "SELECT id FROM customers WHERE email = ?",
                (customer.email,),
            ).fetchone()

            if existing is None:
                connection.execute(
                    "INSERT INTO customers (name, email, active) VALUES (?, ?, ?)",
                    (customer.name, customer.email, int(customer.active)),
                )
            else:
                connection.execute(
                    "UPDATE customers SET name = ?, active = ? WHERE email = ?",
                    (customer.name, int(customer.active), customer.email),
                )

            connection.commit()

            row = connection.execute(
                "SELECT id, name, email, active FROM customers WHERE email = ?",
                (customer.email,),
            ).fetchone()

        if row is None:
            raise RuntimeError("No se pudo persistir el cliente")

        return Customer(
            id=int(row["id"]),
            name=str(row["name"]),
            email=str(row["email"]),
            active=bool(row["active"]),
        )

    def get_by_email(self, email: str) -> Customer | None:
        with closing(self._connect()) as connection:
            row = connection.execute(
                "SELECT id, name, email, active FROM customers WHERE email = ?",
                (email,),
            ).fetchone()

        if row is None:
            return None

        return Customer(
            id=int(row["id"]),
            name=str(row["name"]),
            email=str(row["email"]),
            active=bool(row["active"]),
        )

    def list_all(self) -> list[Customer]:
        with closing(self._connect()) as connection:
            rows = connection.execute(
                "SELECT id, name, email, active FROM customers ORDER BY id"
            ).fetchall()

        return [
            Customer(
                id=int(row["id"]),
                name=str(row["name"]),
                email=str(row["email"]),
                active=bool(row["active"]),
            )
            for row in rows
        ]
