# Práctico 6 - Ejercicio 7: Operaciones básicas

def operaciones_basicas(a, b):
    """Devuelve una tupla con suma, resta, multiplicación y división."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)


if __name__ == "__main__":
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    
    resultados = operaciones_basicas(n1, n2)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    
    if resultados[3] is not None:
        print(f"División: {resultados[3]:.2f}")
    else:
        print("División: No se puede dividir por cero.")
