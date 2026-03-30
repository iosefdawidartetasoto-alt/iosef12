inventario = [
    {"nombre": "arroz", "precio": 2000, "cantidad": 3},
    {"nombre": "leche", "precio": 3000, "cantidad": 2}
]
#recorrer inventario e imprimir valor de cada producto 
for productos in inventario: 
    print ("PRODUCTOS:", productos["nombre"])
#calcular valor total de todo el inventario y mostrarlo
total_inventario = inventario[0]["precio"] * inventario[0]["cantidad"] + inventario[1]["precio"] * inventario[1]["cantidad"]
print ("el valor total del inventario es:", total_inventario)