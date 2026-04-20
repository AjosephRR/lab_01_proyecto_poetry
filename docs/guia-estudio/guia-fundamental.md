# Guia de Estudio del Modulo Fundamental

## 1. Que busca este modulo

El modulo `fundamental` construye la base del curso. Aqui aprendes a trabajar con Python como lenguaje, a preparar tu entorno de desarrollo y a resolver problemas pequenos con codigo claro.

La meta no es solo "hacer que funcione", sino entender:

- como se escribe Python
- como se organizan los datos
- como se usan funciones y clases
- como se leen archivos
- como se consume una API

Si este modulo queda claro, los temas de `intermedio` y `avanzado` tienen mucho mas sentido.

## 2. Contenido explicito del modulo

Segun la estructura actual del proyecto, el modulo incluye estos bloques:

### 01. Entorno y herramientas

Carpeta: `fundamental/01-entorno-herramientas`

Aqui se trabaja con:

- Python 3.12
- Poetry
- VS Code
- `pyproject.toml`
- `black`
- `isort`
- `ruff`
- `pre-commit`

Idea sencilla para explicarlo:

"Antes de programar bien, necesito un entorno ordenado. Estas herramientas me ayudan a instalar dependencias, mantener formato consistente y detectar errores basicos."

Ejemplo real del proyecto:

En `pyproject.toml` se definen dependencias, configuracion de calidad y el script `orders-cli`.

### 02. Fundamentos del lenguaje

Carpeta: `fundamental/02-fundamentos-lenguaje`

Aqui aparecen conceptos como:

- variables
- funciones
- listas y diccionarios
- validaciones
- manejo de errores
- expresiones regulares
- `match/case`
- lectura de JSON

Ejemplo real del proyecto:

En `fundamental/02-fundamentos-lenguaje/lab_02/src/main.py` se ven varias ideas importantes:

- `validar_correo(correo: str) -> bool`: usa una expresion regular para revisar un correo
- `clasificar_edad(edad: int) -> str`: usa `match/case`
- `leer_usuarios(...)`: abre un archivo JSON y maneja errores
- `filtrar_activos(...)`: usa comprension de listas
- `agrupar_por_ciudad(...)`: construye un resumen con diccionarios

Forma simple de explicarlo:

"Este laboratorio ensena a leer datos, validarlos y transformarlos. Es el tipo de logica que aparece todo el tiempo en programas reales."

### 03. Funciones y estilo pythonic

Carpeta: `fundamental/03-funciones-pythonic`

Aqui se estudia:

- parametros posicionales y nombrados
- `*args`
- `**kwargs`
- closures
- decoradores
- generadores
- context managers

Ejemplo real del proyecto:

En `fundamental/03-funciones-pythonic/lab_03/src/main.py`:

- `sumar_todos(*args)` recibe muchos valores
- `mostrar_configuracion(**kwargs)` recibe configuracion flexible
- `crear_multiplicador(factor)` devuelve otra funcion
- `reintentos(...)` crea un decorador reutilizable
- `generar_lotes(...)` usa `yield`
- `temporizador(...)` usa `@contextmanager`

Forma simple de explicarlo:

"Python no solo permite escribir funciones; permite escribir funciones muy expresivas y reutilizables."

### 04. Objetos y modelos de datos

Carpeta: `fundamental/04-objetos-modelo-datos`

Aqui se aprende:

- que es una clase
- que es una instancia
- que es una entidad
- como usar `dataclass`
- como validar entradas con Pydantic
- como separar modelo de entrada, entidad y modelo de salida

Ejemplo real del proyecto:

En `fundamental/04-objetos-modelo-datos/lab_04/src/main.py`:

- `OrderItem` y `Order` representan datos del dominio
- `subtotal`, `total` y `total_items` son propiedades derivadas
- `OrderIn` valida datos de entrada
- `OrderOut` prepara datos de salida
- `to_entity(...)` y `to_output(...)` convierten entre modelos

Forma simple de explicarlo:

"Aqui ya no trabajo solo con variables sueltas. Empiezo a representar informacion del mundo real con objetos, por ejemplo una orden y sus productos."

### 05. Tipado y calidad

Carpeta: `fundamental/05-tipado-y-calidad`

Aqui se introduce:

- `Literal`
- `TypedDict`
- `Protocol`
- anotaciones de tipos
- validacion con herramientas como `mypy`

Ejemplo real del proyecto:

En `fundamental/05-tipado-y-calidad/lab_05/src/main.py`:

