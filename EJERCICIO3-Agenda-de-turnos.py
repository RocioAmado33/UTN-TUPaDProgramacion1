print("Agenda tu turno\n")

nombre=input("Ingrese su nombre: ")
while not nombre.isalpha():#validacion 
    nombre=input("Ingrese su nombre valido: ")

print("1. Reservar turno\n"
"2. Cancelar turno (por nombre)\n"
"3. Ver agenda del día\n"
"4. Ver resumen general\n"
"5. Cerrar sistema)\n")

opcion=input("Escoge una opcion: ")

lunes1 = lunes2 = lunes3 = lunes4 = ""#variables
martes1 = martes2 = martes3 = ""

while opcion!="5": #condicion de salida
     if opcion.isdigit(): #validacion
        match opcion:#menu
           case "1":
             print("Reservar turno\n")

             dia=input("Elige el dia(1=Lunes, 2=Martes): ")#dia
             while dia not in ("1","2"):#validacion
                dia=input("Ingrese 1 para Lunes o 2 para Martes: ")

             paciente=input("Ingrese su nombre: ")#paciente
             while not paciente.isalpha():#validacion paciente
                paciente=input("Ingrese su nombre valido: ")

             #reserva
             if dia == "1":  # Lunes
                 if paciente in (lunes1, lunes2, lunes3, lunes4):
                   print("El paciente ya tiene turno en Lunes")
                 else:
                   if lunes1 == "":
                     lunes1 = paciente
                   elif lunes2 == "":
                     lunes2 = paciente
                   elif lunes3 == "":
                     lunes3 = paciente
                   elif lunes4 == "":
                     lunes4 = paciente
                   else:
                     print("No hay turnos disponibles en Lunes")

                   if paciente in (lunes1, lunes2, lunes3, lunes4):
                     print(f"Turno reservado para {paciente} el Lunes")
  

             elif dia == "2":  # Martes
                   if paciente in (martes1, martes2, martes3):
                      print("El paciente ya tiene turno en Martes")
                   else:
                      if martes1 == "":
                        martes1 = paciente
                      elif martes2 == "":
                        martes2 = paciente
                      elif martes3 == "":
                        martes3 = paciente
                      else:
                        print("No hay turnos disponibles en Martes")

                   if paciente in (martes1, martes2, martes3):
                      print(f"Turno reservado para {paciente} en Martes")

           case "2":
               print("Cancelar turno")

               cancelacion=input("Elige el dia del turno a cancelar(1=Lunes, 2=Martes): ")
               while cancelacion not in ("1","2"):#validacion
                  cancelacion=input("Elige 1 o 2")

               paciente_c=input("Ingrese su nombre: ")#paciente_c
               while not paciente_c.isalpha():#validacion paciente_c
                  paciente_c=input("Ingrese su nombre valido: ")

                #cancelacion
               if cancelacion == "1":  # Lunes
                    if paciente_c in (lunes1, lunes2, lunes3, lunes4):
                      print("El paciente tiene turno el Lunes")
                      if lunes1 == paciente_c:
                       lunes1 = ""
                      elif lunes2 == paciente_c:
                       lunes2 = ""
                      elif lunes3 == paciente_c:
                       lunes3 = ""
                      elif lunes4 == paciente_c:
                       lunes4 = ""
                      print(f"Turno cancelado para {paciente_c} el Lunes")
                    else:
                     print("El paciente no tiene turno programado el  Lunes")


               elif cancelacion == "2":  # Martes
                   if paciente_c in (martes1, martes2, martes3):
                     print("El paciente tiene turno el Martes")

                     if martes1 == paciente_c:
                        martes1 = ""
                     elif martes2 == paciente_c:
                        martes2 = ""
                     elif martes3 == paciente_c:
                        martes3 = ""
                     print(f"Turno cancelado para {paciente_c} el Martes")
                   
                   else:
                     print("No tiene turno programado el  Martes")

   
                
           case "3":
             print("Ver agenda")

             dia = input("Ver agenda de qué día? (1=Lunes, 2=Martes): ")
             while dia not in ("1","2"):
               dia = input("Ingrese 1 o 2: ")

             if dia == "1":  # Lunes
               print("Turnos del Lunes:")
               print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
               print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
               print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
               print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

             elif dia == "2":  # Martes
               print("Turnos del Martes:")
               print("Turno 1:", martes1 if martes1 != "" else "(libre)")
               print("Turno 2:", martes2 if martes2 != "" else "(libre)")
               print("Turno 3:", martes3 if martes3 != "" else "(libre)")
           case "4":
             print("Resumen")
               # Contar ocupados
             ocupados_lunes = 0
             ocupados_lunes += 1 if lunes1 != "" else 0
             ocupados_lunes += 1 if lunes2 != "" else 0
             ocupados_lunes += 1 if lunes3 != "" else 0
             ocupados_lunes += 1 if lunes4 != "" else 0

             ocupados_martes = 0
             ocupados_martes += 1 if martes1 != "" else 0
             ocupados_martes += 1 if martes2 != "" else 0
             ocupados_martes += 1 if martes3 != "" else 0

              # Mostrar resumen
             print(f"Lunes: {ocupados_lunes} turnos ocupados, {4 - ocupados_lunes} libres")
             print(f"Martes: {ocupados_martes} turnos ocupados, {3 - ocupados_martes} libres")

              # Día con más turnos ocupados
             if ocupados_lunes > ocupados_martes:
               print("Día con más turnos ocupados: Lunes")
             elif ocupados_martes > ocupados_lunes:
               print("Día con más turnos ocupados: Martes")
             else:
               print("Empate en turnos ocupados entre Lunes y Martes")
           case "5":
             print("Salir")
           case _:
             print("Opción inválida")

       
     else:
          print("Ingresá un número válido")

     opcion = input("\nEscoge una opcion: ")

