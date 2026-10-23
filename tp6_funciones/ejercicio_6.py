# Práctico 6 - Ejercicio 6: Tabla de multiplicar

def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número del 1 al 10."""
    print(f"\n--- Tabla del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


if __name__ == "__main__":
    num = int(input("Ingrese un número para ver su tabla: "))
    tabla_multiplicar(num)
