from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.db import create_db_and_tables
from app.routers.auth import router as auth_router
from app.routers.orders import router as orders_router

app = FastAPI(
    title="Lab 02 - Orders API con FastAPI",
    version="1.0.0",
    description="API de órdenes con validación, JWT básico y pruebas de integración.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = perf_counter()
    response = await call_next(request)
    duration = perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{duration:.6f}"
    return response


@app.get("/", tags=["health"])
def root() -> dict[str, str]:
    return {"message": "API FastAPI lab 02 funcionando"}


@app.post("/setup", tags=["setup"])
def setup_database() -> dict[str, str]:
    create_db_and_tables()
    return {"message": "Base de datos inicializada"}


app.include_router(auth_router)
app.include_router(orders_router)
