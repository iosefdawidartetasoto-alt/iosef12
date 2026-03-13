print("BIENVENIDO AL SPA")

# spa disponibilidad de producto
servicios = ["masaje", "facial", "manicure"]

print("1. Masaje")
print("2. Facial")
print("3. Manicure")

servicio_elegido = int(input("Ingresa el número del servicio que deseas: "))

if servicio_elegido == 1:
    print("Has elegido masaje, DISPONIBLE")
elif servicio_elegido == 2:
    print("Has elegido facial, DISPONIBLE")
elif servicio_elegido == 3:
    print("Has elegido manicure, DISPONIBLE")
else:
    print("Servicio no válido")