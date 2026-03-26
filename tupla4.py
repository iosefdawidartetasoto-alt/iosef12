filas = int(input("ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = input(f"ingrese valor ({i},{j}): ")
        fila.append(valor)
    matriz.append(fila)

# imprimir matriz:
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()