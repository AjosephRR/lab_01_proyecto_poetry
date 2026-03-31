# Lab 04 - Concurrencia y rendimiento

## Objetivo
Comparar distintos modelos de concurrencia en Python:

- I/O-bound síncrono vs asíncrono
- CPU-bound serial vs ProcessPoolExecutor
- Medición con timeit y cProfile

## Estructura
- `server_mock.py`: API local con delay artificial
- `fetchers.py`: versión sync y async con semáforo
- `cpu_bound.py`: cálculo CPU-bound
- `benchmarks.py`: comparación de tiempos

## Ejecutar servidor mock
poetry run uvicorn app.server_mock:app --reload --port 8001