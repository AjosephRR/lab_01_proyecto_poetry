# Lab 05 - Tipado estático opcional y calidad

## Objetivo
Este laboratorio practica el uso de tipado estático opcional y herramientas de calidad en Python.

Se enfoca en:
- anotar tipos en funciones y entidades,
- aplicar `Literal`, `TypedDict` y `Protocol`,
- validar el código con `mypy`,
- revisar calidad con `ruff`,
- y preparar validaciones automáticas con `pre-commit`.

## Temas aplicados
- Type hints
- `Literal`
- `TypedDict`
- `Protocol`
- `Union` con sintaxis moderna (`|`)
- `mypy`
- `ruff`
- `black`
- `isort`
- `pre-commit`

## Estructura del laboratorio
- `src/main.py`: script principal del laboratorio
- `README-lab_05.md`: descripción del laboratorio

## Qué hace el programa
El programa construye una orden tipada a partir de un diccionario de entrada y demuestra cómo aplicar tipado estático en un caso real.

Incluye:
1. un `TypedDict` para representar la estructura de entrada,
2. un `Literal` para restringir el estado de la orden,
3. un `Protocol` para trabajar por comportamiento,
4. funciones anotadas con tipos,
5. una entidad con datos derivados como subtotal y total.
