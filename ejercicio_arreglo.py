list = [7 , 12 , 24 , 31 , 39 , 47 , 55 , 68 , 74]
buscar = int(input("ingresa el numero: "))

izquierda = 0 
derecha = len(list)-1
medio = (izquierda + derecha) //2 
sw = False
while sw == False and izquierda <= derecha:

    if list[medio] == buscar: 
        print ("bingo")
        sw = True

    elif list[medio] < buscar:
        izquierda = medio + 1
        medio = (izquierda + derecha) // 2
    else: 
        derecha = medio - 1 
        medio = (izquierda + derecha) //2
if not sw:
    print("No se ha encontrado en la lista")
