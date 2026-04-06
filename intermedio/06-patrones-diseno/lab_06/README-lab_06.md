# Lab 06 - Patrones de diseño

## Historia
Como sistema de catálogo y precios, quiero obtener productos desde un proveedor externo, adaptar su formato al modelo interno y calcular el precio final con distintas estrategias de descuento, para mantener una solución flexible, desacoplada y fácil de probar.

## Qué incluye
- Strategy para precios
- Decorator para caché
- Adapter para proveedor externo
- dataclasses
- pruebas con pytest

## Ejecutar ejemplo principal
```bash
$env:PYTHONPATH = (Resolve-Path ".\intermedio\06-patrones-diseno\lab_06\src")
poetry run python -m lab_patterns.main