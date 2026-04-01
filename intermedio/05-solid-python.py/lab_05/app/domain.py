from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, slots=True)
class Customer:
    id: Optional[int]
    name: str
    email: str
    active: bool = True


class DuplicateCustomerError(ValueError):
    pass


class CustomerNotFoundError(ValueError):
    pass
