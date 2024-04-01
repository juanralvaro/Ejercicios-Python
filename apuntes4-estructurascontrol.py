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

#Operador ternario: Es el operador condicional que me permite escribir un condicional de forma compacta


""" xy = 11
resultado_xy = "positivo" if xy > 0 else "negativo" """
"""
variable = -resultado si condición que se ejecuta es verdadero- + -condición booleana a evaluar (comenzando con el if)- + -else + resultado si condición que se ejecuta si es falsa-

Esto equivale a:

xy = 11
if xy > 0:
    resultado = "positivo"
else:
    resultado = "negativo"
print(resultado)

"""


#------ EJEMPLOS -------
#1- Asignación de valor a una variable basado en una condición

""" edad = int(input("Introduce tu edad"))
mensaje = "Eres mayor de edad, bienvenido, puedes acceder" if edad >= 18 else "Eres menor de edad, lo sentimos, tienes el acceso restringido"
print(mensaje) """

"""--> Ejercicio anterior pero pidiendo el año de nacimiento

anio_nacimiento = int(input("Introduce tu año de nacimiento: "))
mensaje_dos = "Eres mayor de edad, bienvenido." if anio_nacimiento <= 2006 else "Eres menor de edad, ¡no puedes pasar!"
print(mensaje_dos) """

#2- Impresión condicional de un mensaje
""" xyz = 5
print("El número es 7" if xyz == 7 else "No es 7") """

"""
--> Solicita a un estudiante que te diga su nota, y en función de la nota imprime un mensaje diciendo que ha aprobado u otro diciendo que ha suspendido. Para ello utiliza la sintaxis del ejemplo que acabamos de ver.


nota = float(input("Introduce tu nota: "))
print("¡Has aprobado!" if nota >= 5 else "¡Has suspendido!") """

""" edad = int(input("Introduce tu edad: \n"))
print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad") """

#3- Modificar el valor de una variable
""" numero = int(input("Introduce un número\n"))
numero -= 1 if numero > 0 else numero
print(numero) """

"""
[código si verdadera]+[condicion]+[código si falsa]
--> Si la edad del usuario es positiva, dile cuantos años tenía el año pasado

edad_usuario = int(input("Introduce tu edad\n"))
edad_usuario -= 1 if edad_usuario > 0 else edad_usuario
print("Edad el año pasado",edad_usuario) """

# --------- BUCLE WHILE -------------
""" 
En python se utiliza para ejecutar un bloque de cíodigo de forma repetida mientras se interprete como verdadera la condición dada

while -condicion-:
    #Código que vamos a ejecutar mientras la condición sea verdadera
"""

""" numero = 7
while numero <= 20:
    print("El número es", numero)
    numero += 1 

infinito = 0
while True:
    print("bucle infinito")
    infinito += 1
    if infinito == 15:
        break
print("C'est fini") """

"""
--> Utiliza una condición diferente para implementar el bucle infinito
"""

""" infinito = 0
while True:
    print("Bucle infinito")
    infinito +=2
    if infinito == 10:
        break
print("Se acabó") """

# ELSE + WHILE: La sección de código del else se ejecuta cuando el bucle while se haya interrumpido de forma natural. Si interrumpo el bucle while utilizando un break, el código tras else no se va a ejecutar

""" x = 10
while x > 0:
    x -= 1
    print(x)
else:
    print("X ha llegado a cero") """

""" x = 12
while x > 0:
    x -= 2
    print("x =",x)
    if x == 4:
        break
else:
    print("Se acabó el bucle. No hay más iteraciones.") """

#-------ANIDACIÓN EN LOS BUCLES-----------
"""

nombres = ["Juan", "María", "Carlos"]
saludos = ["Hola", "Adiós"]

for nombre in nombres: #El bucle externo es el que controla el flujo general de la iteración
    for saludo in saludos: #Se ejecuta completamente en cada ciclo del bucle externo
        print(saludo, nombre)


for numero in range(1, 6):
    for numero_dos in range(1, 11):
        print(numero * numero_dos, end="\t") #Por defecto, el caracter de salida al final de un print() siempre es un salto de línea; "\t" marca como caracter de salida tabulación
    print()

#-----------------------------
for nombre in nombres:
    for saludo in saludos:
        print(f"¡{saludo},  {nombre}!") #Quedaría mejor """

