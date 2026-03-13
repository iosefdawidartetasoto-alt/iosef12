# asistencias por estudiante en un mes

nombreestudiante = input("Hola estudiante, ingrese su nombre: ")

while True:
    try:
        dias = int(input(f"Bienvenido {nombreestudiante}, ingrese el número de días que asistió a clases este mes: "))

        if dias < 0 or dias > 30:
            print("Ingrese un número entre 0 y 30.")
        else:
            break   # si es válido, sale del ciclo

    except ValueError:
        print("Por favor, ingrese un número válido.")

# clasificación de asistencia
if dias <= 5:
    print("Tu asistencia es baja")
elif dias <= 8:
    print("Tu asistencia es media")
else:
    print("Tu asistencia es alta")