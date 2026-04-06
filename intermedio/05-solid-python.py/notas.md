# Notas - Lab 04: Concurrencia y rendimiento

## Objetivo del laboratorio
Comparar distintos modelos de concurrencia en Python para entender cuándo conviene usar ejecución síncrona, `asyncio` y `ProcessPoolExecutor`, además de medir tiempos con `timeit` y `cProfile`.

---

## Componentes implementados

### 1. `server_mock.py`
Se creó un servidor mock con FastAPI para simular una API local con retraso artificial.

Endpoints:
- `GET /health`
- `GET /items/{item_id}?delay=0.3`

Este servidor sirve para probar el caso I/O-bound sin depender de Internet.

---

### 2. `fetchers.py`
Se implementaron dos versiones de fetch:

#### `fetch_sync(...)`
- Usa `httpx.Client`
- Hace requests de forma secuencial
- Es útil como línea base de comparación

#### `fetch_async(...)`
- Usa `httpx.AsyncClient`
- Usa `asyncio.gather(...)`
- Usa `asyncio.Semaphore(...)` para limitar concurrencia
- Es la implementación principal para demostrar mejora en tareas I/O-bound

---

### 3. `cpu_bound.py`
Se implementó una función CPU-bound para contar números primos.

Funciones:
- `count_primes(limit)`
- `run_cpu_serial(limits)`
- `run_cpu_process_pool(limits, max_workers=None)`

Esto permite comparar ejecución serial contra `ProcessPoolExecutor`.

---

### 4. `benchmarks.py`
Se creó el orquestador principal de benchmarks.

Incluye:
- comparación sync vs async
- comparación CPU serial vs process pool
- ejemplos con `timeit`
- soporte para `cProfile`

---

## Conceptos clave aprendidos

### GIL
El GIL en CPython limita la ejecución simultánea de bytecode Python dentro de un mismo proceso.

### Implicación práctica
- Para tareas **I/O-bound**, `asyncio` o threads ayudan mucho porque gran parte del tiempo se pasa esperando.
- Para tareas **CPU-bound**, threads no suelen escalar bien por el GIL.
- Para tareas **CPU-bound**, conviene usar procesos (`ProcessPoolExecutor` o `multiprocessing`).

---

## Resultado obtenido en la comparación I/O-bound

Ejecución real observada:

- Sync elapsed: `3.8375s`
- Async elapsed: `1.1367s`
- Speedup async vs sync: `3.38x`

### Interpretación
La versión asíncrona sí mejoró claramente frente a la síncrona porque el problema era de espera de red simulada, no de cálculo pesado.

Esto confirma que `asyncio` es una buena opción cuando la carga es I/O-bound.

---

## Resultado obtenido en la comparación CPU-bound

Ejecución real observada:

- CPU serial elapsed: `0.1225s`
- CPU process pool elapsed: `0.3773s`
- Speedup process pool vs serial: `0.32x`

### Interpretación
En esta corrida, `ProcessPoolExecutor` fue más lento que la ejecución serial.

Esto no significa que esté mal implementado. Significa que:
- la carga usada fue pequeña
- el costo de crear procesos y coordinar resultados fue mayor que el beneficio

### Conclusión
El process pool no siempre gana. Su ventaja aparece más cuando la tarea CPU-bound es suficientemente pesada.

---

## Resultado de `timeit`

Ejecución real observada:

- Sync timeit runs:
  - `1.0793`
  - `1.1041`
  - `1.0867`

- Async timeit runs:
  - `0.7224`
  - `0.7338`
  - `0.7168`

### Interpretación
`timeit` confirmó la misma tendencia:
- la versión sync tarda más
- la versión async tarda menos

---

## Error importante encontrado
Al principio apareció este error:

`httpx.ConnectError: [WinError 10061] No se puede establecer una conexión...`

### Causa
Se intentó correr `benchmarks.py` sin levantar antes el servidor mock en `127.0.0.1:8001`.

### Solución
Levantar primero el servidor con:

```bash
poetry run uvicorn app.server_mock:app --reload --port 8001