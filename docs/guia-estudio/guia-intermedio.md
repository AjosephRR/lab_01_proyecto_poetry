# Guia de Estudio del Modulo Intermedio

## 1. Que busca este modulo

El modulo `intermedio` es el punto donde Python deja de ser solo un lenguaje de ejercicios y se convierte en una herramienta para crear aplicaciones mas completas.

Aqui ya no basta con escribir codigo que funcione. Tambien importa:

- como se organiza
- como se prueba
- como se conecta con una base de datos
- como se expone como API
- como se separa la logica de negocio de la infraestructura

## 2. Contenido explicito del modulo

El modulo `intermedio` contiene estos bloques:

### 01. Acceso a datos con ORM

Carpeta: `intermedio/01-acceso-datos-orm`

Aqui se aprende:

- que es un ORM
- como mapear tablas a clases
- como crear, leer, actualizar y borrar datos
- como trabajar con relaciones entre entidades

Ejemplo real del proyecto:

En `intermedio/01-acceso-datos-orm/lab_01/app/crud.py`:

- `create_user(...)` crea usuarios
- `create_order(...)` crea una orden y sus items
- `list_orders(...)` recupera ordenes con relaciones cargadas
- `update_order_status(...)` cambia el estado
- `delete_order(...)` elimina una orden

Forma simple de explicarlo:

"Un ORM me permite trabajar con objetos de Python sin escribir SQL manual para todo."

### 02. APIs web con FastAPI

Carpeta: `intermedio/02-apis-web-fastapi`

Aqui se trabaja con:

- rutas y endpoints
- modelos de entrada y salida
- autenticacion basica
- dependencias
- respuestas HTTP
- CRUD de ordenes

Ejemplo real del proyecto:

En `intermedio/02-apis-web-fastapi/lab_02/app/routers/orders.py`:

- `POST /orders/` crea una orden
- `GET /orders/` lista ordenes del usuario
- `GET /orders/{order_id}` obtiene una orden
- `PUT /orders/{order_id}` actualiza una orden
- `DELETE /orders/{order_id}` elimina una orden

Forma simple de explicarlo:

"FastAPI convierte funciones de Python en endpoints web. Asi otros sistemas pueden usar mi aplicacion."

### 03. Pruebas y TDD

Carpeta: `intermedio/03-pruebas-tdd`

Aqui se aprende:

- por que probar es importante
- como validar comportamiento esperado
- como separar logica para hacerla testeable
- como detectar reglas de negocio con pruebas

Ejemplo real del proyecto:

En `intermedio/03-pruebas-tdd/lab_03/app/service.py`:

- `confirm_order(...)` impide confirmar una orden vacia
- `mark_order_as_paid(...)` valida el flujo correcto
- `checkout(...)` integra negocio, precio y notificacion

Forma simple de explicarlo:

"Las pruebas me ayudan a asegurar que las reglas del negocio sigan funcionando aunque cambie el codigo."

### 04. Concurrencia y rendimiento

Carpeta: `intermedio/04-concurrencia-rendimiento`

Aqui el foco esta en:

- distinguir tareas CPU-bound y I/O-bound
- entender concurrencia
- comparar enfoques
- medir rendimiento

Forma simple de explicarlo:

"No todas las tareas tardan por la misma razon. Algunas esperan red o disco, otras consumen procesador. Este modulo ayuda a elegir la estrategia correcta."

### 05. SOLID en Python

Carpeta: `intermedio/05-solid-python.py`

Aqui se trabajan:

- responsabilidad unica
- abierto/cerrado
- sustitucion de Liskov
- segregacion de interfaces
- inversion de dependencias

Forma simple de explicarlo:

"SOLID no es teoria para memorizar. Son ideas para que el codigo sea mas facil de cambiar sin romper todo."

### 06. Patrones de diseno

Carpeta: `intermedio/06-patrones-diseno`

Aqui se ve:

- estrategia
- adaptador
- decorador
- separacion de responsabilidades

Ejemplo real del proyecto:

En este laboratorio aparecen estrategias de precio, un adaptador para proveedor externo y un decorador de cache. Es un buen ejemplo de como evitar codigo rigido.

