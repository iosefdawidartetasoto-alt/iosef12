# cobro de parqueadero
print ("Bienvenido al parqueadero del metropolitano #purojunior")
horas = int (input ("ingrese el numero de horas que estuvo parqueado: "))
if horas <=1 :
    print ("el valor a pagar es de 5000")
elif horas >1 and horas < 3:
    print ("el valor a pagar es de 3000")

total = 5000 + (horas - 1) * 3000
print ("el valor total a pagar es de: ", total)

