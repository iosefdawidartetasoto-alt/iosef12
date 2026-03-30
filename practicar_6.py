personas = {
    "Juan": 20,
    "Ana": 25,
    "Luis": 30
}

# pedir nombre 
nombre = input("ingresa el nombre a buscar:")
#buscar nombre y dar edad 
if nombre in personas:
    print ("tiene", personas[nombre], "años")
else: 
    print ("nombre no encontrado")