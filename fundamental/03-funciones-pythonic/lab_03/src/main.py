import random
import time
from contextlib import contextmanager
from functools import wraps


def saludar(nombre: str, saludo: str = "Hola") -> str:
    """
    Ejemplo de función con argumento posicional y nombrado.
    """

    return f"{saludo}, {nombre}"


def sumar_todos(*args: int) -> int:
    """
    Ejemplo de uso de *args para recibir varios números.
    """

    return sum(args)


def mostrar_configuracion(**kwargs) -> None:
    """
    Ejemplo de uso de **kwargs para recibir argumentos nombrados variables
    """

    print("\nConfiguración recibids:")
    for clave, valor in kwargs.items():
        print(f"_ {clave}: {valor}")


def crear_multiplicador(factor: int):
    """
    Ejemplo de clouser.
    La función interna recuerda el valor de 'factor'.
    """

    def multiplicar(numero: int) -> int:
        return numero * factor

    return multiplicar


def reintentos(
    max_intentos: int = 3, espera_inicial: float = 0.5, factor_backoff: float = 2.0
):
    """
    Decorador que reintenta la ejecución de una función si falla,
    aplicado backoff incremental.
    """

    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            espera_actual = espera_inicial

            for intento in range(1, max_intentos + 1):
                try:
                    print(f"\nIntento {intento} de {max_intentos}...")
                    return func(*args, **kwargs)
                except Exception as error:
                    print(f"Error_detectado: {error}")

                    if intento == max_intentos:
                        print("Se agotaron los intentos.")
                        raise

                    print(f"Reintentando en {espera_actual:.2f} segundos...")
                    time.sleep(espera_actual)
                    espera_actual *= factor_backoff

        return wrapper

    return decorador


@reintentos(max_intentos=4, espera_inicial=0.5, factor_backoff=2)
def obtener_dato_remoto() -> str:
    """
    Simula una operación inestable que a veces falla.
    """

    if random.random() < 0.7:
        raise ConnectionError("Falló la conexión con el servicio remoto.")
    return "Dato obtenido correctamente."


def generar_lotes(datos: list, tamano_lote: int):
    """
    Generador que divide una lista en lotes.
    """

    for i in range(0, len(datos), tamano_lote):
        yield datos[i : i + tamano_lote]


@contextmanager
def temporizador(nombre_bloque: str = "Bloque de código"):
    """
    Context manager que mide el tiempo de ejecución de un bloque.
    """

    inicio = time.perf_counter()
    print(f"\nIniciando: {nombre_bloque}")
    try:
        yield
    finally:
        fin = time.perf_counter()
        duracion = fin - inicio
        print(f"Finalizó: {nombre_bloque}")
        print(f"Duración: {duracion:.6f} segundos")


def main() -> None:
    """
    Función principal del laboratorio.
    """

    print("=== Módulo 03 - FUNCIONES Y PROGRAMACIÓN PYTHONIC ===")

    # Función con argumento nombrado
    mensaje = saludar("Joeeph", saludo="Que tal")
    print(mensaje)

    # *args
    total = sumar_todos(10, 20, 30, 40)
    print(f"\nSuma total: {total}")

    # **kwargs
    mostrar_configuracion(modo="desarrollo", reintentos=4, activo=True)

    # Closure
    duplicar = crear_multiplicador(2)
    triplicar = crear_multiplicador(3)

    print(f"\nDuolicar 5: {duplicar(5)}")
    print(f"Triplicar 5: {triplicar(5)}")

    # Comprensión de listas
    numeros = [1, 2, 3, 4, 5, 6]
    cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
    print(f"\nCuadrados de números pares: {cuadrados_pares}")

    # Generador por lotes
    usuarios = ["Ana", "Luis", "María", "Carlos", "Elena", "Sofía", "Pedro"]
    print("\nLotes de usuarios:")
    for lote in generar_lotes(usuarios, 3):
        print(lote)

    # Context manager de temporización + decorador de reintentos
    with temporizador("Consulta remota con reintentos"):
        try:
            resultado = obtener_dato_remoto()
            print(resultado)
        except ConnectionError as error:
            print(f"Resultado final: {error}")


if __name__ == "__main__":
    main()
