# Práctico 6 - Ejercicio 8: Calcular IMC

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC = peso / altura^2)."""
    return peso / (altura ** 2)


if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros (ej: 1.75): "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
