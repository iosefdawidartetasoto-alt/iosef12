print("BIENVENIDO A LA TIBURONBARBER")

while True:
    try:
        clientes = int(input("Ingrese la hora de llegada: "))

        if clientes >= 6 and clientes <= 11:
            print("El cliente llegó en la mañana")

        elif clientes >= 12 and clientes <= 17:
            print("El cliente llegó en la tarde")

        elif clientes >= 18 and clientes <= 22:
            print("El cliente llegó en la noche")

        else:
            print("El cliente llegó fuera del horario de atención")

        break

    except ValueError:
        print("Error: debes ingresar un número, no letras.")