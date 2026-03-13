n = 5
tabla = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == 0:
            tabla[i][j] = 1
        elif i == 0:
            tabla[i][j] = 1
        else:
            tabla[i][j] = tabla[i-1][j] + tabla[i][j-1]

for fila in tabla:
    for num in fila:
        print(num, end="\t")
    print()