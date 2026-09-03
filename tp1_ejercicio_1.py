# TP Integrador 1 - Ejercicio 1: La Caja del Kiosco

compras = []

print("=== La Caja del Kiosco ===")
while True:
    monto = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    if monto == 0:
        break
    compras.append(monto)

if compras:
    total = sum(compras)
    promedio = total / len(compras)
    maximo = max(compras)
    minimo = min(compras)

    print("\n--- Resultados ---")
    print(f"Total recaudado: ${total:.2f}")
    print(f"Monto promedio: ${promedio:.2f}")
    print(f"Compra más alta: ${maximo:.2f}")
    print(f"Compra más baja: ${minimo:.2f}")
else:
    print("No se ingresaron compras.")
