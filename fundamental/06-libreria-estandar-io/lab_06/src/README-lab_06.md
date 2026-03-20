# Lab 06 - Librería estándar y E/S

## Objetivo
Este laboratorio practica el uso de la librería estándar de Python para trabajar con entrada y salida de datos.

Se enfoca en:
- manipular rutas y archivos con `pathlib`,
- leer datos desde un archivo CSV,
- calcular métricas,
- exportar resultados a JSON,
- y registrar el proceso con `logging`.

## Temas aplicados
- `pathlib`
- manejo de archivos
- `csv`
- `json`
- `datetime`
- `zoneinfo`
- `logging`

## Estructura del laboratorio
- `data/ventas.csv`: archivo de entrada
- `src/main.py`: script principal del laboratorio
- `output/reporte.json`: archivo de salida generado
- `README-lab_06.md`: descripción del laboratorio

## Qué hace el programa
El programa:
1. lee un archivo CSV con datos de ventas,
2. convierte cantidades y precios a tipos numéricos,
3. calcula métricas como monto total y producto más vendido,
4. agrupa ventas por categoría,
5. genera un reporte con fecha y hora de México,
6. exporta el resultado a JSON,
7. y registra todo el flujo usando `logging`.

