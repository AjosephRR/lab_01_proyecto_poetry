# Notas del laboratorio

## Módulo
Patrones de diseño

## Objetivo técnico

Este laboratorio fue diseñado para practicar:

- patrón **Strategy** para reglas de precios
- patrón **Decorator** para agregar caché sin modificar la lógica base
- patrón **Adapter** para integrar un proveedor externo con formato distinto
- uso de `dataclasses` para representar el modelo de dominio
- separación de responsabilidades en módulos pequeños
- pruebas unitarias con `pytest`
- validación del comportamiento de estrategias, caché y adaptación de datos

---

## Estructura del laboratorio

```text
lab_06/
├── README.md
├── notas.md
├── src/
│   └── lab_patterns/
│       ├── __init__.py
│       ├── main.py
│       ├── domain/
│       │   ├── __init__.py
│       │   └── models.py
│       ├── pricing/
│       │   ├── __init__.py
│       │   ├── service.py
│       │   └── strategies.py
│       ├── providers/
│       │   ├── __init__.py
│       │   ├── adapter.py
│       │   └── external_provider.py
│       └── utils/
│           ├── __init__.py
│           └── cache.py
└── tests/
    ├── test_cache_decorator.py
    ├── test_provider_adapter.py
    └── test_pricing_strategy.py