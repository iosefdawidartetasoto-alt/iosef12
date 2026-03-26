jugador_baloncesto = {
    1: {"id": 1048229292, "nombre": "Jander", "apellido": "Arguello", "edad": 30},
    2: {"id": 1048229296, "nombre": "Luisa", "apellido": "De la Rosa", "edad": 19},
    3: {"id": 1048229297, "nombre": "Maria", "apellido": "Sanchez", "edad": 19}
}

while True:
    print("\n--- MENÚ ---")
    print("1. Ver jugadores")
    print("2. Agregar jugador")
    print("3. Buscar jugador por ID")
    print("4. Eliminar jugador por ID")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # 🔍 VER TODOS
    if opcion == "1":
        for llave, datos in jugador_baloncesto.items():
            print(f"{llave}: {datos}")

    # ➕ AGREGAR
    elif opcion == "2":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        id_jugador = int(input("ID: "))

        nueva_clave = max(jugador_baloncesto.keys()) + 1

        jugador_baloncesto[nueva_clave] = {
            "id": id_jugador,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad
        }

        print("Jugador agregado ")

    # 🔎 BUSCAR POR ID
    elif opcion == "3":
        busqueda_id = int(input("Ingrese el ID: "))
        encontrado = None

        for datos in jugador_baloncesto.values():
            if datos["id"] == busqueda_id:
                encontrado = datos
                break

        if encontrado:
            print("Jugador encontrado:", encontrado)
        else:
            print("No encontrado ")

    # ELIMINAR POR ID
    elif opcion == "4":
        eliminar_id = int(input("Ingrese el ID: "))
        llave_a_eliminar = None

        for llave, datos in jugador_baloncesto.items():
            if datos["id"] == eliminar_id:
                llave_a_eliminar = llave
                break

        if llave_a_eliminar:
            del jugador_baloncesto[llave_a_eliminar]
            print("Jugador eliminado ")
        else:
            print("No encontrado ")

    # 🚪 SALIR
    elif opcion == "5":
        print("Saliendo del sistema ")
        break

    else:
        print("Opción inválida ")  