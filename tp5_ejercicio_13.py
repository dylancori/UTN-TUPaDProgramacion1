# Práctico 5 - Ejercicio 13: Eliminar duplicados manteniendo orden
lista_duplicada = [1, 2, 2, 3, 4, 4, 5, 1]
sin_duplicados = []

for item in lista_duplicada:
    if item not in sin_duplicados:
        sin_duplicados.append(item)

print("Original con duplicados:", lista_duplicada)
print("Sin duplicados:", sin_duplicados)
