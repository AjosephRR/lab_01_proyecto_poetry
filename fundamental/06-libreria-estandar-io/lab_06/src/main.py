import csv
import json
import logging
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "ventas.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "reporte.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def leer_ventas(rutas_csv: Path) -> list[dict]:
    if not rutas_csv.exists():
        logging.error(f"No se encontro el archivo: {rutas_csv}")
        raise FileNotFoundError(f"No existe el archivo {rutas_csv}")

    ventas = []

    with rutas_csv.open(mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            venta = {
                "producto": fila["producto"],
                "categoria": fila["categoria"],
                "cantidad": int(fila["cantidad"]),
                "precio_unitario": float(fila["precio_unitario"]),
            }
            ventas.append(venta)

    logging.info(f"Se leyeron {len(ventas)} registros del CSV")
    return ventas


def calcular_metricas(ventas: list[dict]) -> dict:
    total_registros = len(ventas)
    monto_total = 0.0
    contador_productos = Counter()
    ventas_por_categoria = defaultdict(float)

    for venta in ventas:
        subtotal = venta["cantidad"] * venta["precio_unitario"]
        monto_total += subtotal
        contador_productos[venta["producto"]] += venta["cantidad"]
        ventas_por_categoria[venta["categoria"]] += subtotal

    producto_mas_vendido = None
    if contador_productos:
        producto_mas_vendido = contador_productos.most_common(1)[0][0]

    reporte = {
        "fecha_reporte": datetime.now(ZoneInfo("America/Mexico_City")).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "total_registros": total_registros,
        "monto_total": round(monto_total, 2),
        "producto_mas_veniddo": producto_mas_vendido,
        "ventas_por:categoria": {
            categoria: round(total, 2)
            for categoria, total in ventas_por_categoria.items()
        },
    }

    logging.info("Metricas calculadas correctamente")
    return reporte


def exportar_json(datos: dict, ruta_salida: Path) -> None:
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    with ruta_salida.open(mode="w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    logging.info(f"Reporte exportado a JSON en : {ruta_salida}")


def main() -> None:
    logging.info("Inicio del proceso de ingesta")

    try:
        ventas = leer_ventas(DATA_FILE)
        reporte = calcular_metricas(ventas)
        exportar_json(reporte, OUTPUT_FILE)
        logging.info("Proceso finalizado correctamente")
    except Exception as e:
        logging.exception(f"Ocurrió un error durante el proceso: {e}")


if __name__ == "__main__":
    main()
