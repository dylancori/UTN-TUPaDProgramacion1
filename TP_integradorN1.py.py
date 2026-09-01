# TP INTEGRADOR - PROGRAMACION 1

def pedir_nombre(mensaje):
    nombre = input(mensaje).strip()
    while nombre == "" or not nombre.isalpha():
        print("Error: Solo se permiten letras.")
        nombre = input(mensaje).strip()
    return nombre


def pedir_entero_positivo(mensaje):
    dato = input(mensaje).strip()
    while not dato.isdigit() or int(dato) <= 0:
        print("Error: ingrese un numero entero positivo.")
        dato = input(mensaje).strip()
    return int(dato)


def pedir_opcion_1_2(mensaje):
    dato = input(mensaje).strip().lower()
    while dato != "s" and dato != "n":
        print("Error: ingrese S o N.")
        dato = input(mensaje).strip().lower()
    return dato


# ============================================================
# EJERCICIO 1 - CAJA DEL KIOSCO
# ============================================================

def ejercicio_1():
    print("\n=== EJERCICIO 1 - CAJA DEL KIOSCO ===")

    cliente = pedir_nombre("Nombre del cliente: ")
    cantidad = pedir_entero_positivo("Cantidad de productos: ")

    total_sin_descuentos = 0
    total_con_descuentos = 0

    for i in range(1, cantidad + 1):
        precio = pedir_entero_positivo(f"Producto {i} - Precio: ")
        descuento = pedir_opcion_1_2("Descuento (S/N): ")

        total_sin_descuentos += precio

        if descuento == "s":
            precio_final = precio * 0.90
        else:
            precio_final = precio

        total_con_descuentos += precio_final

    ahorro = total_sin_descuentos - total_con_descuentos
    promedio = total_con_descuentos / cantidad

    print("\n--- RESUMEN ---")
    print(f"Cliente: {cliente}")
    print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
    print(f"Total con descuentos: ${total_con_descuentos:.2f}")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")


# ============================================================
# EJERCICIO 2 - ACCESO AL CAMPUS Y MENU SEGURO
# ============================================================

def ejercicio_2():
    print("\n=== EJERCICIO 2 - ACCESO AL CAMPUS ===")

    usuario_correcto = "alumno"
    clave_correcta = "python123"

    acceso = False
    intentos = 0

    while intentos < 3 and not acceso:
        intentos += 1

        usuario = input(f"Intento {intentos}/3 - Usuario: ")
        clave = input("Clave: ")

        if usuario == usuario_correcto and clave == clave_correcta:
            acceso = True
            print("Acceso concedido.")
        else:
            print("Error: credenciales inválidas.")

    if not acceso:
        print("Cuenta bloqueada.")
        return

    salir = False

    while not salir:
        print("\n1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ").strip()

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ").strip()

        opcion = int(opcion)

        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ").strip()

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ").strip()

            opcion = int(opcion)

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirmar nueva clave: ")

            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmar nueva clave: ")

            clave_correcta = nueva_clave
            print("Clave cambiada correctamente.")

        elif opcion == 3:
            print("¡Seguí adelante, cada línea de código te acerca a tu objetivo!")

        elif opcion == 4:
            print("Sesión finalizada.")
            salir = True


# ============================================================
# EJERCICIO 3 - AGENDA DE TURNOS SIN LISTAS
# ============================================================

