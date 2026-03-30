#inventario 
inventario = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)
    print(" Producto agregado correctamente")

def mostrar_inventario():
    for producto in inventario:
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("------")

def calcular_total():
    total = 0 
    for producto in inventario:
        total += producto["precio"] * producto["cantidad"]
    return total


#mostrar menu 
while True:
    print("1. agregar producto")
    print("2. mostrar inventario")
    print("3. calcular total")
    print("4. salir")
    opcion = input("ingresa una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2": 
        mostrar_inventario()
    elif opcion == "3": 
        print("el total del inventario es: " , calcular_total())
    elif opcion == "4": 
        print("saliendo...")
        break
    else: 
        print("opcion invalida")
