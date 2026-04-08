# Notas del laboratorio

## Módulo
Arquitectura Hexagonal (Puertos y Adaptadores)

## Objetivo técnico

Este laboratorio fue diseñado para practicar:

- separación por capas: dominio, aplicación e infraestructura
- definición de puertos con `Protocol`
- creación de adaptadores intercambiables
- implementación de un caso de uso `CreateOrder`
- uso de DTOs para entrada y salida
- inyección de dependencias y wiring con FastAPI
- repositorio en memoria y repositorio con SQLAlchemy
- adaptador de notificación HTTP simulado
- pruebas de dominio, contrato y end-to-end con `pytest`

---

## Estructura del laboratorio

```text
lab_08/
├── README.md
├── notas.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities.py
│   │   └── ports.py
│   ├── application/
│   │   ├── __init__.py
│   │   ├── dto.py
│   │   └── use_cases.py
│   └── infrastructure/
│       ├── __init__.py
│       ├── notifications/
│       │   ├── __init__.py
│       │   └── http_notification.py
│       └── persistence/
│           ├── __init__.py
│           ├── db.py
│           ├── memory_repository.py
│           ├── sqlalchemy_models.py
│           └── sqlalchemy_repository.py
└── tests/
    ├── __init__.py
    ├── test_contract_repository.py
    ├── test_domain_order.py
    ├── test_e2e_api.py
    └── test_use_case_create_order.pys