# Lab 01 - Orders con Arquitectura Limpia

## Historia
Reestructurar el módulo Orders a una arquitectura limpia, separando dominio, aplicación, infraestructura e interfaces. Se introduce Unit of Work para delimitar transacciones, un Presenter para desacoplar la salida del caso de uso y el evento de dominio `OrderCreated` manejado en la capa de aplicación.

## Qué incluye
- Entidades `Order` y `OrderItem`
- Evento de dominio `OrderCreated`
- Caso de uso `CreateOrderUseCase`
- `JsonCreateOrderPresenter`
- `AbstractUnitOfWork` e implementación en memoria
- Repositorio en memoria
- Controlador HTTP con FastAPI
- Pruebas de dominio, caso de uso y endpoint

## Comandos principales para ejecutar pruebas o correr el laboratorio
```powershell
$env:PYTHONPATH="$PWD\avanzado\01-arquitectura-limpia\lab_orders_clean_architecture\src"
poetry run pytest .\avanzado\01-arquitectura-limpia\lab_orders_clean_architecture\tests -q
poetry run uvicorn orders_clean_architecture.main:app --reload --app-dir .\avanzado\01-arquitectura-limpia\lab_orders_clean_architecture\src
poetry run mypy .\avanzado\01-arquitectura-limpia\lab_orders_clean_architecture\src
poetry run ruff check .\avanzado\01-arquitectura-limpia\lab_orders_clean_architecture