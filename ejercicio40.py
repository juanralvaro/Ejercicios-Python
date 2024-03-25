""" Crea un programa en Python que solicite al usuario ingresar dos números enteros positivos, **`inicio`** y **`fin`**, donde **`inicio`** sea menor que **`fin`**. El programa deberá imprimir todos los números pares en el rango desde **`inicio`** hasta **`fin`**, ambos inclusive. Si no hay números pares en el rango dado, el programa debe imprimir un mensaje indicando que no se encontraron números pares. ¡¡Rápido, rápido..!!

1. Solicitar al usuario que ingrese el número inicial del rango y almacenarlo en la variable **`inicio`**.
2. Solicitar al usuario que ingrese el número final del rango y almacenarlo en la variable **`fin`**.
3. Verificar si **`inicio`** es menor o igual que **`fin`** y si ambos son números positivos. Si no lo son, mostrar un mensaje de error y volver al paso 1.
4. Utilizar un bucle **`for`** y la función **`range()`** para iterar sobre los números en el rango desde **`inicio`** hasta **`fin`**, inclusive.
5. Dentro del bucle, verificar si cada número es par utilizando un condicional **`if`** y el operador **`%`**. Si un número es par, imprimirlo.
6. Si no se encuentran números pares en el rango, imprimir un mensaje indicando que no se encontraron números pares. """

#1
inicio = int(input("Introduce el primer número: "))

#2
fin = int(input("Introduce el segundo número: "))

#3
if inicio <= fin and inicio > 0 and fin > 0:
    print("Inicio es menor o igual que fin.")
else:
    print("Error, vuelva al paso 1.")

#4
for i in range(inicio, fin):
#5
    if i % 2 == 0 :
        print(i)
    elif i % 2 == 1:
        print("No es par")
#6    
    else:
        print("No hay números pares en el rango")