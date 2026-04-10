
# notas.md

```md
# Notas del laboratorio

## Módulo
Empaquetado, distribución y CI/CD

## Objetivo técnico
Empaquetar una API Python como wheel, construir una imagen Docker multistage y dejar preparado un flujo profesional de validación para calidad, pruebas y build de artefactos reproducibles.

## Estructura del laboratorio
- `src/orders_packaged_api`: código fuente de la API
- `tests`: pruebas del servicio
- `pyproject.toml`: metadatos, dependencias y configuración del paquete
- `Dockerfile`: construcción multistage
- `.dockerignore`: exclusiones para build de Docker
- `dist/`: wheel generado

## Componentes principales
- Poetry para empaquetado
- FastAPI como servicio web
- Pydantic para esquemas
- Pytest para pruebas
- Black, isort y Ruff para calidad
- mypy para validación de tipos
- Wheel como artefacto reproducible
- Docker multistage para runtime limpio

## Casos cubiertos con pruebas
- endpoint `/health`
- creación de orden
- cálculo correcto del total
- ejecución de la API dentro del contenedor

## Problemas corregidos durante el laboratorio
- ajuste del nombre del archivo `README.md` para que Poetry pudiera construir el wheel
- error de permisos en la caché global de Poetry en Windows
- uso de `POETRY_CACHE_DIR` local para evitar bloqueo por caché
- configuración inicial de Docker Desktop y actualización de WSL
- validación del contenedor una vez resuelto el entorno Docker

## Resultado final
Se obtuvo un wheel instalable, una imagen Docker funcional y una API FastAPI ejecutándose correctamente dentro del contenedor en el puerto 8000.

## Aprendizaje técnico
Este laboratorio ayuda a entender cómo pasar de una aplicación local a un entregable reproducible, cómo construir una imagen Docker multistage, cómo resolver problemas reales de entorno en Windows con Poetry y cómo dejar una base lista para CI/CD.