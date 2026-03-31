from __future__ import annotations

import argparse
import asyncio
from timeit import repeat

from app.cpu_bound import run_cpu_process_pool, run_cpu_serial
from app.fetchers import fetch_async, fetch_sync

DEFAULT_BASE_URL = "http://127.0.0.1:8001"


def print_header(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def benchmark_fetch_compare(
    base_url: str,
    total_requests: int,
    delay: float,
    max_concurrency: int,
) -> None:
    item_ids = list(range(1, total_requests + 1))

    print_header("Comparación I/O-bound: sync vs async")
    print(f"Base URL: {base_url}")
    print(f"Requests: {total_requests}")
    print(f"Delay por request: {delay}s")
    print(f"Concurrencia async: {max_concurrency}")

    sync_result = fetch_sync(base_url=base_url, item_ids=item_ids, delay=delay)
    async_result = asyncio.run(
        fetch_async(
            base_url=base_url,
            item_ids=item_ids,
            delay=delay,
            max_concurrency=max_concurrency,
        )
    )

    print(f"\nSync elapsed:  {sync_result.elapsed_seconds:.4f}s")
    print(f"Async elapsed: {async_result.elapsed_seconds:.4f}s")

    if async_result.elapsed_seconds > 0:
        speedup = sync_result.elapsed_seconds / async_result.elapsed_seconds
        print(f"Speedup async vs sync: {speedup:.2f}x")


def benchmark_cpu_compare(limits: list[int], max_workers: int | None) -> None:
    print_header("Comparación CPU-bound: serial vs ProcessPoolExecutor")
    print(f"Inputs: {limits}")
    print(f"Workers: {max_workers}")

    serial_result = run_cpu_serial(limits)
    process_result = run_cpu_process_pool(limits, max_workers=max_workers)

    print(f"\nCPU serial elapsed:       {serial_result.elapsed_seconds:.4f}s")
    print(f"CPU process pool elapsed: {process_result.elapsed_seconds:.4f}s")

    if process_result.elapsed_seconds > 0:
        speedup = serial_result.elapsed_seconds / process_result.elapsed_seconds
        print(f"Speedup process pool vs serial: {speedup:.2f}x")


def run_timeit_examples(base_url: str) -> None:
    print_header("timeit: ejemplos rápidos")

    sync_times = repeat(
        stmt="fetch_sync(base_url=base_url, item_ids=[1, 2, 3], delay=0.2)",
        setup="from app.fetchers import fetch_sync",
        globals={"base_url": base_url},
        repeat=3,
        number=1,
    )

    async_times = repeat(
        stmt=(
            "asyncio.run(fetch_async("
            "base_url=base_url, item_ids=[1, 2, 3], delay=0.2, max_concurrency=3))"
        ),
        setup="import asyncio\nfrom app.fetchers import fetch_async",
        globals={"base_url": base_url},
        repeat=3,
        number=1,
    )

    print(f"Sync timeit runs:  {sync_times}")
    print(f"Async timeit runs: {async_times}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmarks de concurrencia")

    parser.add_argument(
        "--mode",
        choices=["fetch", "cpu", "timeit", "all"],
        default="all",
        help="Qué benchmark ejecutar",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help="URL base del servidor mock",
    )
    parser.add_argument(
        "--requests",
        type=int,
        default=10,
        help="Número de requests para benchmark de fetch",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.30,
        help="Delay artificial por request en el mock server",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=5,
        help="Máximo de concurrencia para el fetch async",
    )
    parser.add_argument(
        "--cpu-inputs",
        type=int,
        nargs="+",
        default=[30_000, 31_000, 32_000, 33_000],
        help="Entradas para benchmark CPU-bound",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=None,
        help="Número de procesos para ProcessPoolExecutor",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.mode in {"fetch", "all"}:
        benchmark_fetch_compare(
            base_url=args.base_url,
            total_requests=args.requests,
            delay=args.delay,
            max_concurrency=args.max_concurrency,
        )

    if args.mode in {"cpu", "all"}:
        benchmark_cpu_compare(
            limits=args.cpu_inputs,
            max_workers=args.max_workers,
        )

    if args.mode in {"timeit", "all"}:
        run_timeit_examples(base_url=args.base_url)


if __name__ == "__main__":
    main()
