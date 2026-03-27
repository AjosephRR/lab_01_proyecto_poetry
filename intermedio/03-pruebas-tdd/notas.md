# Notas del laboratorio 

## Módulo
Pruebas y TDD

## Objetivo técnico

Este laboratorio fue diseñado para practicar:

- pruebas unitarias con `pytest`
- uso de `fixtures`
- parametrización
- markers
- mocking con `unittest.mock`
- property-based testing con `Hypothesis`
- cobertura con `pytest-cov`
- flujo de trabajo con TDD

---

## Estructura del laboratorio

```text
lab_03/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── pricing.py
│   ├── notifications.py
│   └── service.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_pricing.py
│   ├── test_service.py
│   └── test_properties.py
├── README.md
└── notas.md