def ejercicio_3():
    print("\n=== EJERCICIO 3 - AGENDA DE TURNOS ===")

    operador = pedir_nombre("Nombre del operador: ")

    # Lunes tiene 4 espacios
    lunes1 = ""
    lunes2 = ""
    lunes3 = ""
    lunes4 = ""

    # Martes tiene 3 espacios
    martes1 = ""
    martes2 = ""
    martes3 = ""

    salir = False

    while not salir:
        print(f"\n--- Agenda de {operador} ---")
        print("1. Reservar turno")
        print("2. Cancelar turno")
        print("3. Ver agenda del día")
        print("4. Ver resumen general")
        print("5. Cerrar sistema")

        opcion = input("Opción: ").strip()

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Opción: ").strip()

        opcion = int(opcion)

        # ---------------- RESERVAR ----------------
        if opcion == 1:
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                if not dia.isdigit():
                    print("Error: ingrese un número válido.")
                else:
                    print("Error: elija 1 o 2.")
                dia = input("Día (1=Lunes, 2=Martes): ").strip()

            dia = int(dia)
            paciente = pedir_nombre("Nombre del paciente: ")

            if dia == 1:
                repetido = (
                    paciente.lower() == lunes1.lower() or
                    paciente.lower() == lunes2.lower() or
                    paciente.lower() == lunes3.lower() or
                    paciente.lower() == lunes4.lower()
                )

                if repetido:
                    print("Error: el paciente ya tiene un turno ese día.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado correctamente. Turno 1.")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado correctamente. Turno 2.")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado correctamente. Turno 3.")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado correctamente. Turno 4.")
                else:
                    print("No hay cupos disponibles para el lunes.")

            else:
                repetido = (
                    paciente.lower() == martes1.lower() or
                    paciente.lower() == martes2.lower() or
                    paciente.lower() == martes3.lower()
                )

                if repetido:
                    print("Error: el paciente ya tiene un turno ese día.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado correctamente. Turno 1.")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado correctamente. Turno 2.")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado correctamente. Turno 3.")
                else:
                    print("No hay cupos disponibles para el martes.")

        # ---------------- CANCELAR ----------------
        elif opcion == 2:
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                if not dia.isdigit():
                    print("Error: ingrese un número válido.")
                else:
                    print("Error: elija 1 o 2.")
                dia = input("Día (1=Lunes, 2=Martes): ").strip()

            dia = int(dia)
            paciente = pedir_nombre("Nombre del paciente: ")
            encontrado = False

            if dia == 1:
                if paciente.lower() == lunes1.lower() and lunes1 != "":
                    lunes1 = ""
                    encontrado = True
                elif paciente.lower() == lunes2.lower() and lunes2 != "":
                    lunes2 = ""
                    encontrado = True
                elif paciente.lower() == lunes3.lower() and lunes3 != "":
                    lunes3 = ""
                    encontrado = True
                elif paciente.lower() == lunes4.lower() and lunes4 != "":
                    lunes4 = ""
                    encontrado = True
            else:
                if paciente.lower() == martes1.lower() and martes1 != "":
                    martes1 = ""
                    encontrado = True
                elif paciente.lower() == martes2.lower() and martes2 != "":
                    martes2 = ""
                    encontrado = True
                elif paciente.lower() == martes3.lower() and martes3 != "":
                    martes3 = ""
                    encontrado = True

            if encontrado:
                print("Turno cancelado correctamente.")
            else:
                print("No se encontró un turno para ese paciente.")

        # ---------------- VER AGENDA ----------------
        elif opcion == 3:
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                if not dia.isdigit():
                    print("Error: ingrese un número válido.")
                else:
                    print("Error: elija 1 o 2.")
                dia = input("Día (1=Lunes, 2=Martes): ").strip()

            dia = int(dia)

            if dia == 1:
                print("\n--- LUNES ---")
                if lunes1 == "":
                    print("Turno 1: (libre)")
                else:
                    print(f"Turno 1: {lunes1}")

                if lunes2 == "":
                    print("Turno 2: (libre)")
                else:
                    print(f"Turno 2: {lunes2}")

                if lunes3 == "":
                    print("Turno 3: (libre)")
                else:
                    print(f"Turno 3: {lunes3}")

                if lunes4 == "":
                    print("Turno 4: (libre)")
                else:
                    print(f"Turno 4: {lunes4}")

            else:
                print("\n--- MARTES ---")
                if martes1 == "":
                    print("Turno 1: (libre)")
                else:
                    print(f"Turno 1: {martes1}")

                if martes2 == "":
                    print("Turno 2: (libre)")
                else:
                    print(f"Turno 2: {martes2}")

                if martes3 == "":
                    print("Turno 3: (libre)")
                else:
                    print(f"Turno 3: {martes3}")

        # ---------------- RESUMEN ----------------
        elif opcion == 4:
            ocupados_lunes = 0
            disponibles_lunes = 0

            if lunes1 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1

            if lunes2 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1

            if lunes3 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1

            if lunes4 == "":
                disponibles_lunes += 1
            else:
                ocupados_lunes += 1

            ocupados_martes = 0
            disponibles_martes = 0

            if martes1 == "":
                disponibles_martes += 1
            else:
                ocupados_martes += 1

            if martes2 == "":
                disponibles_martes += 1
            else:
                ocupados_martes += 1

            if martes3 == "":
                disponibles_martes += 1
            else:
                ocupados_martes += 1

            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} disponibles.")
            print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles.")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print("Día con más turnos: empate.")

        elif opcion == 5:
            print("Sistema cerrado.")
            salir = True


# ============================================================
# EJERCICIO 4 - ESCAPE ROOM: LA BOVEDA
# ============================================================

