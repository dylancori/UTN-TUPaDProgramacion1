# Práctico 6 - Ejercicio 3: Información personal

def informacion_personal(nombre, apellido, edad, residencia):
    """Recibe cuatro parámetros e imprime un mensaje con los datos personales."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


if __name__ == "__main__":
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    edad = input("Edad: ").strip()
    residencia = input("Residencia: ").strip()
    informacion_personal(nombre, apellido, edad, residencia)
