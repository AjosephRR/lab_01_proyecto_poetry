# Lab: CLI y automatización para Orders

## Historia
Se construyó un CLI con Typer para gestionar orders consumiendo una API empaquetada. El laboratorio permite mostrar configuración, crear, listar y borrar órdenes desde terminal.

## Qué incluye
- CLI con Typer
- consumo de API con httpx
- configuración por variables de entorno
- payload JSON de ejemplo
- pruebas del CLI con pytest
- integración con la API empaquetada del laboratorio anterior

## Comandos principales para ejecutar pruebas o correr el laboratorio

### Configurar variables de entorno
```powershell
$env:PYTHONPATH = (Resolve-Path .\src).Path
$env:ORDERS_API_BASE_URL = "http://127.0.0.1:8000"
$env:ORDERS_API_TIMEOUT = "10"