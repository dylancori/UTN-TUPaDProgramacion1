# Práctico 6 - Ejercicio 10: Calcular promedio

def calcular_promedio(a, b, c):
    """Recibe tres números y devuelve su promedio."""
    return (a + b + c) / 3


if __name__ == "__main__":
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    
    prom = calcular_promedio(n1, n2, n3)
    print(f"El promedio es: {prom:.2f}")
