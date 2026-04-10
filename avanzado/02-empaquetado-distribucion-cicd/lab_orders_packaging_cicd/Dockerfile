FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=2.1.1

WORKDIR /app

RUN pip install "poetry==${POETRY_VERSION}"

COPY pyproject.toml README.md ./
COPY src ./src

RUN poetry build -f wheel


FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN useradd --create-home --shell /bin/bash appuser

COPY --from=builder /app/dist/*.whl /tmp/

RUN pip install /tmp/*.whl && rm -rf /tmp/*.whl

USER appuser

EXPOSE 8000

CMD ["uvicorn", "orders_packaged_api.main:app", "--host", "0.0.0.0", "--port", "8000"]