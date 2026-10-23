# Práctico 6 - Ejercicio 2: Saludar usuario

def saludar_usuario(nombre):
    """Recibe un nombre como parámetro y devuelve un saludo personalizado."""
    return f"Hola {nombre}!"


if __name__ == "__main__":
    nombre_usuario = input("Ingrese su nombre: ").strip()
    print(saludar_usuario(nombre_usuario))
