print("Bienvenido a La Arena del Gladiador")

#  Nombre del jugador con validación
gladiador = input("Ingrese el nombre del Gladiador: ")
while not gladiador.isalpha():
    gladiador = input("Error: Solo se permiten letras. Ingrese nuevamente: ")

# Variables iniciales
vida_gladiador = 100
vida_enemigo = 100 
posion_vida = 3 
dano_base_ataque_pesado = 15 
dano_base_del_enemigo = 12 
turno_gladiador = True  

# combate
while vida_gladiador > 0 and vida_enemigo > 0:

    if turno_gladiador:
        # TURNO DEL JUGADOR
        print(f"""
                Gladiador: Puntos de vida {vida_gladiador}
                Enemigo: Puntos de vida {vida_enemigo}
                Pociones disponibles: {posion_vida}""")
        
        print("""1. Ataque Pesado
                 2. Ráfaga Veloz 
                 3. Curar""")
        
        opcion = input("Escoge tu movimiento: ")

        # VALIDACIÓN
        while not opcion.isdigit() or opcion not in ("1", "2", "3"):
            opcion = input("Error, elija 1, 2 o 3: ")

        # ACCIONES
        if opcion == "1":
            dano = dano_base_ataque_pesado

            if vida_enemigo < 20:
                dano = dano * 1.5  
                print("¡Golpe crítico!")

            vida_enemigo -= dano
            print(f"¡Atacaste al enemigo por {dano} puntos de daño!")

        elif opcion == "2":
            print("Ráfaga Veloz")
            for i in range(3):
                vida_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

        elif opcion == "3":
            if posion_vida > 0:
                vida_gladiador += 30
                posion_vida -= 1
                print("Te curaste 30 de vida")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False  # CAMBIO DE TURNO

    else:
        # TURNO DEL ENEMIGO
        print("Turno del enemigo...")
        vida_gladiador -= dano_base_del_enemigo
        print(f"¡El enemigo te atacó por {dano_base_del_enemigo} puntos de daño!")

        turno_gladiador = True  # VUELVE AL JUGADOR

#SALIDA
if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate")