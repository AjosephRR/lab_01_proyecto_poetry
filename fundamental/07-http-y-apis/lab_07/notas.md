# Notas del módulo 07 - HTTP y consumo de APIs

## Temas vistos
- `httpx`
- timeouts
- reintentos
- manejo de errores HTTP
- streaming de respuestas
- escritura a disco con `Path`

## Aprendizajes
- Un cliente HTTP robusto no solo hace peticiones; también debe manejar fallos.
- `httpx` permite construir clientes modernos con timeout y soporte para HTTP/2.
- Los reintentos con backoff ayudan a mejorar resiliencia frente a fallos temporales.
- El manejo correcto de errores evita que el programa falle silenciosamente.
- El streaming de respuestas permite descargar archivos de forma más eficiente en memoria.
- `Path` ayuda a crear rutas de salida de manera clara y segura.

## Relación con el laboratorio
En este laboratorio se implementó:
- un cliente `httpx`,
- lógica de reintentos con backoff,
- timeouts,
- manejo de errores HTTP y de red,
- consulta de JSON,
- y descarga de archivo por streaming a disco.

## Problemas encontrados
- [Escribe aquí errores reales que te aparezcan]
- [Ejemplo: Smocker no estaba levantado]
- [Ejemplo: endpoint incorrecto]
- [Ejemplo: timeout o error de conexión]

## Evidencia
- Laboratorio completado en `lab_07/`
- Cliente HTTP ejecutado correctamente
- Archivo descargado generado en `output/`