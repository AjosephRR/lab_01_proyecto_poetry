# Lab 03 - Funciones y programación pythonic

## Objetivo
Este laboratorio practica conceptos clave de la programación “pythonic” mediante ejemplos funcionales y reutilizables.

El script implementa:

- funciones con argumentos posicionales y nombrados,
- uso de `*args` y `**kwargs`,
- closures,
- decoradores,
- generadores,
- comprensiones,
- y un context manager con `with`.

Además, incluye tres componentes principales solicitados en el laboratorio del módulo:

- un decorador de reintentos con backoff,
- un generador por lotes,
- y un context manager de temporización.

## Temas aplicados
- Funciones y diseño de APIs claras
- Argumentos posicionales y nombrados
- Uso de `*args` y `**kwargs`
- Closures
- Decoradores
- Iteradores y generadores
- Comprensiones
- Context managers con `with`

## Estructura del laboratorio
- `src/main.py`: script principal del laboratorio
- `README-lab_03.md`: descripción del laboratorio

## Qué hace el programa
El programa demuestra distintos elementos del estilo pythonic:

1. Genera un saludo con argumentos posicionales y nombrados.
2. Suma múltiples valores usando `*args`.
3. Muestra una configuración dinámica usando `**kwargs`.
4. Crea funciones derivadas mediante closures.
5. Usa una comprensión de listas para obtener cuadrados de números pares.
6. Divide una lista de usuarios en lotes con un generador.
7. Simula una operación inestable y le aplica un decorador de reintentos con backoff.
8. Mide el tiempo de ejecución de un bloque usando un context manager.

## Cómo ejecutarlo
Ubícate en la carpeta del laboratorio y ejecuta:

```powershell
python .\src\main.py