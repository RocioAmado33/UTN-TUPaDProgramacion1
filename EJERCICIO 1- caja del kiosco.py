# EJERCICIO 1- caja del kiosco

# pedido de nombre y validacion
nombre_cliente = input("Ingrese su nombre: ")
while not nombre_cliente.isalpha() or nombre_cliente.strip() == "":
    print("Por favor, ingrese un nombre valido")
    nombre_cliente = input("ingrese su nombre: ")

# pedido cantidad de producto y validacion
cantidad = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error")
    cantidad = input("Ingrese la cantidad valida: ")
cantidad = int(cantidad)

# calculos de totales
total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(1, cantidad + 1):
    # pedido de precio y validacion
    precio = input(f"Producto {i}- Ingrese el precio: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Precio inválido, ingrese un número positivo")
        precio = input(f"Producto {i}- Ingrese el precio: ")
    precio = int(precio)
    
    total_sin_descuentos += precio  # suma sin descuento

    # descuento
    descuento = input(f"Producto {i} - ¿Tiene descuento? S/N: ").lower()
    while descuento not in ["s", "n"]:
        print("Respuesta inválida, ingrese S o N")
        descuento = input(f"Producto {i} - ¿Tiene descuento? S/N: ").lower()

    if descuento == "s":
        precio_desc = precio - (precio * 10 / 100)
    else:
        precio_desc = precio

    total_con_descuentos += precio_desc  # suma con descuento

    # resumen por producto
    print(f"Producto {i} - Precio: {precio}  Descuento: {descuento.upper()}  Precio final: {precio_desc:.2f}")

# calculos finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

# salida
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: {total_sin_descuentos}")
print(f"Total con descuentos: {total_con_descuentos}")
print(f"Ahorro: {ahorro}")
print(f"Promedio por producto: {promedio:.2f}")



       
        
