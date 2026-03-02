IMP = 0.004

u1 = input("Usuario 1: ")
s1 = float(input("Saldo inicial: "))

u2 = input("\nUsuario 2: ")
s2 = float(input("Saldo inicial: "))

while True:

    print("\n1. Ver saldos")
    print("2. Retirar")
    print("3. Consignar")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        print("\n--- SALDOS ---")
        print(f"{u1}: ${s1:.2f}")
        print(f"{u2}: ${s2:.2f}")

    elif op == "2":
        u = input("¿Quién retira? (1/2): ")
        m = float(input("Monto: "))
        t = m * (1 + IMP)

        if u == "1":
            if s1 >= t:
                s1 -= t
            elif s1 + s2 >= t:
                t -= s1
                s1 = 0
                s2 -= t
            else:
                print("Fondos insuficientes")
                continue

        elif u == "2":
            if s2 >= t:
                s2 -= t
            elif s2 + s1 >= t:
                t -= s2
                s2 = 0
                s1 -= t
            else:
                print("Fondos insuficientes")
                continue

        print("Retiro exitoso")

    elif op == "3":
        u = input("¿Quién consigna? (1/2): ")
        m = float(input("Monto: "))
        t = m * (1 + IMP)

        if u == "1" and s1 >= t:
            s1 -= t
            s2 += m
        elif u == "2" and s2 >= t:
            s2 -= t
            s1 += m
        else:
            print("Fondos insuficientes")
            continue

        print("Consignación exitosa")

    elif op == "4":
        print("Sistema cerrado")
        break

    else:
        print("Opción inválida")