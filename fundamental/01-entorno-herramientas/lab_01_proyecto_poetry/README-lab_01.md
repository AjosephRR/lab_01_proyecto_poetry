# Módulo: Entorno y herramientas

## Objetivo
Configurar un entorno profesional de desarrollo en Python 3.12 utilizando Poetry, Visual Studio Code y herramientas de calidad de código.

## Contenidos trabajados
- Instalación de Python 3.12
- Gestión de entornos virtuales con Poetry
- Configuración de Visual Studio Code
- Estructura de proyecto con `pyproject.toml`
- Aplicación de PEP 8 y principios de PEP 20
- Automatización de validaciones con `black`, `isort`, `ruff` y `pre-commit`

## Herramientas instaladas
- Python 3.12
- Poetry
- Git
- VS Code
- black
- isort
- ruff
- pre-commit

## Estructura del proyecto
- `pyproject.toml`: configuración principal del proyecto y dependencias
- `.pre-commit-config.yaml`: hooks para validaciones automáticas
- `.gitignore`: exclusión de archivos temporales y del entorno
- `src/`: código fuente
- `tests/`: base para pruebas
- `README.md`: documentación del laboratorio

## Comandos utilizados
```powershell
poetry install
poetry run python --version
poetry run isort .
poetry run black .
poetry run ruff check .
poetry run pre-commit install
poetry run pre-commit run --all-files