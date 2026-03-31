from __future__ import annotations

import asyncio
from dataclasses import dataclass
from time import perf_counter

import httpx


@dataclass(slots=True)
class FetchResult:
    mode: str
    total_requests: int
    elapsed_seconds: float
    payloads: list[dict[str, object]]


def fetch_sync(
    base_url: str,
    item_ids: list[int],
    delay: float = 0.30,
    timeout: float = 10.0,
) -> FetchResult:
    start = perf_counter()
    payloads: list[dict[str, object]] = []

    with httpx.Client(base_url=base_url, timeout=timeout) as client:
        for item_id in item_ids:
            response = client.get(f"/items/{item_id}", params={"delay": delay})
            response.raise_for_status()
            payloads.append(response.json())

    elapsed = perf_counter() - start
    return FetchResult(
        mode="sync",
        total_requests=len(item_ids),
        elapsed_seconds=elapsed,
        payloads=payloads,
    )


async def _fetch_one(
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    item_id: int,
    delay: float,
) -> dict[str, object]:
    async with semaphore:
        response = await client.get(f"/items/{item_id}", params={"delay": delay})
        response.raise_for_status()
        return response.json()


async def fetch_async(
    base_url: str,
    item_ids: list[int],
    delay: float = 0.30,
    timeout: float = 10.0,
    max_concurrency: int = 5,
) -> FetchResult:
    start = perf_counter()
    semaphore = asyncio.Semaphore(max_concurrency)

    async with httpx.AsyncClient(base_url=base_url, timeout=timeout) as client:
        tasks = [
            _fetch_one(client, semaphore, item_id=item_id, delay=delay)
            for item_id in item_ids
        ]
        payloads = await asyncio.gather(*tasks)

    elapsed = perf_counter() - start
    return FetchResult(
        mode="async",
        total_requests=len(item_ids),
        elapsed_seconds=elapsed,
        payloads=payloads,
    )
