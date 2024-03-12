"""Ejercicio de andar por casa

Crea una colección de datos inmutable que me permita añadir los siguientes datos de usuario:
-Nombre y apellidos
-Edad
-Lugar de nacimiento
-Ciudad de residencia

tupla_datos = (str(input("Nombre y apellidos: ")),int(input("Edad: ")),str(input("Lugar de nacimiento: ")),str(input("Ciudad de residencia: ")))
print(tupla_datos) """

tupla_andar_casa = ["nombre", "apellidos"], [0], ["ciudad_residencia"], ["ciudad_nacimiento"]

tupla_andar_casa[0][0] = str(input("Introduce un nombre: "))
tupla_andar_casa[0][1] = str(input("Introduce un apellido: "))
tupla_andar_casa[1][0] = int(input("Introduce una edad: "))
tupla_andar_casa[2][0] = str(input("Introduce una ciudad de residencia: "))
tupla_andar_casa[3][0] = str(input("Introduce una ciudad de nacimiento: "))

print(tupla_andar_casa)