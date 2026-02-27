# Simulación de cuenta bancaria con decimales

saldo = 100000.0  # saldo base en cop (ahora como float)
op = ""

while op != "5":

    print("\n1. Visualizar saldo")
    print("2. Depositar a cuenta")
    print("3. Retirar de la cuenta")
    print("4. Consignar a otra cuenta")
    print("5. Salir")

    op = input("Ingrese la opcion: ")

    if op == "1":
        print(f"Tu saldo disponible es: ${saldo:.2f}")

    elif op == "2":
        deposito = float(input("¿Cuánto deseas depositar? "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("El monto debe ser mayor que 0.")

    elif op == "3":
        retiro = float(input("¿Cuánto deseas retirar? "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor que 0.")

    elif op == "4":
        consignacion = float(input("¿Cuánto deseas consignar? "))
        if consignacion > 0:
            if consignacion <= saldo:
                saldo -= consignacion
                print(f"Consignación exitosa. Nuevo saldo: ${saldo:.2f}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor que 0.")

    elif op == "5":
        print("Gracias por usar el sistema bancario.")

    else:
        print("Opción no válida.")