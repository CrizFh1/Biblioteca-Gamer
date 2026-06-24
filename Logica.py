<<<<<<< HEAD
import json

juegos = []

def agregar_juego(nombre, plataforma, genero):
    nombre = nombre.strip()

    if buscar_juego(nombre):
        return False

    juegos.append({
        "nombre": nombre,
        "plataforma": plataforma,
        "genero": genero,
        "estado": "Pendiente"
    })
    return True


def mostrar_juegos():
    return juegos


def buscar_juego(nombre):
    nombre = nombre.lower().strip()
    return next((j for j in juegos if j["nombre"].lower() == nombre), None)


def cambiar_estado(nombre, nuevo_estado):
    juego = buscar_juego(nombre)
    if juego:
        juego["estado"] = nuevo_estado
        return True
    return False


def eliminar_juego(nombre):
    nombre = nombre.lower().strip()

    for i, juego in enumerate(juegos):
        if juego["nombre"].lower() == nombre:
            del juegos[i]
            return True

    return False



def obtener_estadisticas():
    pendientes = sum(1 for j in juegos if j["estado"] == "Pendiente")
    jugando = sum(1 for j in juegos if j["estado"] == "Jugando")
    terminados = sum(1 for j in juegos if j["estado"] == "Terminado")

    return {
        "total": len(juegos),
        "pendientes": pendientes,
        "jugando": jugando,
        "terminados": terminados
    }



def guardar_juegos():
    with open("juegos.json", "w", encoding="utf-8") as archivo:
        json.dump(juegos, archivo, indent=4, ensure_ascii=False)


def cargar_juegos():
    global juegos

    try:
        with open("juegos.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

            juegos = [
                {
                    "nombre": j["nombre"],
                    "plataforma": j["plataforma"],
                    "genero": j["genero"],
                    "estado": j.get("estado", "Pendiente")
                }
                for j in data
            ]

    except FileNotFoundError:
=======
import json

juegos = []

def agregar_juego(nombre, plataforma, genero):
    nombre = nombre.strip()

    if buscar_juego(nombre):
        return False

    juegos.append({
        "nombre": nombre,
        "plataforma": plataforma,
        "genero": genero,
        "estado": "Pendiente"
    })
    return True


def mostrar_juegos():
    return juegos


def buscar_juego(nombre):
    nombre = nombre.lower().strip()
    return next((j for j in juegos if j["nombre"].lower() == nombre), None)


def cambiar_estado(nombre, nuevo_estado):
    juego = buscar_juego(nombre)
    if juego:
        juego["estado"] = nuevo_estado
        return True
    return False


def eliminar_juego(nombre):
    nombre = nombre.lower().strip()

    for i, juego in enumerate(juegos):
        if juego["nombre"].lower() == nombre:
            del juegos[i]
            return True

    return False



def obtener_estadisticas():
    pendientes = sum(1 for j in juegos if j["estado"] == "Pendiente")
    jugando = sum(1 for j in juegos if j["estado"] == "Jugando")
    terminados = sum(1 for j in juegos if j["estado"] == "Terminado")

    return {
        "total": len(juegos),
        "pendientes": pendientes,
        "jugando": jugando,
        "terminados": terminados
    }



def guardar_juegos():
    with open("juegos.json", "w", encoding="utf-8") as archivo:
        json.dump(juegos, archivo, indent=4, ensure_ascii=False)


def cargar_juegos():
    global juegos

    try:
        with open("juegos.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

            juegos = [
                {
                    "nombre": j["nombre"],
                    "plataforma": j["plataforma"],
                    "genero": j["genero"],
                    "estado": j.get("estado", "Pendiente")
                }
                for j in data
            ]

    except FileNotFoundError:
>>>>>>> 2681aa70d34472511598ef123b70ef5d5613469b
        juegos = []