estudiantes = []

# CREATE
def agregar_estudiante():
    try:
        id_est = int(input("ID: "))
    except:
        print("❌ El ID debe ser un número")
        return

    # validar que el ID no exista
    for e in estudiantes:
        if e["id"] == id_est:
            print("❌ Ese ID ya existe")
            return
    
    nombre = input("Nombre: ")
    
    try:
        edad = int(input("Edad: "))
        nota = float(input("Nota: "))
    except:
        print("❌ Edad o nota inválida")
        return
    
    estudiante = {
        "id": id_est,
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }
    
    estudiantes.append(estudiante)
    print("✅ Estudiante agregado")


# READ
def mostrar_estudiantes():
    if not estudiantes:
        print("⚠️ No hay estudiantes")
        return
    
    print("\n📋 Lista de estudiantes:")
    for e in estudiantes:
        print(f"ID: {e['id']} | Nombre: {e['nombre']} | Edad: {e['edad']} | Nota: {e['nota']}")


# UPDATE
def actualizar_estudiante():
    try:
        id_buscar = int(input("Ingrese ID del estudiante: "))
    except:
        print("❌ ID inválido")
        return
    
    for e in estudiantes:
        if e["id"] == id_buscar:
            print("✅ Estudiante encontrado")
            
            e["nombre"] = input("Nuevo nombre: ")
            
            try:
                e["edad"] = int(input("Nueva edad: "))
                e["nota"] = float(input("Nueva nota: "))
            except:
                print("❌ Datos inválidos")
                return
            
            print("✏️ Estudiante actualizado")
            return
    
    print("❌ Estudiante no encontrado")


# DELETE
def eliminar_estudiante():
    try:
        id_buscar = int(input("Ingrese ID del estudiante: "))
    except:
        print("❌ ID inválido")
        return
    
    for e in estudiantes:
        if e["id"] == id_buscar:
            estudiantes.remove(e)
            print("🗑️ Estudiante eliminado")
            return
    
    print("❌ Estudiante no encontrado")


# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n=== CRUD ESTUDIANTES ===")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Opción inválida")


# EJECUTAR PROGRAMA
menu()