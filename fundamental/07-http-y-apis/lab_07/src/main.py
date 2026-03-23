import logging
import os
import time
from dataclasses import dataclass
from pathlib import Path

import httpx

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
DOWNLOAD_FILE = OUTPUT_DIR / "reporte_descargado.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@dataclass(frozen=True)
class RetryConfig:
    max_attempts: int = 3
    timeout_seconds: float = 5.0
    backoff_seconds: float = 1.0


class ApiClient:
    def __init__(self, base_url: str, retry_config: RetryConfig) -> None:
        self.base_url = base_url.rstrip("/")
        self.retry_config = retry_config
        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=httpx.Timeout(self.retry_config.timeout_seconds),
            http2=True,
        )

    def close(self) -> None:
        self.client.close()

    def _request_with_retries(
        self, method: str, endpoint: str, **kwargs
    ) -> httpx.Response:
        """
        Ejecuta una petición HTTP con reintentos y backoff
        """

        wait_time = self.retry_config.backoff_seconds

        for attempt in range(1, self.retry_config.max_attempts + 1):
            try:
                logging.info(f"Intento {attempt} para {method} {endpoint}")
                response = self.client.request(method, endpoint, **kwargs)
                response.raise_for_status()
                return response

            except httpx.HTTPStatusError as error:
                status_code = error.response.status_code
                logging.warning(f"Respuesta HTTP inválida: {status_code}")

                # Solo reintenta si es error 5xx o 429
                if status_code < 500 and status_code != 429:
                    raise

                if attempt == self.retry_config.max_attempts:
                    raise

            except httpx.TimeoutException as error:
                logging.warning(f"Timeout detecatado: {error}")

                if attempt == self.retry_config.max_attempts:
                    raise

            except httpx.RequestError as error:
                logging.warning(f"Error de red o conexión: {error}")

                if attempt == self.retry_config.max_attempts:
                    raise

            logging.info(f"Reintentando en {wait_time:.2} segundos... ")
            time.sleep(wait_time)
            wait_time *= 2

        raise RuntimeError("No se pudo completar la petición")

    def get_json(self, endpoint: str) -> dict:
        """
        Obtiene una respuest json usando reintentos.
        """

        response = self._request_with_retries("GET", endpoint)
        return response.json()

    def download_streaming(self, endpoint: str, destination: Path) -> None:
        """
        Descarga un archivo por streaming y lo guarda en disco
        """

        destination.parent.mkdir(parents=True, exist_ok=True)
        Wait_time = self.retry_config.backoff_seconds

        for attempt in range(1, self.retry_config.max_attempts + 1):
            try:
                logging.info(f"Intento {attempt} para descargar {endpoint}")

                with self.client.stream("GET", endpoint) as response:
                    response.raise_for_status()

                    with destination.open("wb") as output_file:
                        for chunk in response.iter_bytes(chunk_size=8192):
                            if chunk:
                                output_file.write(chunk)

                logging.info(f"Archivo descargado correctamente en: {destination}")
                return

            except httpx.HTTPStatusError as error:
                status_code = error.response.status_code
                logging.warning(f"Error HTTP al descargar: {status_code}")

                if status_code < 500 and status_code != 429:
                    raise

                if attempt == self.retry_config.max_attempts:
                    raise

            except httpx.TimeoutException as error:
                logging.warning(f"Timeout durante descarga: {error}")

                if attempt == self.retry_config.max_attempts:
                    raise

            except httpx.RequestError as error:
                logging.warning(f"Error de red durante descarga: {error}")

                if attempt == self.retry_config.max_attempts:
                    raise

            logging.info(f"Reintentando descarga en {Wait_time:.2f} segundos...")
            time.sleep(Wait_time)
            Wait_time *= 2

        raise RuntimeError("No se pudo completar la descarga")


def main() -> None:
    print("=== MÓDULO 07 - HTTP Y CONSUMO DE APIS ===")

    # Url de Smocker
    base_url = os.getenv("SMOCKER_BASE_URL", "http://localhost:8000")

    # Deependen de mis Mocks
    status_endpoint = "/api/status"
    download_endpoint = "/files/reporte.csv"

    client = ApiClient(
        base_url=base_url,
        retry_config=RetryConfig(
            max_attempts=3,
            timeout_seconds=5.0,
            backoff_seconds=1.0,
        ),
    )

    try:
        logging.info("Iniciando consulta al endpoint JSON")
        metadata = client.get_json(status_endpoint)
        print("\nRespuesta JSON recibida:")
        print(metadata)

        logging.info("Iniciando descarga por streaming")
        client.download_streaming(download_endpoint, DOWNLOAD_FILE)

        print("\nDescarga finalizada correctamente.")
        print(f"Archivo guardado en: {DOWNLOAD_FILE}")

    except Exception as error:
        logging.exception(f"Ocurrió un error durante el proceso HTTP: {error}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
