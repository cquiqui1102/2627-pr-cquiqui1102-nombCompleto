# Desarrolla un programa en Python que solicite el nombre, el primer apellido y el segundo apellido de una persona y muestre su nombre completo correctamente formateado.

def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea el nombre completo del usuario para separar por espacio y la primera letra en mayúscula.

    Args:
    nombre = Nombre del usuario
    apellido1 = Primer apellido del usuario
    apellido2 = Segundo apellido del usuario

    Returns:
    str = Nombre completo formateado

    """

    nombre_compuesto: str = nombre.strip().split()

    if len(nombre_compuesto) == 1:
        nombre_formateado: str = nombre_compuesto[0].capitalize()
    else:
        nombre_formateado: str = nombre_compuesto[0].capitalize() + " " + nombre_compuesto[1].capitalize()

    apellido1_formateado: str = apellido1.strip().capitalize()

    apellido2_formateado: str = apellido2.strip().capitalize()

    return (f"Su nombre completo es {nombre_formateado} {apellido1_formateado} {apellido2_formateado}.")



def main():
    """
    Función principal
    
    Args:
    Nombre del usuario
    Primer apellido del usuario
    Segundo apellido del usuario

    Returns:
    Nombre completo separado por espacios y primeras letras en mayúsculas
    
    """

    # Entrada

    nombre: str = input("Introduzca su nombre: ")
    apellido1: str = input("Introduzca su primer apellido: ")
    apellido2: str = input("Introduzca su segundo apellido: ")

    # Salida
    
    print(formatear_nombre(nombre, apellido1, apellido2))

if __name__ == "__main__":
    main()