def ejercicio_4():
    print("\n=== EJERCICIO 4 - ESCAPE ROOM: LA BOVEDA ===")

    agente = pedir_nombre("Nombre del agente: ")

    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    forzadas_seguidas = 0

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

        print("\n--------------------------------")
        print(f"Agente: {agente}")
        print(f"Energía: {energia}")
        print(f"Tiempo: {tiempo}")
        print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
        print(f"Alarma: {'ON' if alarma else 'OFF'}")
        print("--------------------------------")

        print("1. Forzar cerradura")
        print("2. Hackear panel")
        print("3. Descansar")

        opcion = input("Opción: ").strip()

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Opción: ").strip()

        opcion = int(opcion)

        # ---------------- FORZAR CERRADURA ----------------
        if opcion == 1:
            energia -= 20
            tiempo -= 2
            forzadas_seguidas += 1

            print("Intentás forzar la cerradura...")

            if forzadas_seguidas == 3:
                alarma = True
                print("¡La cerradura se trabó! ¡ALARMA ACTIVADA!")
            else:
                if energia < 40:
                    riesgo = input("Riesgo de alarma. Elegí un número del 1 al 3: ").strip()

                    while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                        print("Error: ingrese un número del 1 al 3.")
                        riesgo = input("Elegí un número del 1 al 3: ").strip()

                    riesgo = int(riesgo)

                    if riesgo == 3:
                        alarma = True
                        print("¡Elegiste 3! ¡ALARMA ACTIVADA!")
                    else:
                        cerraduras_abiertas += 1
                        print("¡Cerradura abierta!")

                else:
                    cerraduras_abiertas += 1
                    print("¡Cerradura abierta!")

        # ---------------- HACKEAR PANEL ----------------
        elif opcion == 2:
            energia -= 10
            tiempo -= 3
            forzadas_seguidas = 0

            print("Iniciando hackeo...")

            for paso in range(1, 5):
                print(f"Paso {paso}/4 - Progreso...")
                codigo_parcial += "A"

            print(f"Código parcial: {codigo_parcial}")

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código completo! Se abrió una cerradura.")

        # ---------------- DESCANSAR ----------------
        elif opcion == 3:
            energia += 15

            if energia > 100:
                energia = 100

            tiempo -= 1
            forzadas_seguidas = 0

            if alarma:
                energia -= 10
                print("La alarma está activa: perdés 10 de energía extra.")

            print("Descansaste.")

        # Bloqueo especial por alarma
        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            print("¡La alarma bloqueó el sistema!")
            break

    print("\n=== RESULTADO ===")

    if cerraduras_abiertas == 3:
        print("¡VICTORIA! Abriste las 3 cerraduras y escapaste de la bóveda.")
    elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("DERROTA. La bóveda quedó bloqueada por la alarma.")
    elif energia <= 0 or tiempo <= 0:
        print("DERROTA. Te quedaste sin energía o sin tiempo.")
    else:
        print("DERROTA. No pudiste abrir la bóveda.")


# ============================================================
# EJERCICIO 5 - ESCAPE ROOM: LA ARENA DEL GLADIADOR
# ============================================================

def ejercicio_5():
    print("\n=== EJERCICIO 5 - LA ARENA DEL GLADIADOR ===")
    print("--- BIENVENIDO A LA ARENA ---")

    nombre = pedir_nombre("Nombre del Gladiador: ")

    vida_jugador = 100
    vida_enemigo = 100
    pociones = 3
    ataque_pesado = 15
    dano_enemigo = 12
    turno_gladiador = True

    print("\n=== INICIO DEL COMBATE ===")

    while vida_jugador > 0 and vida_enemigo > 0:

        if turno_gladiador:
            print("\n--------------------------------")
            print(
                f"{nombre} (HP: {vida_jugador}) vs "
                f"Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}"
            )
            print("--------------------------------")

            print("Elige acción:")
            print("1. Ataque Pesado")
            print("2. Ráfaga Veloz")
            print("3. Curar")

            opcion = input("Opción: ").strip()

            while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
                if not opcion.isdigit():
                    print("Error: Ingrese un número válido.")
                else:
                    print("Error: opción fuera de rango.")
                opcion = input("Opción: ").strip()

            opcion = int(opcion)

            # Ataque pesado
            if opcion == 1:
                dano = float(ataque_pesado)

                if vida_enemigo < 20:
                    dano = ataque_pesado * 1.5
                    print("¡GOLPE CRÍTICO!")

                vida_enemigo -= dano
                print(f"¡Atacaste al enemigo por {dano:.1f} puntos de daño!")

            # Ráfaga veloz
            elif opcion == 2:
                print(">> ¡Inicias una ráfaga de golpes!")

                for golpe in range(3):
                    if vida_enemigo > 0:
                        vida_enemigo -= 5
                        print("> Golpe conectado por 5 de daño")

            # Curar
            elif opcion == 3:
                if pociones > 0:
                    vida_jugador += 30

                    if vida_jugador > 100:
                        vida_jugador = 100

                    pociones -= 1
                    print("¡Usaste una poción y recuperaste vida!")
                else:
                    print("¡No quedan pociones!")

            # Si el enemigo sigue vivo, ataca.
            if vida_enemigo > 0:
                vida_jugador -= dano_enemigo
                print(f"¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

            turno_gladiador = True

    print("\n=== FIN DEL JUEGO ===")

    if vida_jugador > 0:
        print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
    else:
        print("DERROTA. Has caído en combate.")


# ============================================================
# MENU PRINCIPAL PARA PROBAR LOS EJERCICIOS
# ============================================================

def main():
    salir = False

    while not salir:
        print("\n================================================")
        print("        TP INTEGRADOR - PROGRAMACIÓN 1")
        print("================================================")
        print("1. Caja del Kiosco")
        print("2. Acceso al Campus y Menú Seguro")
        print("3. Agenda de Turnos")
        print("4. Escape Room: La Bóveda")
        print("5. Escape Room: La Arena del Gladiador")
        print("6. Salir")

        opcion = input("Seleccione un ejercicio: ").strip()

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Seleccione un ejercicio: ").strip()

        opcion = int(opcion)

        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        elif opcion == 6:
            print("Programa finalizado.")
            salir = True


main()
