# Práctico 6 - Ejercicio 5: Segundos a horas

def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas con decimales."""
    return segundos / 3600


if __name__ == "__main__":
    segundos = float(input("Ingrese la cantidad de segundos: "))
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")