- `OrderStatus = Literal[...]` restringe valores posibles
- `OrderPayload` describe el formato esperado de un diccionario
- `SupportsSummary` muestra tipado por comportamiento
- `normalize_discount(...)` trabaja con `float | int | None`

Forma simple de explicarlo:

"El tipado no cambia lo que Python puede hacer, pero hace el codigo mas claro y ayuda a detectar errores antes de ejecutar."

### 06. Libreria estandar e IO

Carpeta: `fundamental/06-libreria-estandar-io`

Aqui se trabaja con:

- `csv`
- `json`
- `logging`
- `datetime`
- `zoneinfo`
- `collections`
- manejo de rutas con `pathlib`

Ejemplo real del proyecto:

En `fundamental/06-libreria-estandar-io/lab_06/src/main.py`:

- se lee `ventas.csv`
- se calculan metricas de negocio
- se usa `Counter` para detectar el producto mas vendido
- se usa `defaultdict` para agrupar por categoria
- se genera `reporte.json`

Forma simple de explicarlo:

"Este laboratorio ensena a tomar datos de un archivo, procesarlos y convertirlos en informacion util."

### 07. HTTP y APIs

Carpeta: `fundamental/07-http-y-apis`

Aqui se estudia:

- cliente HTTP
- timeout
- reintentos
- backoff
- descarga por streaming
- manejo de errores de red

Ejemplo real del proyecto:

En `fundamental/07-http-y-apis/lab_07/src/main.py`:

- `RetryConfig` guarda configuracion de reintentos
- `ApiClient` encapsula el acceso a una API
- `_request_with_retries(...)` vuelve a intentar cuando falla una llamada
- `download_streaming(...)` descarga un archivo en bloques

Forma simple de explicarlo:

"Una API no siempre responde bien. Por eso aqui se aprende a comunicarse con servicios externos de forma mas segura y controlada."

## 3. Conceptos y terminologia clave

Estos terminos conviene saber explicarlos con palabras simples:

- `entorno virtual`: espacio aislado donde se instalan dependencias del proyecto
- `dependencia`: libreria externa que el proyecto usa
- `funcion`: bloque de codigo reutilizable
- `parametro`: dato que una funcion recibe
- `retorno`: valor que una funcion devuelve
- `lista`: coleccion ordenada de elementos
- `diccionario`: coleccion de pares `clave: valor`
- `excepcion`: error que ocurre durante la ejecucion
- `dataclass`: forma simple de crear clases que representan datos
- `Pydantic`: libreria para validar datos
- `tipado`: forma de describir que tipo de dato se espera
- `JSON`: formato de texto usado para intercambiar datos
- `CSV`: formato tabular simple, comun en reportes
- `API`: interfaz para que un sistema hable con otro
- `HTTP`: protocolo usado para comunicarse en la web
- `retry`: reintento automatico ante un fallo
- `streaming`: lectura o descarga por partes, no de golpe

## 4. Como explicarlo en una exposicion

Puedes usar esta idea:

"El modulo fundamental me ensena a programar con Python desde la base. Primero preparo mi entorno, luego aprendo la sintaxis y la logica del lenguaje, despues uso funciones y objetos para organizar mejor el codigo, y finalmente trabajo con archivos y APIs. Es el modulo donde se forma la base tecnica para todo lo demas."

## 5. Ejemplos reales que puedes mencionar

- Lectura de usuarios desde JSON en `fundamental/02-fundamentos-lenguaje/lab_02/src/main.py`
- Decorador de reintentos en `fundamental/03-funciones-pythonic/lab_03/src/main.py`
- Modelo `Order` con `dataclass` en `fundamental/04-objetos-modelo-datos/lab_04/src/main.py`
- Tipado con `TypedDict` y `Protocol` en `fundamental/05-tipado-y-calidad/lab_05/src/main.py`
- Reporte de ventas desde CSV hacia JSON en `fundamental/06-libreria-estandar-io/lab_06/src/main.py`
- Cliente HTTP con reintentos en `fundamental/07-http-y-apis/lab_07/src/main.py`

## 6. Que deberias dominar antes de pasar al siguiente modulo

Antes de `intermedio`, deberias poder:

- leer y escribir funciones sin copiar ejemplos
- entender listas, diccionarios y ciclos
- crear clases simples
- leer archivos JSON o CSV
- entender que hace una API y como consumirla
- reconocer errores comunes y manejarlos

## 7. Resumen corto para memorizar

`fundamental` ensena el lenguaje, las herramientas y las bases para resolver problemas pequenos con Python de forma ordenada.
