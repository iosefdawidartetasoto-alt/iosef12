# Articulos
menu = {
    "cafe": 4000,
    "te": 3500,
    "jugo": 5000
}

# Menu de la cafeteria 
print("BIENVENIDO A LA CAFETERIA DEL TIBURON #JUNIORMANDA") 

producto = input("Ingrese el producto que desea comprar (cafe, te, jugo): ").lower()
cantidad = int(input("¿Cuantos? "))

# Calculamos producto y cantidad
if producto == "cafe":
    total = menu["cafe"] * cantidad
elif producto == "te":
    total = menu["te"] * cantidad
elif producto == "jugo":
    total = menu["jugo"] * cantidad
else:
    total = 0
    print("Producto no válido, por favor ingrese un producto válido.")

# Verificamos si hubo una compra válida para imprimir el recibo
if total > 0:
    print(f"El total a pagar por {cantidad} {producto}(s) es: {total} pesos")
