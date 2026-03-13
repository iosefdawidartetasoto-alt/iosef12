n = int(input("ingresa un numero:"))

for i in range(n):
    print(" " * (n - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()