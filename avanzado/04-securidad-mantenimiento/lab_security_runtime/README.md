# Lab: Seguridad y mantenimiento

## Historia
Este laboratorio implementa una API mínima en FastAPI con configuración segura usando `pydantic-settings`. El objetivo es separar secretos del código, validar la carga de configuración desde variables de entorno y preparar la aplicación para ejecutarse de forma más segura tanto en entorno local como en contenedor.

## Qué incluye
- Configuración centralizada con `pydantic-settings`
- Manejo de secretos con `SecretStr`
- Archivo `.env.example` como base de configuración local
- Endpoints de prueba para validar estado y configuración
- Pruebas unitarias para settings y endpoints
- Estructura preparada para auditoría de dependencias
- Base para contenedor Docker con enfoque de hardening

## Comandos principales para ejecutar pruebas o correr el laboratorio

```bash
poetry install
Copy-Item .\.env.example .\.env -Force
poetry run pytest -v
poetry run uvicorn secure_app.main:app --reload