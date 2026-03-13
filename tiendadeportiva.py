contador = 0 

for i in range (5):
    precio = int(input("Ingrese el precio del producto: "))

    if precio > 100000:
        contador += 1 

print (" el numero de productos que valen mas de 100000 es: ", contador)