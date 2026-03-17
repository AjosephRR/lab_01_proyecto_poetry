import json
import re
from pathlib import Path


def validar_correo(correo: str) -> bool:
    """
    Valida si un correo tiene un formato básico correcto usando expresiones regulares
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(patron, correo))


def clasificar_edad(edad: int) -> str:
    """
    Clasifica una edad usando pattern matching
    """
    match edad:
        case edad if edad < 18:
            return "menor de edad"
        case edad if 18 <= edad <= 29:
            return "joven adulto"
        case edad if 30 <= edad <= 59:
            return "adulto"
        case _:
            return "adulto mayor"


def leer_usuarios(ruta_archivo: Path) -> list[dict]:
    """
    Lee una rchivo JSON y devuelve unalista de usuarios tambipen
    maneja error de archivo inexistente y formato invalido.
    """

    try:
        with ruta_archivo.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError(
                "El contenido del archivo JSON debe de ser una lista de usuarios."
            )
        return datos
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo {ruta_archivo}")
        return []

    except json.JSONDecodeError:
        print("Error: el archivo no contiene un JSON valido.")
        return []

    except ValueError as error:
        print(f"Error de validación: {error}")
        return []


def filtrar_activos(usuarios: list[dict]) -> list[dict]:
    """
    Devuelve solo los usuarios activos
    """

    return [usuarios for usuarios in usuarios if usuarios.get("activo") is True]


def agrupar_por_ciudad(usuarios: list[dict]) -> dict[str, int]:
    """
    Cuenta cuantos usuarios activos hay por ciudad.
    """

    resumen = {}

    for usuario in usuarios:
        ciudad = usuario.get("ciudad", "Desconocida")
        resumen[ciudad] = resumen.get(ciudad, 0) + 1

    return resumen


def mostrar_resumen(usuarios: list[dict]) -> None:
    """
    Muestra información resumida de cada usuario.
    """

    print("\n=== RESUMEN DE USUARIOS ===")

    for usuario in usuarios:
        try:
            nombre = usuario["nombre"]
            edad = usuario["edad"]
            correo = usuario["correo"]

            correo_valido = validar_correo(correo)
            categoria = clasificar_edad(edad)

            print(f"Nombre: {nombre}")
            print(f"Edad: {edad} ({categoria})")
            print(f"Correo válido: {'Sí' if correo_valido else 'No'}")
            print("-" * 30)

        except KeyError as error:
            print(f"Error: falta la clave oblihatoria {error} en un usuario.")


def main() -> None:
    """
    Función principal de programa
    """

    ruta_json = Path(__file__).resolve().parent.parent / "data" / "usuarios.json"
    usuarios = leer_usuarios(ruta_json)

    if not usuarios:
        print("No fue posible procesar usuarios.")
        return

    usuarios_activos = filtrar_activos(usuarios)
    conteo_ciudades = agrupar_por_ciudad(usuarios_activos)

    print("Usarios activos encontrados:", len(usuarios_activos))
    print("\nUsuarios activos por ciudad:")

    for ciudad, total in conteo_ciudades.items():
        print(f"- {ciudad}: {total}")

        mostrar_resumen(usuarios_activos)


if __name__ == "__main__":
    main()
