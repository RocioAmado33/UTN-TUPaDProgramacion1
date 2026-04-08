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
        
