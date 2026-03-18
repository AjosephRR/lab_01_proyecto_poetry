## Temas vistos
- Clases
- Composición
- Dunder methods
- `dataclass`
- `@property`
- Pydantic para validación y serialización

## Aprendizajes
- Una clase permite representar entidades con datos y comportamiento.
- La composición ayuda a construir objetos más complejos a partir de otros más simples.
- `dataclass` reduce código repetitivo cuando una clase representa principalmente datos.
- `__post_init__` permite ejecutar lógica adicional justo después de crear una instancia.
- `@property` ayuda a exponer cálculos derivados como si fueran atributos.
- Pydantic permite validar datos de entrada y generar salidas serializadas de forma clara.
- Separar entidad, entrada y salida mejora el diseño del modelo.

## Relación con el laboratorio
En este laboratorio se implementó:
- una clase `OrderItem`,
- una entidad `Order` como `dataclass`,
- cálculos derivados como subtotal, total y total de artículos,
- comparación entre órdenes,
- modelos Pydantic `OrderIn` y `OrderOut`,
- y conversión de datos de entrada validados a entidad.

## Problemas encontrados
- Se detectó un typo en la validación Pydantic al escribir `main_length` en lugar de `min_length`.
- También se detectó un error en los datos de entrada al escribir `prodcut_name` en lugar de `product_name`.
- Pydantic ayudó a identificar claramente qué campo faltaba y dónde estaba el problema.
- Después se corrigieron los datos y el script ejecutó correctamente.

## Validación realizada
Se ejecutó correctamente el script y se obtuvo:
- entidad creada,
- subtotal,
- descuento,
- total,
- salida serializada,
- y comparación entre órdenes.