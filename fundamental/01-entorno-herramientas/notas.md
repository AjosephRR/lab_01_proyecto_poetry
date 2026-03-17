## Temas vistos
- Instalación y configuración de Python
- Uso de Poetry para gestión de dependencias y entorno
- Estructura base de un proyecto Python
- Archivo `pyproject.toml`
- Archivo `poetry.lock`
- Organización con `src/` y `tests/`
- Configuración de herramientas de calidad:
  - Black
  - isort
  - Ruff
  - pre-commit
- Uso básico de Git y GitHub para seguimiento del proyecto

## Aprendizajes
- Poetry ayuda a crear y administrar proyectos Python de forma ordenada.
- `pyproject.toml` centraliza la configuración principal del proyecto y sus dependencias.
- `poetry.lock` permite mantener versiones consistentes de las librerías instaladas.
- Separar el código fuente en `src/` y las pruebas en `tests/` mejora la organización.
- Black formatea el código automáticamente para mantener consistencia.
- isort ayuda a ordenar los imports de forma limpia.
- Ruff funciona como linter y formateador rápido para detectar problemas de estilo y calidad.
- pre-commit permite ejecutar validaciones automáticas antes de hacer un commit.
- Git ayuda a llevar control de cambios y GitHub permite respaldar y compartir el proyecto.

## Relación con el laboratorio
En este módulo se creó y configuró un proyecto base con Poetry, dejando lista una estructura profesional para trabajar los siguientes módulos.

El laboratorio incluyó:
- creación del proyecto,
- configuración del entorno,
- instalación de herramientas de calidad,
- validación del formato del código,
- y preparación del repositorio para trabajar con Git y GitHub.

## Problemas encontrados
- Hubo ajustes en la reorganización del repositorio para pasar de una estructura inicial simple a una estructura por módulos y niveles dentro de `python-onboarding`.
- Se presentó confusión inicial entre la raíz del repositorio y la carpeta del laboratorio, lo cual se corrigió al dejar `python-onboarding` como raíz principal.
- También se revisó la ubicación correcta de archivos como `.gitignore` y `.pre-commit-config.yaml`, que debían permanecer en la raíz del repositorio.

## Evidencia
- Laboratorio completado en `lab_01_proyecto_poetry/`
- Proyecto organizado dentro de:
  `fundamental/01-entorno-herramientas/lab_01_proyecto_poetry/`