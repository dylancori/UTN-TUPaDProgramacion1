# TP Integrador 1 - Ejercicio 4: La Bóveda del Tesoro

matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("=== La Bóveda del Tesoro ===")
for fila in matriz:
    print(fila)

fila = int(input("\nIngrese número de fila (0-2): "))
columna = int(input("Ingrese número de columna (0-2): "))

if 0 <= fila <= 2 and 0 <= columna <= 2:
    print(f"El valor en la posición [{fila}][{columna}] es: {matriz[fila][columna]}")
else:
    print("Coordenadas fuera de rango.")
