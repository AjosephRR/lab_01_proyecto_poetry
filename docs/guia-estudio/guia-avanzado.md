# Guia de Estudio del Modulo Avanzado

## 1. Que busca este modulo

El modulo `avanzado` se enfoca en pensar como ingeniero de software. Aqui la pregunta ya no es solo "como programo esto", sino:

- como lo organizo mejor
- como lo distribuyo
- como lo automatizo
- como lo protejo
- como lo mantengo en el tiempo

En este modulo aparecen temas muy cercanos a un entorno profesional real.

## 2. Contenido explicito del modulo

### 01. Arquitectura limpia

Carpeta: `avanzado/01-arquitectura-limpia`

Aqui se estudia:

- dominio
- entidades
- casos de uso
- interfaces
- infraestructura
- eventos de dominio
- Unit of Work
- presenter

Ejemplos reales del proyecto:

En `avanzado/01-arquitectura-limpia/lab_orders_clean_architecture/src/orders_clean_architecture/domain/entities.py`:

- `OrderItem` valida reglas desde el dominio
- `Order.create(...)` valida datos y genera un evento `OrderCreated`
- `pull_events()` permite extraer eventos acumulados

En `avanzado/01-arquitectura-limpia/lab_orders_clean_architecture/src/orders_clean_architecture/application/use_cases/create_order.py`:

- el caso de uso crea la orden
- usa `UnitOfWork`
- publica eventos
- devuelve la salida usando un presenter

En `avanzado/01-arquitectura-limpia/lab_orders_clean_architecture/src/orders_clean_architecture/interfaces/http/controllers.py`:

- FastAPI solo recibe la peticion y delega al caso de uso

Forma simple de explicarlo:

"La arquitectura limpia separa el corazon del negocio de los detalles externos. Asi el sistema es mas facil de probar, cambiar y mantener."

### 02. Empaquetado, distribucion y CI/CD

Carpeta: `avanzado/02-empaquetado-distribucion-cicd`

Aqui se aprende:

- como empaquetar una aplicacion
- como construir una wheel
- como preparar Docker
- como automatizar calidad y build con CI/CD

Ejemplo real del proyecto:

En `avanzado/02-empaquetado-distribucion-cicd/lab_orders_packaging_cicd/pyproject.toml` se define el paquete `orders-packaged-api`, sus dependencias y reglas de calidad.

En `avanzado/02-empaquetado-distribucion-cicd/lab_orders_packaging_cicd/src/orders_packaged_api/main.py`:

- hay un `FastAPI` minimo
- existe un endpoint `/health`
- existe `POST /orders`
- luego se agregan `GET /orders` y `DELETE /orders/{order_id}`

En `workflows/orders-packaging-ci.yml` se ve la intencion de automatizar:

- `isort`
- `black`
- `ruff`
- `mypy`
- `pytest`
- build de wheel
- build y push de imagen Docker

Forma simple de explicarlo:

"Empaquetar significa preparar el proyecto para distribuirlo. CI/CD significa automatizar revisiones y construcciones para no depender siempre de pasos manuales."

### 03. CLI y automatizacion

Carpeta del lab: `avanzado/03-cli-automatizacion/lab_orders_cli`

Codigo principal actual: `src/lab_orders_cli`

Aqui se estudia:

- CLI con Typer
- configuracion por variables de entorno
- consumo de API
- automatizacion desde terminal
- manejo claro de errores para usuario final

Ejemplo real del proyecto:

En `src/lab_orders_cli/main.py`:

- `config` muestra configuracion
- `list` consulta ordenes
- `create` lee un archivo JSON y crea una orden
- `delete` borra una orden

En `src/lab_orders_cli/client.py`:

- `OrdersApiClient` encapsula llamadas HTTP
- `ApiError` da mensajes mas entendibles

En `src/lab_orders_cli/config.py`:

- la configuracion sale de `ORDERS_API_BASE_URL`
- el timeout sale de `ORDERS_API_TIMEOUT`

Forma simple de explicarlo:

"Un CLI permite usar una aplicacion desde terminal. Es util para automatizar tareas, integrar scripts o dar una herramienta practica al usuario."

### 04. Seguridad y mantenimiento

Carpeta: `avanzado/04-securidad-mantenimiento`

Aqui se trabaja con:

- configuracion centralizada
- secretos
- variables de entorno
- validacion de configuracion
- base para auditoria de dependencias
- preparacion para contenedor

