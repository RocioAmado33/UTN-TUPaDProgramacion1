print("Bienvenido a Escape Room: La Bóveda")
   
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

# nombre del agente con validación
nombre = input("Ingrese el nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Nombre inválido. Ingrese solo letras: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\nEstado: Energía={energia}, Tiempo={tiempo}, Cerraduras abiertas={cerraduras_abiertas}, Alarma={'Sí' if alarma else 'No'}")
    print("Elija acción:")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    
    opcion = input("Ingrese opción (1-3): ")
    while opcion not in ("1", "2", "3"):
        opcion = input("Opción inválida. Ingrese 1, 2 o 3: ")
    
    if opcion == "1":
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        if energia < 0:
            energia = 0
        if tiempo < 0:
            tiempo = 0

        if energia < 40:
            riesgo = input("Riesgo de alarma: elija un número del 1 al 3: ")
            while riesgo not in ("1", "2", "3"):
                riesgo = input("Número inválido. Ingrese 1, 2 o 3: ")
            if riesgo == "3":
                alarma = True
                print("¡Alarma activada por riesgo!")

        if forzar_seguidas == 3:
            alarma = True
            print("¡Alarma activada! La cerradura se trabó, no se abre esta vez.")
        else:
            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura forzada y abierta exitosamente.")

    elif opcion == "2":
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        if energia < 0:
            energia = 0
        if tiempo < 0:
            tiempo = 0

        print("Hackeando panel:")
        codigo_parcial = ""
        letras = "ABCD"  

        for paso in range(4):
          codigo_parcial += letras[paso]  
          print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta automáticamente por hackeo!")

    elif opcion == "3":
        forzar_seguidas = 0
        tiempo -= 1
        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("Descansar con alarma activa consume energía extra.")

        if energia < 0:
            energia = 0
        if tiempo < 0:
            tiempo = 0

        print(f"Descansaste. Energía: {energia}, Tiempo: {tiempo}")

    # Verificar condiciones de fin después de cada turno
    if cerraduras_abiertas == 3:
        print("¡Felicidades, abriste las 3 cerraduras! GANASTE.")
        break
    elif energia <= 0 or tiempo <= 0:
        print("Se acabó tu energía o tiempo. PERDISTE.")
        break
    elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma y poco tiempo. PERDISTE.")
        break