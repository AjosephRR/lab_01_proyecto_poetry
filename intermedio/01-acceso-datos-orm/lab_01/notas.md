# Notas del laboratorio

## Qué entendí
- SQLite me permite practicar sin instalar un servidor de base de datos.
- SQLAlchemy ORM me deja modelar tablas como clases.
- Alembic sirve para versionar cambios en la base de datos.
- Las relaciones ayudan a conectar entidades como User -> Order -> OrderItem.
- Las pruebas con SQLite en memoria son rápidas y no ensucian el proyecto.

## Diferencia entre Core y ORM
- Core se parece más a escribir SQL estructurado.
- ORM se enfoca en trabajar con objetos y relaciones.
- En este laboratorio usé ORM porque el objetivo era modelar entidades y CRUD.

## Símbolos y sintaxis importante
- `->` indica el tipo de retorno de una función.
- `None` significa ausencia de valor.
- `|` significa unión de tipos, por ejemplo `User | None`.
- `@property` permite exponer un método como si fuera atributo.
- `with` abre un recurso y lo cierra automáticamente.
- `yield` en pytest fixture entrega el recurso temporalmente y luego permite limpiar.

## Lo que me costó más
- Entender cómo Alembic detecta los modelos.
- Entender que `relationship()` no crea columnas, sino relaciones a nivel ORM.
- Entender por qué en tests se usa SQLite en memoria.

## Drivers que existen aunque no usé todavía
- PostgreSQL: psycopg
- SQL Server: pyodbc
- MongoDB async: motor