""" VERSIÓN B - Versión compleja
Solicitar al usuario que ingrese la cantidad de personas cuyas edades desea evaluar.
Utilizar un bucle for para iterar sobre cada persona y solicitar su edad.
Utilizar un condicional if dentro del bucle para evaluar la edad de cada persona y mostrar un mensaje dependiendo del rango de edad:
Si la edad está entre 0 y 12 años (inclusive), mostrar el mensaje "Eres un niño".
Si la edad está entre 13 y 19 años (inclusive), mostrar el mensaje "Eres un adolescente".
Si la edad está entre 20 y 64 años (inclusive), mostrar el mensaje "Eres un adulto".
Si la edad es 65 o mayor, mostrar el mensaje "Eres un adulto mayor".
Mostrar el mensaje correspondiente al rango de edad detectado para cada persona. """

numero_personas = int(input("Introduzca el número de personas a consultar edad: "))

for persona in range(numero_personas):
    edad = int(input(f"Ingrese la edad de la persona {persona+1}: "))
    if edad >= 0 and edad < 13:
        print("Es un niño.")
    elif edad >= 13 and edad < 20:
        print("Es un adolescente.")
    elif edad >= 20 and edad < 65:
        print("Es un adulto.")
    else:
        print("Es un adulto mayor.")