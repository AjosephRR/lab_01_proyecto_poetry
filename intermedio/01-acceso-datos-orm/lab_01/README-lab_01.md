# Lab 01 - Acceso a datos y ORM

## Objetivo
Modelar entidades User, Order y OrderItem usando SQLAlchemy ORM, realizar operaciones CRUD básicas, manejar migraciones con Alembic y probar la lógica con SQLite en memoria.

## Tecnologías usadas
- Python
- Poetry
- SQLAlchemy
- Alembic
- SQLite
- Pytest

## Estructura
- `app/db.py`: configuración de base de datos y sesión
- `app/models.py`: modelos ORM
- `app/crud.py`: operaciones CRUD
- `app/main.py`: ejecución de prueba manual
- `tests/test_crud.py`: pruebas automáticas
- `migrations/`: migraciones con Alembic

## Entidades
- User
- Order
- OrderItem

## Relaciones
- Un User tiene muchas Orders
- Una Order tiene muchos OrderItems

## Cómo ejecutar
1. Entrar a `intermedio/01-acceso-datos-orm/lab_01`
2. Ejecutar `poetry run alembic upgrade head`
3. Ejecutar `poetry run python -m app.main`

## Cómo probar
- `poetry run pytest tests -v`

## Aprendizajes clave
- Modelado ORM
- Relaciones entre entidades
- Sesiones y transacciones
- Migraciones versionadas
- Pruebas con SQLite en memoria