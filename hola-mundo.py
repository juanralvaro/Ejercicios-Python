#ACEPTAR SUGERENCIAS VS CODE : Tabulador    

#Esto es un comentario de una sola línea

"""Esto
es un comentario
en bloque: Los comentarios son fragmentos de código que son ignoradas por el intérprete. Para crear un bloque de código comentado, podemos seleccionarlo y pulsar el atajo ALT + SHIFT + A """

""" print("Estoy programando en Python ") """



#EJEMPLOS DE TIPOS DE DATOS

""" # _numero = 3 #Los nombre de variables no pueden comenzar por un número ni por un caracter especial,  a excepción del _numero = 42

#Puedo declarar varias variables a la vez
#nombre, edad, altura = "Juan", 30, 1

#print(nombre)

#namning de las variables --> Minúyscula + snake_case """

""" mi_nombre_es = "Alejandra" #str (String)
dato_numero = 2888 #int (Entero)
dato_decimal = 345.234 #float (Decimal)
dato_cadena_de_caracteres = "esto es una cadena"
dato_cadena_de_caracteres_dos = 'esto es una cadena' """

""" EJERCICIO 1
Crea 3 variables, una de tipo número que represente tu edad, otra de tipo string que represente tu nombre y otra de tipo decimal que represente tu peso.
Imprime estas variables utilizando la función print() """

""" edad = 33
nombre = "Alejandra"
peso = 23.67

print("Mi nombre es " + nombre + " y mi edad es " + str(edad)) #Conversión de variables """

#CADENAS DE CARACTERES

"""
#Siempre antes y después de un operador, tengo que incluir un espacio (el símbolor = es en Python el operador de asignación, el que utilizamos para asignar un valor a una variable)

cadena = "Hola" #El índice hace referencia a la posición de cada uno de los caracteres dentro de una cadena. El primer caracter en cualquier cadena siempre es el índice 0)
print(cadena[0]) 

cadena[0] = "L"
print(cadena) #Error porque no se puede modificar un único caracter. """


""" EJERCICIO 2

Crea un cuento modelo que incluya al menos 10 datos diferentes personalizados del niño o niña al que va dirigido el cuento. La declaración de variables debe ser en bloque. Ejemplo:

    ciudad, year, nombre_niño = "Bogotá", 2021, "Nicolás"
    print("Amanece en " + ciudad + "en el año " + str(year)+ "..." ) #El naming de una variable no puede empezar con un número, ni con un caracter especial a excepción de _ """

"""print("Habia una vez una niña llamada" + nombre +". Esta niña nacio en " + ciudad + 
      ". En el año"  + str(año) + "su familia se mudó a otra ciudad"  + " y ella no quiso irse" + 
      " por más que le decían que allí estaba bueno el lugar donde vivía su abuelo." + 
      "\nAsí que decidió quedarse y buscarle a él para que la llevara de vuelta a casa.")"""

#TRABAJANDO CON CADENA DE CARACTERES

""" cadena[1:2] # a una sección de la cadena, en la sección se incluye el primer índice y se excluye el segundo
cadena[1:] # desde un caracter hasta el final
cadena[:3] # desde el principio hasta un caracter
cadena[-1] # A la última posición
cadena[-2] # A la penúltima posición """

""" nueva_cadena = "soy una nueva variable"

print(nueva_cadena[0:4])
print(nueva_cadena[3:9])
print(nueva_cadena[5:])
print(nueva_cadena[:8])
print(nueva_cadena[-1])
print(nueva_cadena[-2]) """

""" TIPOS CONVERSIÓN DE DATOS 

¿Por qué es importante realizar conversiones de datos en Python?
    · Poder realizar operaciones coherentes.
    · Presentación de los datos
    · Interacción con los usuarios
    · Compatibilidad

TIPOS --->

1 - Casting de datos: Cambiar el tipo de dato de una variable
    numero_entero = int(3.14278974)
    numero_entero_dos = "El numero entero es" +  str(numero_entero)

2 - Concatenación de variables: Combinar variables de diferentes tipos en una cadena
    print("El nombre del usuario es " + name + " y su año de nacimiento es " + str(year))

3 - F-string: Simplificar la creacción de cadenas con variables.
    name = "Carlos"
    age = 35
    mensaje = f"Hola mi nombre es {name} y mi edad es {age}"

4 - .format : Alternativa más antigua para formatear cadenas. Surgió con Python1
    El método format() se utiliza para construir cadenas que contienen valores de variables.
    La sintaxis básica es:    
    mensaje = "Hola {} y su edad es {}".format(name, age)  #{} -> Marcadores

Otros métodos avanzados: 
json.dumps()
xml.etree.ElementTree.dump()

"""

""" #Casting de datos
numero_entero = int(3.14278974)
numero_entero_dos = "El numero entero es " +  str(numero_entero)
#print(numero_entero_dos)

name = "Pepito"
year = 1990
#print("El nombre del niño es " + name + " y su año de nacimiento es " + str(year))
#print(year + 10)

#f-string
name = "Juan"
age = 42
message = f"Mi nombre es {name} y mi edad es {age}"
#print(message)

#Método .format
message = "Hola, me llamo {} y tengo {} años".format(name,age)
#print(message) """

""" #ENTRADA POR TECLADO CON INPUT

#Cualquier tipo de dato

entrada = input() # Por defecto es una cadena de caracteres, se recomienda introducir previamente el tipo de dato:

entrada_dos = int(input())
entrada_tres = str(input())
entrada_cuatro = float(input()) 

nombre_usuario = input("\nIngrese un nombre:\n") #salto de línea:\n
print(f"Hola, " + nombre_usuario + ", bienvenidx a nuestro programa") """

""" #CONVERSIÓN MAYÚSCULAS-MINÚSCULAS

texto_original = "Buenos días, Alejandra"
print(texto_original)

#Conversión a mayúsculas
texto_mayusculas = texto_original.upper()
print(f"Texto en Mayúsculas: {texto_mayusculas}")

#Conversión a minúsculas
texto_minusculas = texto_original.lower()
print(f"Texto en Minúsculas: {texto_minusculas}")

 """