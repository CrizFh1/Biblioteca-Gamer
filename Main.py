<<<<<<< HEAD
from Logica import *

cargar_juegos()

while True:

    print("\n========== MI BIBLIOTECA GAMER ==========")
    print("1. Agregar juego")
    print("2. Ver biblioteca")
    print("3. Buscar juego")
    print("4. Actualizar estado")
    print("5. Eliminar juego")
    print("6. Ver estadísticas")
    print("7. Salir")

    opcion = input("\nSelecciona una opción: ")

    
    if opcion == "1":

        nombre = input("Nombre del juego: ")
        plataforma = input("Plataforma: ")
        genero = input("Género: ")

        if agregar_juego(nombre, plataforma, genero):
            print(f"\n'{nombre}' agregado correctamente.")
        else:
            print("\nEse juego ya existe.")

    
    elif opcion == "2":

        lista = mostrar_juegos()

        if not lista:
            print("\nBiblioteca vacía.")
        else:
            for i, juego in enumerate(lista, start=1):
                print(f"\nJuego #{i}")
                print("-" * 30)
                print(f"Nombre: {juego['nombre']}")
                print(f"Plataforma: {juego['plataforma']}")
                print(f"Género: {juego['genero']}")
                print(f"Estado: {juego['estado']}")

    
    elif opcion == "3":

        nombre = input("¿Qué juego quieres buscar? ")
        juego = buscar_juego(nombre)

        if juego:
            print("\n Encontrado:")
            print(juego)
        else:
            print("\nNo encontrado.")


    elif opcion == "4":

        nombre = input("Nombre del juego: ")

        print("\n1. Pendiente")
        print("2. Jugando")
        print("3. Terminado")

        estado_op = input("Opción: ")

        estados = {
            "1": "Pendiente",
            "2": "Jugando",
            "3": "Terminado"
        }

        if estado_op in estados:
            cambiar_estado(nombre, estados[estado_op])
            print("\nEstado actualizado.")
        else:
            print("\nOpción inválida.")

    
    elif opcion == "5":

        nombre = input("Juego a eliminar: ")

        if eliminar_juego(nombre):
            print("\nEliminado correctamente.")
        else:
            print("\nNo encontrado.")

    
    elif opcion == "6":

        datos = obtener_estadisticas()

        print("\n========== ESTADÍSTICAS ==========")
        print(f"Total: {datos['total']}")
        print(f"Pendientes: {datos['pendientes']}")
        print(f"Jugando: {datos['jugando']}")
        print(f"Terminados: {datos['terminados']}")

    elif opcion == "7":

        guardar_juegos()
        print("\nGuardando datos... hasta luego")
        break

    else:
=======
from Logica import *

cargar_juegos()

while True:

    print("\n========== MI BIBLIOTECA GAMER ==========")
    print("1. Agregar juego")
    print("2. Ver biblioteca")
    print("3. Buscar juego")
    print("4. Actualizar estado")
    print("5. Eliminar juego")
    print("6. Ver estadísticas")
    print("7. Salir")

    opcion = input("\nSelecciona una opción: ")

    
    if opcion == "1":

        nombre = input("Nombre del juego: ")
        plataforma = input("Plataforma: ")
        genero = input("Género: ")

        if agregar_juego(nombre, plataforma, genero):
            print(f"\n'{nombre}' agregado correctamente.")
        else:
            print("\nEse juego ya existe.")

    
    elif opcion == "2":

        lista = mostrar_juegos()

        if not lista:
            print("\nBiblioteca vacía.")
        else:
            for i, juego in enumerate(lista, start=1):
                print(f"\nJuego #{i}")
                print("-" * 30)
                print(f"Nombre: {juego['nombre']}")
                print(f"Plataforma: {juego['plataforma']}")
                print(f"Género: {juego['genero']}")
                print(f"Estado: {juego['estado']}")

    
    elif opcion == "3":

        nombre = input("¿Qué juego quieres buscar? ")
        juego = buscar_juego(nombre)

        if juego:
            print("\n Encontrado:")
            print(juego)
        else:
            print("\nNo encontrado.")


    elif opcion == "4":

        nombre = input("Nombre del juego: ")

        print("\n1. Pendiente")
        print("2. Jugando")
        print("3. Terminado")

        estado_op = input("Opción: ")

        estados = {
            "1": "Pendiente",
            "2": "Jugando",
            "3": "Terminado"
        }

        if estado_op in estados:
            cambiar_estado(nombre, estados[estado_op])
            print("\nEstado actualizado.")
        else:
            print("\nOpción inválida.")

    
    elif opcion == "5":

        nombre = input("Juego a eliminar: ")

        if eliminar_juego(nombre):
            print("\nEliminado correctamente.")
        else:
            print("\nNo encontrado.")

    
    elif opcion == "6":

        datos = obtener_estadisticas()

        print("\n========== ESTADÍSTICAS ==========")
        print(f"Total: {datos['total']}")
        print(f"Pendientes: {datos['pendientes']}")
        print(f"Jugando: {datos['jugando']}")
        print(f"Terminados: {datos['terminados']}")

    elif opcion == "7":

        guardar_juegos()
        print("\nGuardando datos... hasta luego")
        break

    else:
>>>>>>> 2681aa70d34472511598ef123b70ef5d5613469b
        print("\nOpción inválida.")