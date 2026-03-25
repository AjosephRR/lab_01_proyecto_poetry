# Lab 02 - APIs web con FastAPI

## Objetivo
Construir una API web con FastAPI que exponga un CRUD de órdenes, con validación de datos, autenticación JWT básica, middleware, CORS y pruebas de integración con una base temporal.

## Tecnologías usadas
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- PyJWT
- pwdlib
- pytest
- httpx
- SQLite

## Estructura
- `app/main.py`: instancia principal de la API
- `app/db.py`: configuración de base de datos
- `app/models.py`: modelos ORM
- `app/schemas.py`: esquemas Pydantic
- `app/security.py`: hashing y JWT
- `app/deps.py`: dependencias reutilizables
- `app/routers/auth.py`: endpoints de autenticación
- `app/routers/orders.py`: CRUD de órdenes
- `tests/`: pruebas de integración

## Endpoints principales
- `POST /auth/register`
- `POST /auth/login`
- `POST /orders/`
- `GET /orders/`
- `GET /orders/{order_id}`
- `PUT /orders/{order_id}`
- `DELETE /orders/{order_id}`

## Documentación automática
- `/docs`
- `/redoc`

## Cómo ejecutar
1. Entrar a `intermedio/02-apis-web-fastapi/lab_02`
2. Ejecutar `poetry run uvicorn app.main:app --reload`
3. Llamar `POST /setup`
4. Usar `/docs`

## Cómo correr pruebas
- `poetry run pytest tests -v`

## Aprendizajes clave
- routers
- dependencias
- validación con Pydantic
- autenticación JWT
- middleware y CORS
- pruebas de integración con DB temporal