Ejemplo real del proyecto:

En `avanzado/04-securidad-mantenimiento/lab_security_runtime/src/secure_app/settings.py`:

- `Settings` hereda de `BaseSettings`
- `api_key` y `database_url` se manejan como `SecretStr`
- `safe_dict()` devuelve una vista segura de la configuracion

En `avanzado/04-securidad-mantenimiento/lab_security_runtime/src/secure_app/main.py`:

- `/health` devuelve estado y entorno
- `/config-check` usa la configuracion validada

En `avanzado/04-securidad-mantenimiento/lab_security_runtime/tests/test_settings.py`:

- se prueba lectura desde variables de entorno
- se valida que falten secretos obligatorios y eso falle correctamente

Forma simple de explicarlo:

"La seguridad empieza desde la configuracion. No conviene dejar secretos escritos en el codigo ni asumir que todo el entorno esta bien configurado."

## 3. Conceptos y terminologia clave

- `arquitectura limpia`: organizacion que separa el dominio del resto del sistema
- `dominio`: reglas y conceptos principales del negocio
- `caso de uso`: accion que resuelve una necesidad del negocio
- `infraestructura`: detalles tecnicos como base de datos, HTTP o archivos
- `interface`: contrato que define como se comunica una parte con otra
- `evento de dominio`: hecho importante que ocurre dentro del negocio
- `Unit of Work`: patron para agrupar cambios en una transaccion
- `presenter`: componente que prepara la salida para otra capa
- `paquete`: proyecto preparado para distribuirse e instalarse
- `wheel`: formato comun de distribucion en Python
- `CI`: integracion continua
- `CD`: entrega o despliegue continuo
- `pipeline`: secuencia automatizada de pasos
- `CLI`: interfaz de linea de comandos
- `variable de entorno`: valor de configuracion definido fuera del codigo
- `secreto`: dato sensible como token, password o API key
- `hardening`: acciones para hacer mas segura una aplicacion o contenedor

## 4. Como explicarlo en una exposicion

Puedes usar esta idea:

"En el modulo avanzado aprendo practicas profesionales de ingenieria. Ya no solo me enfoco en que el sistema funcione, sino en que tenga una arquitectura clara, pueda empaquetarse, automatizarse, usarse desde terminal y configurarse de forma segura."

## 5. Relacion entre los laboratorios del modulo avanzado

Este modulo tiene una secuencia logica:

1. Primero organizas mejor el sistema con arquitectura limpia.
2. Despues preparas una API para distribuirla y automatizar su calidad.
3. Luego construyes un CLI que consume esa API.
4. Finalmente trabajas seguridad y mantenimiento para que el sistema sea mas robusto.

Dicho simple:

"Primero ordeno el software, luego lo preparo para distribuirlo, despues creo herramientas para usarlo, y al final lo hago mas seguro."

## 6. Ejemplos reales que puedes mencionar

- Entidad de dominio con validaciones en `avanzado/01-arquitectura-limpia/lab_orders_clean_architecture/src/orders_clean_architecture/domain/entities.py`
- Bus de eventos en `avanzado/01-arquitectura-limpia/lab_orders_clean_architecture/src/orders_clean_architecture/application/event_bus.py`
- Caso de uso principal en `avanzado/01-arquitectura-limpia/lab_orders_clean_architecture/src/orders_clean_architecture/application/use_cases/create_order.py`
- API empaquetada en `avanzado/02-empaquetado-distribucion-cicd/lab_orders_packaging_cicd/src/orders_packaged_api/main.py`
- CLI para consumir la API en `src/lab_orders_cli/main.py`
- Configuracion segura en `avanzado/04-securidad-mantenimiento/lab_security_runtime/src/secure_app/settings.py`

## 7. Que deberias poder explicar despues de estudiar este modulo

Despues de este modulo deberias poder explicar:

- por que conviene separar dominio, aplicacion e infraestructura
- para que sirve un pipeline automatizado
- que beneficio tiene un CLI sobre hacer llamadas manuales
- por que la configuracion y los secretos no deben ir hardcodeados
- por que mantener software implica mas que escribir funcionalidades nuevas

## 8. Resumen corto para memorizar

`avanzado` ensena a trabajar con arquitectura, empaquetado, automatizacion, CLI, seguridad y mantenimiento para acercarse a un entorno profesional real.
