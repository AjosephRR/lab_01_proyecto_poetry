import sys
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.ports import CustomerRepository  # noqa: E402
from app.providers import build_customer_repository  # noqa: E402


@pytest.fixture(params=["memory", "sqlite"])
def customer_repository(
    request: pytest.FixtureRequest,
) -> Generator[CustomerRepository, None, None]:
    repo_type = request.param

    if repo_type == "memory":
        yield build_customer_repository("memory")
        return

    with tempfile.TemporaryDirectory() as tmp_dir:
        db_path = str(Path(tmp_dir) / "customers.db")
        yield build_customer_repository("sqlite", db_path=db_path)
