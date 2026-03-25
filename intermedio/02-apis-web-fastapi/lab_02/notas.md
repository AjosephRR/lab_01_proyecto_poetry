# Notas del laboratorio

## Qué entendí
- FastAPI permite dividir una API en múltiples archivos usando routers.
- Depends sirve para inyectar dependencias como la sesión de base de datos y el usuario autenticado.
- Pydantic valida entradas y salidas de la API.
- JWT me permite autenticar endpoints protegidos.
- CORS se usa cuando un frontend y backend están en orígenes distintos.
- Middleware permite ejecutar lógica antes y después de cada request.
- Para probar FastAPI de forma limpia conviene usar pytest + httpx con ASGITransport.

## Qué hice en este laboratorio
- Registro y login básico con JWT
- CRUD de órdenes protegido
- Validaciones con Pydantic
- Middleware para header de tiempo
- CORS para localhost
- Tests de integración con DB temporal

## Sintaxis importante
- `@router.post(...)`: decorador que registra un endpoint POST
- `Depends(...)`: inyección de dependencias
- `Annotated[...]`: mezcla tipo + metadata
- `Field(...)`: reglas de validación
- `Literal[...]`: conjunto fijo de valores válidos
- `yield`: presta un recurso temporalmente
- `| None`: tipo opcional
- `f""`: inserta variables dentro de cadenas
- `response_model=...`: define y valida la respuesta

## Lo que más debo poder explicar
- por qué separar auth y orders en routers
- por qué get_db usa yield
- por qué el login usa form-data y no JSON
- por qué en tests se sobreescribe get_db
- por qué usar httpx es más natural que aiohttp en FastAPI