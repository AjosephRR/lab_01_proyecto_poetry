
---

## `notas.md`

```md
# Notas del laboratorio

## Módulo
Seguridad y mantenimiento

## Objetivo técnico
Implementar una aplicación Python con configuración segura, separando secretos del código, validando variables de entorno con `pydantic-settings` y dejando la base lista para auditoría de dependencias y endurecimiento del runtime.

## Estructura del laboratorio
- `src/secure_app/settings.py`: configuración central de la aplicación
- `src/secure_app/main.py`: endpoints mínimos de FastAPI
- `tests/test_settings.py`: validación de lectura de variables de entorno y errores por secretos faltantes
- `tests/test_main.py`: validación de endpoints y protección de secretos en respuestas
- `.env.example`: ejemplo de variables requeridas
- `.gitignore`: exclusión de entorno, cachés y archivos sensibles
- `.dockerignore`: exclusión de archivos innecesarios para build de contenedor

## Componentes principales
- `BaseSettings` de `pydantic-settings`
- `SecretStr` para datos sensibles
- `FastAPI`
- `pytest`
- configuración con `.env`
- soporte previsto para `/run/secrets` en contenedor

## Casos cubiertos con pruebas
- Lectura correcta de `APP_API_KEY` y `APP_DATABASE_URL`
- Lectura de listas desde variables de entorno
- Error cuando faltan secretos obligatorios
- Endpoint `/health` funcionando correctamente
- Endpoint `/config-check` sin exponer valores sensibles reales

## Problemas corregidos durante el laboratorio
- Corrección de estructura del laboratorio y ubicación de archivos
- Ajuste del `pyproject.toml` para que Poetry reconociera nombre y versión del proyecto
- Regeneración de `poetry.lock` al detectar desincronización con `pyproject.toml`
- Resolución de fallo de Poetry al conectarse a PyPI usando caché local del proyecto
- Validación correcta del entorno virtual y ejecución de pruebas

## Resultado final
El laboratorio quedó funcional, con instalación correcta mediante Poetry, cuatro pruebas aprobadas y configuración segura desacoplada del código fuente. La aplicación ya está lista para continuar con validaciones de lint, tipado, auditoría de dependencias y pruebas en contenedor.

## Aprendizaje técnico
Aprendí a estructurar un laboratorio autónomo con Poetry, a usar `pydantic-settings` para centralizar configuración sensible, a detectar diferencias entre errores de red reales y problemas de caché/configuración en Poetry, y a validar que un warning de `/run/secrets` en Windows no implica un fallo funcional del proyecto.