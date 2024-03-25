#------------- ESTRUCTURAS DE CONTROL-------------
"""Gracias a las estructuras de control podemos cambiar el flujo de ejecución de un programa"""

#CONDICIONAL IF: Nos permite tomar decisiones basadas en condiciones. Vamos a poder ejecutar un bloque de código si una condición dada para evaluacióne s tomada como verdadera. 
"""
SINTAXIS: 
if condicion:
    #Bloque de código que se va a ejecutar si la condicón evaluada es verdadera
· La expresión que sigue a if debe ser una expresión booleana, algo que pueda ser tomado como verdadero o falso.
· Si la condición es verdadera, se va a ejecutar el bloque de código identado debajo del if. Si la condición es tomada como falsa, el bloque de código del if se omite, y solo se ejecutará el bloque de código dentro de "else" en caso de que exista.
· En este tipo de estructyura solo se ejecutará el primer bloque de código cuya condición sea verdadera. 

· La expresión que sigue a if debe ser una expresión booleana

#Ejemplo

numero = 0
#verificar si el número es positivo o negativo
if numero > 0:
    print("El número es positivo")
else:
    print("El número es menor o igual a cero")
print("Estoy fuera del condicional") #La identación es fundamental para definir el bloque de código que pertene a nuestra estructura de control. En este caso el print que esta fuera se va a ejecutar siempre. """

#Ejercicio al vuelo: analizador de números por entrada

""" print("Bienvenido al analizador de números.")

numero = int(input("Escriba su número a analizar: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
elif numero == -2:
    print("El número es -2.")
else:
    print("El número es cero.")

print("Gracias por usar el analizador de números. ¡Feliz día!") """

# Número par o impar:

""" numero = int(input("Introduzca el número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.") """

#Calculadora Python
    
""" print("Bienvenidx a la calculadora de Python.")

num1 = float(input("\nIntroduzca el primer operador: "))
num2 = float(input("\nIntroduzca el segundo operador: "))

print("\nOperaciones disponibles:")
print("\n1. Suma")
print("\n2. Resta")
print("\n3. Multiplicación")
print("\n4. División")

operacion = int(input("\nSeleccione la operación a implantar: "))

if operacion == 1:
    resultado = num1 + num2
    print("\nEl resultado de la suma es: ",resultado)
elif operacion == 2:
    resultado = num1 - num2
    print("\nEl resultado de la resta es: ",resultado)
elif operacion == 3:
    resultado = num1 * num2
    print("\nEl resultado de la multiplicación es: ",resultado)
elif operacion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("\nEl resultado de la división es: ",resultado)
    else:
        print("\nNo se puede dividir por cero.")
else:
    print("\nOperación no válida. Introduzca el número correcto.")
print("\nGracias por usar la calculadora de Python. ¡Buen día!")
 """
#NOTA
"""if num1 < 6: print("El número es menor que 6"), print("Esto es sintácticamente correcto")""" #Es correcto pero no recomendable

#FUNCIÓN range(): Genera una secuencia de números enteros. Puede tomar argumentos

""" for i in range(5):
    print(i)

for i in range(4, 8): #Me devuelve una iteración del 1 al 4, porque el número final no lo incluye
    print(i)

for i in range(0, 10, 2): #Devuelve los numeros pares del 0 al 8 (inicio, final, incremento)
    print(i) """

""" personas = int(input("Introduce el nunero de personas"))

for i in range(personas):
    print("Otra persona") """