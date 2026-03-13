# precio de las entradas al cine según edad

menoresde12 = 8000
adultosde13a59 = 12000
mayoresde60 = 9000

while True:
    try:
        edad = int(input("Ingrese su edad para calcular el precio de la entrada al cine: "))

        if edad < 13:
            precio = menoresde12
        elif edad >= 12 and edad <= 59:
            precio = adultosde13a59
        else:
            precio = mayoresde60

        print("El precio de su entrada es:", precio)

    except ValueError:
        print("Por favor, ingrese una edad válida.")