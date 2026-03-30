numeros = []

while True:
    print("1. agregar numero")
    print("2. mostrar numeros")
    print("3. salir")

    opcion = input("ingresa una opcion: ")

    if opcion == "1":
        numero = int(input("ingresa un numero: "))
        numeros.append(numero)

    elif opcion == "2":
        print(numeros)

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")