Forma simple de explicarlo:

"Un patron de diseno es una forma conocida de resolver un problema repetido sin improvisar cada vez."

### 07. Ciencia de datos

Carpeta: `intermedio/07-ciencia-datos`

Aqui se introduce:

- carga de datos
- entrenamiento basico
- inferencia
- artefactos de modelo

Forma simple de explicarlo:

"Este bloque muestra que Python no solo sirve para APIs, tambien sirve para analisis y modelos predictivos."

### 08. Arquitectura hexagonal

Carpeta: `intermedio/08-arquitectura-hexagonal`

Este es uno de los bloques mas importantes del modulo.

Aqui se aprende:

- separacion por capas
- puertos y adaptadores
- dominio desacoplado
- casos de uso
- infraestructura intercambiable

Ejemplo real del proyecto:

En `intermedio/08-arquitectura-hexagonal/lab_08/app/application/use_cases.py`, `CreateOrderUseCase` crea una orden sin depender de FastAPI ni de SQLAlchemy directamente.

En `intermedio/08-arquitectura-hexagonal/lab_08/app/main.py`, FastAPI hace el wiring de dependencias y conecta el caso de uso con repositorio y notificador.

Forma simple de explicarlo:

"La arquitectura hexagonal busca que la logica de negocio no quede amarrada a la base de datos ni al framework web."

## 3. Conceptos y terminologia clave

- `ORM`: herramienta que conecta clases de Python con tablas de base de datos
- `CRUD`: crear, leer, actualizar y borrar
- `endpoint`: ruta de una API
- `request`: informacion que entra a la API
- `response`: informacion que devuelve la API
- `autenticacion`: proceso para verificar quien eres
- `dependencia`: objeto o servicio que otro componente necesita
- `test`: verificacion automatica de comportamiento
- `TDD`: enfoque donde primero se piensa en la prueba y luego en la implementacion
- `refactor`: mejorar el codigo sin cambiar su comportamiento
- `concurrencia`: capacidad de manejar varias tareas al mismo tiempo
- `patron de diseno`: solucion reusable para un problema comun
- `puerto`: contrato o interfaz que define como se conecta una capa con otra
- `adaptador`: implementacion concreta de ese puerto
- `caso de uso`: accion principal del negocio, por ejemplo crear una orden

## 4. Como explicarlo en una exposicion

Puedes decirlo asi:

"En el modulo intermedio aprendo a construir aplicaciones reales. Trabajo con base de datos, creo APIs, escribo pruebas, aplico principios de diseno y empiezo a separar mejor la logica del negocio de los detalles tecnicos. Es el modulo donde Python pasa de ser un lenguaje de practica a una herramienta de desarrollo de software."

## 5. Ejemplos reales que puedes mencionar

- CRUD con SQLAlchemy en `intermedio/01-acceso-datos-orm/lab_01/app/crud.py`
- Endpoints de ordenes en `intermedio/02-apis-web-fastapi/lab_02/app/routers/orders.py`
- Reglas de checkout en `intermedio/03-pruebas-tdd/lab_03/app/service.py`
- Caso de uso desacoplado en `intermedio/08-arquitectura-hexagonal/lab_08/app/application/use_cases.py`
- Wiring de FastAPI y dependencias en `intermedio/08-arquitectura-hexagonal/lab_08/app/main.py`

## 6. Ideas importantes para principiantes

- no todo el codigo debe ir en una sola funcion o archivo
- una API no es solo "internet"; es una forma de exponer funcionalidades
- una base de datos no se usa directamente desde cualquier parte del sistema
- las pruebas no son un extra: ayudan a evitar regresiones
- una buena arquitectura hace mas facil cambiar componentes despues

## 7. Que deberias dominar antes de pasar al siguiente modulo

Antes de `avanzado`, deberias poder:

- entender un CRUD completo
- leer una API con rutas, modelos y validaciones
- reconocer la diferencia entre logica de negocio e infraestructura
- entender por que existen pruebas
- seguir el flujo de un caso de uso en varias capas

## 8. Resumen corto para memorizar

`intermedio` ensena a construir aplicaciones reales con base de datos, APIs, pruebas y una mejor separacion de responsabilidades.
