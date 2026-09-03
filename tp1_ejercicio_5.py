# TP Integrador 1 - Ejercicio 5: La Arena de Batalla

jugadores = []

num_jugadores = int(input("¿Cuántos jugadores ingresarán a la arena?: "))

for i in range(num_jugadores):
    nombre = input(f"Nombre del jugador {i+1}: ")
    puntos = int(input(f"Puntaje de {nombre}: "))
    jugadores.append((nombre, puntos))

# Ordenar por puntaje de mayor a menor
jugadores.sort(key=lambda x: x[1], reverse=True)

print("\n=== Tabla de Posiciones ===")
for pos, (nombre, puntos) in enumerate(jugadores, start=1):
    print(f"{pos}. {nombre} - {puntos} pts")
