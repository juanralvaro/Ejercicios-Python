""" Crea un programa en Python que simule el registro de gastos y ahorros. Utiliza variables para representar el saldo inicial, solicita al usuario ingresar gastos y ahorros, y utiliza operadores y el método **`append()`** para actualizar la información. Realiza las siguientes operaciones:

1. Pregunta al usuario por su saldo inicial utilizando **`input()`**.
2. Muestra un mensaje de bienvenida y el saldo inicial.
3. Pregunta al usuario por el importe de un gasto y lo resta del saldo.
4. Pregunta al usuario por el importe de un ahorro y lo suma al saldo.
5. Muestra el saldo actualizado y una lista con los gastos y ahorros registrados. """

saldo_inicial = float(input("Introduzca su saldo inicial: "))

print("Bienvenido al simulador de gastos y ahorros.")

gasto1 = float(input("Introduzca su último gasto: "))
saldo_inicial -= gasto1

ahorro1 = float(input("Introduzca su último ahorro: "))
saldo_inicial += ahorro1

gasto2 = float(input("Introduzca su último gasto: "))
saldo_inicial -= gasto2

ahorro2 = float(input("Introduzca su último ahorro: "))
saldo_inicial += ahorro2

gasto3 = float(input("Introduzca su último gasto: "))
saldo_inicial -= gasto3

ahorro3 = float(input("Introduzca su último ahorro: "))
saldo_inicial += ahorro3

lista_ahorros = []
lista_ahorros.append(ahorro1)
lista_ahorros.append(ahorro2)
lista_ahorros.append(ahorro3)

lista_gastos = []
lista_gastos.append(gasto1)
lista_gastos.append(gasto2)
lista_gastos.append(gasto3)

print(f"\nSu saldo actual es {saldo_inicial}.")
print("Lista de gastos: ", lista_gastos)
print("Lista de ahorros: ", lista_ahorros)