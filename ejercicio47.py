#Práctica rápida 1: crear un programa que le solicite al usuario su nombre y sus apellidos. A continuación, el programa ejecutará una función saludar() para saludar al usuario.
#Práctica rápida 2: solicitamos el año de nacimiento, y a continuación el usuario le dirá al programa los años que tiene.

nombre = str(input("Introduzca su nombre: "))
apellidos = str(input("Introduzca sus apellidos: "))

def saludar():
    print(f"¡Hola, {nombre} {apellidos}!")

saludar()

anio_nacimiento = int(input("Introduzca su año de nacimiento: "))

def edad():
    print(f"Usted tiene {2024 - anio_nacimiento} años de edad.")
edad()

""" EJERCICIO 1 


def saludar(nombre):  # 'nombre' es un parámetro de la función
    print("¡Hola,", nombre, "!")

# Pedimos al usuario que introduzca su nombre
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Llamamos a la función 'saludar' y le pasamos el nombre del usuario como argumento
saludar(nombre_usuario) """

""" EJERCICIO 2 

def calcular_edad():
    # Solicitar al usuario su año de nacimiento
    anio_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: \n"))
    anio_actual = int(input("Por favor, ingresa el año actual:\n"))
    # Calcular la edad restando el año de nacimiento al año actual
    edad = anio_actual - anio_nacimiento
    
    # Devolver la edad calculada
    return edad

# Llamar a la función para calcular la edad del usuario
edad_usuario = calcular_edad()

# Mostrar la edad calculada
print("Tienes", edad_usuario, "años de edad.")"""

