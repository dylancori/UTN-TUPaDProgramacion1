# Práctico 5 - Ejercicio 12: Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]

print("Lista completa:", numeros)
print("Solo pares:", pares)
