## Temas vistos
- Funciones con argumentos posicionales y nombrados
- Uso de `*args` y `**kwargs`
- Closures
- Decoradores
- Iteradores y generadores
- Comprensiones de listas
- Context managers con `with`

## Aprendizajes
- Una función bien diseñada debe tener una responsabilidad clara y una interfaz fácil de entender.
- Los argumentos posicionales y nombrados hacen que una función sea más flexible y legible.
- `*args` permite recibir múltiples argumentos posicionales en una sola función.
- `**kwargs` permite recibir argumentos nombrados variables de forma dinámica.
- Un closure permite que una función interna recuerde valores definidos en un contexto externo.
- Un decorador sirve para agregar comportamiento adicional a una función sin modificar su lógica principal.
- Un generador permite producir datos por partes usando `yield`, lo que puede ser útil cuando no conviene cargar todo de una vez.
- Un context manager ayuda a controlar recursos o bloques de código de manera más segura y ordenada.

## Relación con el laboratorio
En este laboratorio se implementó:

- una función con argumentos posicionales y nombrados,
- una función con `*args`,
- una función con `**kwargs`,
- un closure para crear multiplicadores,
- una comprensión de listas,
- un generador por lotes,
- un decorador de reintentos con backoff,
- y un context manager de temporización.

## Problemas encontrados
- Inicialmente el bloque `if __name__ == "__main__":` quedó mal indentado dentro de la función `main()`, por lo que el script no ejecutaba nada. Se corrigió moviéndolo fuera de la función.
- Se presentó un error tipográfico al escribir `time.pref_counter()` en lugar de `time.perf_counter()`. Se corrigió usando el nombre correcto de la función.
- También se ajustaron varios textos de salida en consola para mejorar consistencia y claridad.

