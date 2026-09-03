# Práctico 5 - Ejercicio 3: Eliminar elemento de una lista
frutas = ["manzana", "banana", "naranja", "pera"]
print("Lista original:", frutas)

fruta_a_eliminar = "banana"
if fruta_a_eliminar in frutas:
    frutas.remove(fruta_a_eliminar)

print(f"Lista tras eliminar '{fruta_a_eliminar}':", frutas)
