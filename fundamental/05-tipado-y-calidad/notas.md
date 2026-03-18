## Temas vistos
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
- validación de calidad centralizada desde la raíz del repositorio

## Aprendizajes
- Los type hints ayudan a que el código sea más claro y fácil de mantener.
- `Literal` permite restringir ciertos valores a opciones concretas.
- `TypedDict` sirve para tipar diccionarios de entrada sin convertirlos todavía en clases.
- `Protocol` permite trabajar con objetos que comparten comportamiento, aunque no hereden entre sí.
- `mypy` ayuda a detectar errores de tipos antes de ejecutar el programa.
- `ruff`, `black` e `isort` ayudan a mantener orden y consistencia en el código.
- `pre-commit` automatiza validaciones antes de hacer commit.
- La calidad del proyecto ya no depende solo del lab 01, sino que ahora se puede aplicar a todo el repositorio `python-onboarding`.

## Relación con el laboratorio
En este laboratorio se:
- anotaron tipos en funciones, estructuras de entrada y entidades,
- usó `Literal` para el estado de la orden,
- usó `TypedDict` para la entrada,
- usó `Protocol` para aceptar cualquier objeto con un método `summary`,
- ejecutó validación estática con `mypy`,
- y se validó calidad con `ruff` y `pre-commit`.

## Problemas encontrados
- Inicialmente hubo confusión entre ejecutar `mypy` y ejecutar el programa con `python`.
- Se confirmó que `mypy` valida tipos, pero no ejecuta el código ni muestra los `print`.
- También se ajustó un detalle menor de formato en la cadena mostrada por `summary()`.

## Validación realizada
- Se ejecutó correctamente:
  `poetry run python main.py`
- Se validó tipado correctamente:
  `poetry run mypy main.py`
- Resultado de `mypy`:
  `Success: no issues found in 1 source file`

