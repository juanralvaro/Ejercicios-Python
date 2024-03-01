""" Crea un programa en Python que solicite al usuario introducir la temperatura en grados Celsius. Luego, realiza la conversión de esta temperatura a grados Fahrenheit utilizando la fórmula:

F=9/5⋅C+32

Donde *F* es la temperatura en grados Fahrenheit y *C* es la temperatura en grados Celsius.

Finalmente, muestra el resultado de la temperatura en ambas escalas. Utiliza f-strings para formatear la salida y muestra la temperatura en grados Fahrenheit con dos decimales. """

# Programa de Conversión de Temperatura
print("¡Bienvenido al Programa de Conversión de Temperatura!\n")

# Entrada de datos
temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Conversión a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Mostrar resultados
print(f"\nTemperatura en grados Celsius: {temperatura_celsius}")
print(f"Temperatura en grados Fahrenheit: {temperatura_fahrenheit:.2f}")