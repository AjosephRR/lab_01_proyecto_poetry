from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from math import isqrt
from time import perf_counter


@dataclass(slots=True)
class CpuResult:
    mode: str
    inputs: list[int]
    outputs: list[int]
    elapsed_seconds: float


def count_primes(limit: int) -> int:
    total = 0

    for number in range(2, limit + 1):
        prime = True
        root = isqrt(number)

        for divisor in range(2, root + 1):
            if number % divisor == 0:
                prime = False
                break

        if prime:
            total += 1

    return total


def run_cpu_serial(limits: list[int]) -> CpuResult:
    start = perf_counter()
    outputs = [count_primes(limit) for limit in limits]
    elapsed = perf_counter() - start

    return CpuResult(
        mode="cpu-serial",
        inputs=limits,
        outputs=outputs,
        elapsed_seconds=elapsed,
    )


def run_cpu_process_pool(
    limits: list[int],
    max_workers: int | None = None,
) -> CpuResult:
    start = perf_counter()

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        outputs = list(executor.map(count_primes, limits))

    elapsed = perf_counter() - start

    return CpuResult(
        mode="cpu-process-pool",
        inputs=limits,
        outputs=outputs,
        elapsed_seconds=elapsed,
    )
