# TP Integrador 1 - Ejercicio 3: Sistema de Turnos

turnos = []

while True:
    print("\n=== Sistema de Turnos ===")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. Ver lista de espera")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        turnos.append(nombre)
        print(f"Paciente {nombre} agregado a la lista.")
    elif opcion == "2":
        if turnos:
            atendido = turnos.pop(0)
            print(f"Atendiendo a: {atendido}")
        else:
            print("No hay pacientes en espera.")
    elif opcion == "3":
        print("Lista actual:", turnos)
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
