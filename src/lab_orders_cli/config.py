from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    base_url: str
    timeout: float


def get_settings() -> Settings:
    base_url = os.getenv("ORDERS_API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
    timeout_raw = os.getenv("ORDERS_API_TIMEOUT", "10")

    try:
        timeout = float(timeout_raw)
    except ValueError:
        timeout = 10.0

    return Settings(
        base_url=base_url,
        timeout=timeout,
    )
