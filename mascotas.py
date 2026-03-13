print("BIENVENIDO A LA TIENDA DE MASCOTAS")
print("1. Perro")
print("2. Gato")
print("3. Conejo")

mascota = int(input("Seleccione la mascota para saber su información alimenticia: "))

if mascota == 1:
    print("Proteína, grasas saludables, carbohidratos, vitaminas, minerales.")

elif mascota == 2:
    print("Proteína animal, grasas, taurina, vitaminas, minerales.")

elif mascota == 3:
    print("Heno, verduras frescas, agua, pellets, fibra.")

else:
    print("Opción no válida.")