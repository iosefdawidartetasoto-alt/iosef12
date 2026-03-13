total_promedios = 0
estudiantes = 0

bajo = 0
medio = 0
alto = 0

mejor_promedio = 0
mejor_estudiante = ""

while True:

    nombre = input("Nombre del estudiante (o salir): ")

    if nombre == "salir":
        break

    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3

    total_promedios += promedio
    estudiantes += 1

    if promedio < 60:
        bajo += 1

    elif promedio < 80:
        medio += 1

    else:
        alto += 1

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

promedio_grupo = total_promedios / estudiantes

print("Promedio general:", promedio_grupo)
print("Mejor estudiante:", mejor_estudiante)
print("Nivel bajo:", bajo)
print("Nivel medio:", medio)
print("Nivel alto:", alto)
