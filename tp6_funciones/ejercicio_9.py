# Práctico 6 - Ejercicio 9: Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit (F = C * 9/5 + 32)."""
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    c = float(input("Ingrese la temperatura en grados Celsius: "))
    f = celsius_a_fahrenheit(c)
    print(f"{c}°C equivalen a {f:.2f}°F")
