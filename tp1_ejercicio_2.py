# TP Integrador 1 - Ejercicio 2: El Menú del Campus

menu_semanal = ["Milanesa", "Pastas", "Guiso", "Tacos", "Hamburguesa"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

print("=== Menú Semanal del Campus ===")
for dia, plato in zip(dias, menu_semanal):
    print(f"{dia}: {plato}")

modificar = input("\n¿Desea cambiar el plato de algún día? (s/n): ").lower()
if modificar == "s":
    dia_cambiar = input("Ingrese el día a modificar: ").capitalize()
    if dia_cambiar in dias:
        pos = dias.index(dia_cambiar)
        nuevo_plato = input(f"Ingrese el nuevo plato para el {dia_cambiar}: ")
        menu_semanal[pos] = nuevo_plato
        print(f"Menú actualizado. El {dia_cambiar} ahora se sirve {nuevo_plato}.")
    else:
        print("Día no válido.")
