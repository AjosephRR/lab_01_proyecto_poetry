# Lab 02 - Empaquetado, Docker y CI/CD

## Historia
Empaquetar una API FastAPI como wheel, contenerizarla con Docker multistage y automatizar un pipeline de CI que ejecute validaciones, construya artefactos y publique una imagen a GHCR.

## Qué incluye
- Proyecto Python empaquetable con Poetry
- API FastAPI mínima
- Generación de wheel
- Dockerfile multistage
- Workflow de GitHub Actions
- Publicación de artifact `.whl`
- Push de imagen Docker a GHCR

## Comandos principales para ejecutar pruebas o correr el laboratorio
```powershell
cd .\avanzado\02-empaquetado-distribucion-cicd\lab_orders_packaging_cicd
poetry install
poetry run pytest -q
poetry build -f wheel
docker build -t orders-packaged-api:local .
docker run --rm -p 8000:8000 orders-packaged-api:local