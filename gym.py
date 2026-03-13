# acceso a gym por edad
edad = int(input("para ingresar digite su edad : "))

if edad <13:
    print("lo siento no puedes ingresar al gym")
elif edad >=13 and edad <18:
    print ("puedes ingresar con tus representantes")
elif edad >=18 and edad <59:
    print ("puedes ingresar al gym sin restricciones")
else: 
    print ("perteneces a la clase sennior puedes ingresar al gym")

 