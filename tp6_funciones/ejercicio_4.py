# Práctico 6 - Ejercicio 4: Área y perímetro de un círculo

def calcular_area_circulo(radio):
    """Calcula y devuelve el área del círculo usando pi = 3.14."""
    return 3.14 * (radio ** 2)


def calcular_perimetro_circulo(radio):
    """Calcula y devuelve el perímetro del círculo usando pi = 3.14."""
    return 2 * 3.14 * radio


if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio)}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio)}")
