import asyncio

from fastapi import FastAPI

app = FastAPI(title="Mock API para concurrencia")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/{item_id}")
async def get_item(item_id: int, delay: float = 0.30) -> dict[str, object]:
    await asyncio.sleep(delay)
    return {
        "id": item_id,
        "name": f"item-{item_id}",
        "delay": delay,
        "status": "ok",
    }
