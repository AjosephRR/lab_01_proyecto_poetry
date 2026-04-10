# Notas del laboratorio

## Módulo
CLI y automatización

## Objetivo técnico
Construir un CLI mantenible con Typer para gestionar orders consumiendo una API, usando variables de entorno para configuración y comandos ejecutables desde terminal.

## Estructura del laboratorio
- `src/lab_orders_cli/config.py`: carga de configuración
- `src/lab_orders_cli/client.py`: cliente HTTP hacia la API
- `src/lab_orders_cli/render.py`: salida formateada en terminal
- `src/lab_orders_cli/main.py`: comandos del CLI
- `payloads/order_demo.json`: payload de ejemplo
- `tests/test_cli.py`: pruebas del CLI
- `src/orders_packaged_api/main.py` del lab anterior: API actualizada con list y delete

## Componentes principales
- Typer para comandos CLI
- httpx para consumo de API
- variables de entorno para URL y timeout
- FastAPI para el backend de orders
- almacenamiento en memoria para listar y borrar órdenes

## Casos cubiertos con pruebas
- mostrar configuración
- crear order
- listar orders
- borrar order
- manejo de JSON inválido

## Problemas corregidos durante el laboratorio
- Poetry no completaba la instalación por fallo de red con PyPI
- el payload inicial no incluía `order_id`
- la API solo exponía `POST /orders`
- se agregaron `GET /orders` y `DELETE /orders/{order_id}`
- se implementó almacenamiento en memoria para soportar list y delete

## Resultado final
Se obtuvo un CLI funcional que puede crear, listar y borrar orders consumiendo la API empaquetada del laboratorio anterior.

## Aprendizaje técnico
Este laboratorio permitió practicar integración CLI + API, manejo de errores HTTP, configuración por variables de entorno y validación completa del flujo create/list/delete.