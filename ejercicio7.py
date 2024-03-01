""" Crea un programa en Python que solicite al usuario introducir la temperatura en grados Celsius. Luego, realiza la conversión de esta temperatura a grados Fahrenheit utilizando la fórmula:

F=9/5⋅C+32

Donde *F* es la temperatura en grados Fahrenheit y *C* es la temperatura en grados Celsius.

Finalmente, muestra el resultado de la temperatura en ambas escalas. Utiliza f-strings para formatear la salida y muestra la temperatura en grados Fahrenheit con dos decimales. """

print("Bienvenido al conversor de grados Celsius en grados Fahrenheit.")

temperatura_celsius = int(input("Introduzca la temperatura en grados Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9 / 5 +  32)
fahrenheit_dos_decimales = "{:.2f}".format(temperatura_fahrenheit)

print(f"La temperatura en grados Celsius es", temperatura_celsius)
print(f"La temperatura en grados Farenheit es", fahrenheit_dos_decimales)