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


#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

# Credenciales fijas en el código
usuario_c = "alumno"
clave_c = "python123"

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")
contador = 0

# Intentos
while contador < 2 and (usuario != usuario_c or clave != clave_c):
    print("Error, el usuario o la clave son incorrectas")
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    contador += 1
    if contador == 2:
        print("Cuenta bloqueada")
        break

# Acceso correcto
if usuario == usuario_c and clave == clave_c:
    eleccion = 0  # inicializamos variable
    while eleccion != 4:
        # Mostrar menú
        print(
              "1. Ver estado de inscripción\n"
              "2. Cambiar clave\n"
              "3. Mostrar mensaje motivacional\n"
              "4. Salir\n")
        
        eleccion = input("Opción: ")

        # Validación del menú
        if not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > 4:
            print("Opción inválida, ingrese un número del 1 al 4")
            continue

        eleccion = int(eleccion)

        # Opciones del menú
        if eleccion == 1:
            print("Inscripto\n")
        elif eleccion == 2:
            nueva_clave = input("Ingresa una nueva clave, con mínimo 6 caracteres: ")
            nueva_clave_conf = input("Repite la nueva clave: ")
            if nueva_clave == nueva_clave_conf and len(nueva_clave) > 6:
                print("El cambio de clave se ha realizado con éxito\n")
            else:
                print("Error: las claves no coinciden o no tienen 6 caracteres\n")
        else:
            print("La constancia es la clave del éxito\n")
        
