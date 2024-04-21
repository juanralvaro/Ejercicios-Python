""" - 10- Programa de información personal (WeekEnd)
    
    Crea un programa en Python que solicite al usuario ingresar su información personal, incluyendo su nombre, edad y ciudad de residencia. Luego, utiliza la función **`print()`** para mostrar un mensaje personalizado utilizando diferentes métodos de formateo de cadenas.
    
    1. Solicita al usuario que introduzca su nombre.
    2. Solicita al usuario que introduzca su edad.
    3. Solicita al usuario que introduzca su ciudad de residencia.
    
    Luego, muestra un mensaje de saludo personalizado que incluya la información ingresada. Utiliza tanto la función **`.format()`** como las f-strings para formatear la salida de la siguiente manera:
    
    - En el primer mensaje, utiliza **`.format()`** para incluir el nombre y la ciudad.
    - En el segundo mensaje, utiliza una f-string para incluir la edad.
    
    *Ejemplo de salida:* 
    
    *¡Bienvenido al Programa de Información Personal!*
    
    *Introduce tu nombre: Juan
    Introduce tu edad: 30
    Introduce tu ciudad de residencia: Ciudad Paraíso*
    
    *¡Hola, Juan! Bienvenido a Ciudad Paraíso.
    Esperamos que disfrutes tu estudio. Tienes 30 años de sabiduría.* """

print("¡Bienvenido al programa de información personal de la Universidad de Málaga!")
nombre = str(input("\nIntroduce tu nombre: "))
edad = int(input("\nIntroduce tu edad: "))
ciudad_de_residencia = str(input("\nIntroduce tu ciudad de residencia: "))

print("\n¡Hola, {}, de {}! Bienvenido a la Universidad de Málaga.".format(nombre, ciudad_de_residencia))
print(f"\nDisfruta estudiando aquí. Sólo tienes {edad} años y toda una vida por delante.")