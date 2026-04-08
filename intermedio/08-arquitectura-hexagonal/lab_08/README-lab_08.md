# Lab 08 - Arquitectura Hexagonal

## Historia
Como sistema de órdenes, quiero crear una orden mediante un caso de uso desacoplado de la infraestructura, para poder guardar la información con distintos adaptadores y notificar la creación sin afectar la lógica de negocio.

## Qué incluye
- arquitectura hexagonal
- capas: dominio, aplicación e infraestructura
- puertos con `Protocol`
- adaptadores en memoria y SQLAlchemy
- adaptador de notificación HTTP simulado
- FastAPI con wiring de dependencias
- pruebas de dominio, contrato y end-to-end

## Ejecutar pruebas
```bash
$env:PYTHONPATH = (Resolve-Path ".\intermedio\08-arquitectura-hexagonal\lab_08")
poetry run python -m pytest .\intermedio\08-arquitectura-hexagonal\lab_08\tests -v