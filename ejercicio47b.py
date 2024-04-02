""" Crea un programa que solicite al usuario dos números enteros y realice las siguientes operaciones aritméticas utilizando funciones:

1. Suma
2. Resta
3. Multiplicación
4. División

El programa debe mostrar el resultado de cada operación.

1. Solicita al usuario que ingrese dos números enteros.
2. Define una función llamada **`suma`** que tome dos parámetros (los números ingresados) y devuelva la suma de ambos.
3. Define una función llamada **`resta`** que tome dos parámetros y devuelva la resta del primero menos el segundo.
4. Define una función llamada **`multiplicacion`** que tome dos parámetros y devuelva el resultado de multiplicar ambos.
5. Define una función llamada **`division`** que tome dos parámetros y devuelva el resultado de dividir el primero entre el segundo.
6. Llama a cada una de estas funciones con los números ingresados por el usuario como argumentos.
7. Imprime los resultados de cada operación aritmética.

Recuerda agregar comentarios explicativos en tu código para guiar al lector a través de cada paso y función. """

print("Bienvenido al programa de operaciones.")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el primer número: "))

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

suma(num1, num2)
resta(num1, num2)
multiplicacion(num1, num2)
division(num1, num2)
print("\nLa suma es: ", suma(num1, num2), "\nLa resta es: ", resta(num1, num2), "\nLa multiplicación es: ", multiplicacion(num1, num2), "\nLa división es: ", division(num1, num2))