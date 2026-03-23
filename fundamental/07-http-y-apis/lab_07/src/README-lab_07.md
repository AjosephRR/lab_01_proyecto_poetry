# Lab 07 - HTTP y consumo de APIs

## Objetivo
Este laboratorio practica la construcción de un cliente HTTP robusto usando `httpx`.

Se enfoca en:
- timeouts,
- reintentos con backoff,
- manejo de errores,
- y descarga por streaming a disco.

## Temas aplicados
- `httpx`
- timeouts
- reintentos
- errores HTTP y de conexión
- streaming de respuestas
- escritura eficiente a disco

## Estructura del laboratorio
- `src/main.py`: cliente HTTP principal
- `output/reporte_descargado.csv`: archivo de salida descargado
- `README-lab_07.md`: descripción del laboratorio

## Qué hace el programa
El programa:
1. consulta un endpoint que devuelve JSON,
2. maneja errores y reintentos si falla,
3. descarga un archivo por streaming,
4. y guarda el resultado en disco.