""" for num1 in range(1, 11):
    for num2 in range(1, 11):
        print(num1 * num2, end="\t")
    print() """

""" for num1 in range(1, 11):
    for num2 in range(1, 11):
        for num3 in range(1, 11):
            print(num1 * num2 * num3, end="\t")
        print()
    print() """ #multiplicando al cubo en 10 estructuras

""" print("a","b","c", sep="-") #sep: separador
print("Hola", end="\t") #end: modifico el caracter de salida
print("Mundo") """

""" for i in range(5): #Secuencia 0, 1, 2, 3, 4. Bucle externo FILAS
    for j in range(i+1): #Bucle interno COLUMNAS | secuencia= 0+1, 1+1, 2+1, 3+1, 4+1
        print("*", end=" ") #Imprime un asterisco + espacio por cada columna
    print() #Imprime una nueva línea al final de cada columna """

""" for i in range(5):
    for j in range(i+1):
        for k in range(j):
            print("*", end=" ")
        print()
    print() """ #aparición gradual de estrellas

""" for filas in range(10):
    for columnas in range(filas+1):
        print("^", end=" ")
    print() #1 ^ en fila 1, 2 ^ en la 2, ... 10 ^ en la 10 """

# ----- FUNCIONES EN PYTHON --------
"""
Una  función en Python es un bloque de código que se puede llamar desde cualquier lugar del programa. Estas funciones permiten organizar la ejecución de nuestro programa. SINTAXIS:
def nombre_funcion(argumentos de entrada):
    bloque de código
    return valor devuelto (opcional)
 """
#Ejemplo 1
def suma(a, b):
    return a - b
print("La sumatoria es:", suma(6,3))

# Ejemplo 2
def Suma(a, b):
    sumatorio = a + b
    print("La sumatoria es:", sumatorio)
    return (sumatorio) #Utilizamos return para comunicar el resultado de una función de vuelta al código que la ha llamado. Nos permite que ese resultado se almacene o se utilice en futuras operaciones

sum = Suma(5, 5)

#Ejemplo 3
def suma_dos(a, b):
    print("La sumatoria es:",a + b)
suma_dos(10, 5)

numero = 100 * sum
print(numero)

#Ejemplo función saludar: Utilizar variables globales dentro de mi función.
""" nombre_usuario = str(input("Ingrese su nombre: \n"))

def saluda():
    print ("Hola", nombre_usuario)

saluda() """

#Ejemplo parámetro como variables

""" def doble(numero):
    return numero + numero

resultado_uno = doble(5)
resultado_dos = doble(10)

print(resultado_uno, resultado_dos)

#Ejemplo pasar variables como argumento

mi_numero = 7
resultado = doble(mi_numero)
print(resultado) """

# USO DE RETURN

def suma_sin_return(a, b):
    resultado_tres = a + b #None

resultado_suma_sin = suma_sin_return(10,5)
print(resultado_suma_sin)

def suma_con_return(a, b):
    resultado_tres = a + b
    return resultado_tres

resultado_suma_con = suma_con_return(10,5)
print(resultado_suma_con)

#Ejemplos pero con resta
#1
def resta1(a, b):
    return a - b
print("La resta 1 es:",resta1(5,4))
#2
def resta2(a, b):
    restatorio = a - b
    print("La resta 2 es:",restatorio)
    return (restatorio)
res = resta2(5,2)
#3
def resta3(a, b):
    print("La resta 3 es:",a-b)
resta3(10,2)

numero = 100 * resta1(10,5) #con resta3 daría error porque contienen strings
print(numero)

#Práctica rápida: crear un programa que le solicite al usuario su nombre y sus apellidos. A continuación, el programa ejecutará una función saludar() para saludar al usuario.
#Siguiente: solicitamos el año de nacimiento, y a continuación el usuario le dirá al programa los años que tiene.

nombre = str(input("Introduzca su nombre:"))
apellidos = str(input("Introduzca sus apellidos:"))

def saludar():
    print("Hola",nombre,apellidos )

saludar()

anio_nacimiento = int(input("Introduzca su año de nacimiento:"))

def edad():
    print(f"Su edad es: {2024 - anio_nacimiento} años.")
edad()