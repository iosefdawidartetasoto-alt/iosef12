total_dia = 0

while True:

    pedido = input("Producto (cafe, capuchino, pastel o salir): ")

    if pedido == "salir":
        break

    cantidad = int(input("Cantidad: "))

    if pedido == "cafe":
        total = 4000 * cantidad

    elif pedido == "capuchino":
        total = 7000 * cantidad

    elif pedido == "pastel":
        total = 6000 * cantidad

    else:
        print("Producto no válido")
        continue

    if total > 20000:
        descuento = total * 0.10
        total = total - descuento

    print("Total del cliente:", total)

    total_dia += total

print("Total vendido en el día:", total_dia)
