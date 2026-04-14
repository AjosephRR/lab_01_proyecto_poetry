from typing import Annotated

from fastapi import Depends, FastAPI

from secure_app.settings import Settings, get_settings

app = FastAPI(title="Security Maintenance Lab", version="0.1.0")


@app.get("/health")
def health(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, object]:
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.environment,
    }


@app.get("/config-check")
def config_check(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, object]:
    return settings.safe_dict()
