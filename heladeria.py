# contadores para cada sabor
vainilla = 0 
chocolate = 0
fresa = 0   
#ciclo para los 5 clientes 
for i in range (5): 
    sabor = input ("ingrese el sabor (vainilla, chocolate, fresa): "). lower()
    
    if sabor == "vainilla":
        vainilla += 1 
    elif sabor == "chocolate":
        chocolate += 1
    elif sabor == "fresa":
        fresa += 1
    else:
        print("sabor no válido, por favor ingrese un sabor válido.")

#resultados finales 
print("\n pedidos totales: ")
print ("vainilla: ", vainilla)
print ("chocolate: ", chocolate)
print ("fresa: ", fresa)
        
 