## Temas vistos
- Sintaxis e indentación en Python
- Variables y alcance
- Tipos básicos de datos
- Colecciones: list, dict, set, tuple
- Control de flujo con if, for, while y match/case
- Manejo de errores con try-except
- Validación básica con expresiones regulares
- Lectura de archivos JSON

## Aprendizajes
- Python usa indentación para definir bloques de código.
- Las listas y diccionarios permiten trabajar de forma práctica con datos estructurados.
- `match/case` ayuda a clasificar escenarios de forma más clara.
- El manejo de excepciones evita que el programa falle abruptamente.
- El módulo `json` permite convertir fácilmente el contenido de un archivo a estructuras de Python.
- Las expresiones regulares sirven para validar patrones de texto, como correos electrónicos.

## Relación con el laboratorio
En este laboratorio se construyó un script que:
- lee un archivo JSON,
- filtra usuarios activos,
- agrupa datos por ciudad,
- valida correos con regex,
- clasifica edades con pattern matching,
- y maneja errores de archivo y formato.

## Problemas encontrados
- [Escribe aquí los errores reales que te aparezcan]
- [Ejemplo: ruta incorrecta al JSON]
- [Ejemplo: archivo mal formado]
- [Ejemplo: error al crear carpetas en vez de archivos]

## Evidencia
- Laboratorio completado en `lab_02/`

## Prueba de manejo de errores
Se renombró temporalmente el archivo `usuarios.json` para validar el manejo de error por archivo inexistente.

### Resultado
El programa mostró el mensaje:
- "Error: no se encontró el archivo ..."
- "No fue posible procesar usuarios."

### Conclusión
El bloque `try-except` funcionó correctamente al capturar `FileNotFoundError` sin detener abruptamente la ejecución.