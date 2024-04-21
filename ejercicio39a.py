""" VERSIÓN A
Escribe un programa en Python que solicite al usuario ingresar su edad y luego determine en qué rango de edad se encuentra. El programa debe seguir los siguientes pasos:

Solicitar al usuario que ingrese su edad como un número entero.
Utilizar un condicional if para evaluar la edad ingresada y mostrar un mensaje dependiendo del rango de edad:
Si la edad está entre 0 y 12 años (inclusive), mostrar el mensaje "Eres un niño".
Si la edad está entre 13 y 19 años (inclusive), mostrar el mensaje "Eres un adolescente".
Si la edad está entre 20 y 64 años (inclusive), mostrar el mensaje "Eres un adulto".
Si la edad es 65 o mayor, mostrar el mensaje "Eres un adulto mayor".
Mostrar el mensaje correspondiente al rango de edad detectado. """

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 20:
    print("Eres un adolescente.")
elif edad >= 20 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")