param(
    [string]$BaseUrl = "http://127.0.0.1:8000"
)

$env:ORDERS_API_BASE_URL = $BaseUrl
$env:ORDERS_API_TIMEOUT = "10"

Write-Host "Probando configuración del CLI..." -ForegroundColor Cyan
poetry run orders-cli config

Write-Host ""
Write-Host "Probando listado de orders..." -ForegroundColor Cyan
poetry run orders-cli list