from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Mock API activa"}


@app.get("/api/status")
def get_status():
    return {
        "status": "ok",
        "service": "mock-api",
        "version": "1.0",
        "message": "API local funcionando correctamente",
    }


@app.get("/files/reporte.csv")
def get_csv_file():
    contenido_csv = """producto,categoria,cantidad,precio_unitario
Mouse,Perifericos,2,150
Teclado,Perifericos,1,300
Monitor,Pantallas,3,2500
Laptop,Computo,1,12000
"""

    return Response(
        content=contenido_csv,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=reporte.csv"},
    )
