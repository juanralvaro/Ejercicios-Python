""" Crea 3 diccionarios, utilizando las 3 versiones para crear diccionarios que hemos visto en clase (sintaxis básica, y las dos versiones del método de constructor dict() ). Rellena los datos de cada diccionario con información que luego pediremos al usuario que actualice.

1. El primer diccionario incluirá los datos básicos del usuario: Nombre, apellidos, fecha de nacimiento, ciudad de nacimiento, nombre del padre y nombre de la madre.
2. El segundo diccionario incluirá: Nº de DNI, fecha de expedición y fecha de caducidad
3. El tercer diccionario: Nacionalidad y domicilio.

A continuación realizaremos las siguientes operaciones:

1. Mostraremos los datos antiguos del diccionario.
2. El programa le pedirá al usuario que actualice los datos uno a uno utilizando la función **`input()`**
3. Por último le mostraremos al usuario los datos actualizados de los 3 diccionarios. """

#Creación diccionarios:
diccionario_uno = {
    "Nombre": 'Juan Raimundo',
    "Apellidos": 'Álvaro Núñez',
    "Fecha de nacimiento": '16-12-1981',
    "Ciudad de nacimiento": 'Betanzos',
    "Nombre del padre": 'Ángel',
    "Nombre de la madre": 'María de las Ermitas'
}

diccionario_dos = dict([
    ("Número de DNI sin letra", 47356660),
    ("Letra del DNI", "M"),
    ("Fecha de expedición", "16-06-2015"),
    ("Fecha de caducidad", "16-06-2025")
])

diccionario_tres = dict(
    Nacionalidad="Española",
    Domicilio="C/ Rosalía de Castro, 8, 4º Izq."
)

#1. Mostramos datos antiguos del diccionario
print(diccionario_uno)
print(diccionario_dos)
print(diccionario_tres)

#2. Actualización de datos uno a uno con input

diccionario_uno["Nombre"]= str(input("Introduzca el nuevo nombre: "))
diccionario_uno["Apellidos"]= str(input("Introduzca los nuevos apellidos: "))
diccionario_uno["Fecha de nacimiento"]= str(input("Introduzca la nueva fecha de nacimiento: "))
diccionario_uno["Ciudad de nacimiento"]= str(input("Introduzca la nueva ciudad de nacimiento: "))
diccionario_uno["Nombre del padre"]= str(input("Introduzca el nuevo nombre del padre: "))
diccionario_uno["Nombre de la madre"]= str(input("Introduzca el nuevo nombre de la madre: "))
diccionario_dos["Número de DNI sin letra"] = int(input("Introduzca el nuevo número del DNI: "))
diccionario_dos["Letra del DNI"] = str(input("Introduzca la nueva letra del DNI: "))
diccionario_dos["Fecha de expedición"] = str(input("Introduzca la nueva fecha de expedición: "))
diccionario_dos["Fecha de caducidad"] = str(input("Introduzca la nueva fecha de caducidad: "))
diccionario_tres["Nacionalidad"] = str(input("Introduzca la nueva nacionalidad: "))
diccionario_tres["Domicilio"] = str(input("Introduzca el nuevo domicilio: "))

#3. Diccionarios actualizados
print(diccionario_uno)
print(diccionario_dos)
print(diccionario_tres)