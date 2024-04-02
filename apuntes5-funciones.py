# ----- FUNCIONES EN PYTHON --------
"""
Una  función en Python es un bloque de código que se puede llamar desde cualquier lugar del programa. Estas funciones permiten organizar la ejecución de nuestro programa. SINTAXIS:
def nombre_funcion(argumentos de entrada):
    bloque de código
    return valor devuelto (opcional)
 """
#Ejemplo 1
""" def suma(a, b):
    return a - b
print("La sumatoria es:", suma(6,3)) """

# Ejemplo 2
""" def Suma(a, b):
    sumatorio = a + b
    print("La sumatoria es:", sumatorio)
    return (sumatorio) #Utilizamos return para comunicar el resultado de una función de vuelta al código que la ha llamado. Nos permite que ese resultado se almacene o se utilice en futuras operaciones

sum = Suma(5, 5) """

#Ejemplo 3
""" def suma_dos(a, b):
    print("La sumatoria es:",a + b)
suma_dos(10, 5)

numero = 100 * sum
print(numero) """

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

""" def suma_sin_return(a, b):
    resultado_tres = a + b #None

resultado_suma_sin = suma_sin_return(10,5)
print(resultado_suma_sin)

def suma_con_return(a, b):
    resultado_tres = a + b
    return resultado_tres

resultado_suma_con = suma_con_return(10,5)
print(resultado_suma_con)
 """
#Ejemplos pero con resta
#1
""" def resta1(a, b):
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
print(numero)  """

#Argumentos por posición: Python tomará la posición de los argumentos y la equiparará a la posición de los parámetros. 

""" def suma(a, b): #Parámetro: variable declarada en la definición de una función. La función espera recibir estos valores cuando sea llamada. Se utilizan para pasar información desde fuera hacia adentro
    return a + b

resultado = suma(5, 3) # 5 y 3 son argumentos: Es el valor real que se la pasa a la función cuando se la llama.  """

""" def multiplicacion(a, b):
    return a * b

resultado_multiplicacion = multiplicacion(b=4, a=3)
print("Resultado de la multiplicación",resultado_multiplicacion)

def division(a, b, c=2):
    return a / b / c

resultado_division = division(100, 2)
resultado_division_dos = division(100, 2, 5)
print("Resultado división uno",resultado_division)
print("Resultado división dos",resultado_division_dos)"""

#Argumentos por nombre: incluyo el nombre del parámetro seguido del símbolo "=" y a continuación añado el argumento asociado a ese parámetro
""" def resta(a, b):
    return a - b
numero_uno = int(input("Por favor introduce el primer número"))
numero_dos = int(input("Por favor introduce el segundo número"))
resultado_resta = resta(b=numero_uno, a=numero_dos)
resultado_resta = resta(5, 10)
print(resultado_resta) """

#Ejemplo: Defino una función saludar que incluya un parámetro nombre
""" def saludar(nombre):
    print("hola", nombre)
#Solicito al usuario que introduzca su nombre
nombre_usuario = str(input("Por favor, introduce tu nombre"))
#Llamo a la función saludar y le paso como argumento la variable nombre_usuario
saludar(nombre_usuario) """

#Argumentos por defecto
""" def multiplicacion(a, b, c=100):
    return a * b * c
resultado_multiplicacion = multiplicacion(2, 3)
resultado_multiplicacion_dos = multiplicacion(2, 3, 5)
print(resultado_multiplicacion)
print(resultado_multiplicacion_dos) """

#Argumentos de longitud variable
"""def suma_dos(numeros):
    total = 0
    for n in numeros:
        total += n #total = total + n
    return total
suma_dos([2, 2, 2, 2, 5, 5, 5, 5])
print("El valor total es:", suma_dos([2, 3, 4]))

def suma_tres(*numeros):
    total = 0
    for n in numeros:
        total += n #total = total + n
    return total
suma_tres(1, 2, 3, 4)
suma_tres(1, 2)
suma_tres(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("El valor total de la tupla es:", suma_tres(3, 4, 5, 5)) """

#Ejemplo
"""def resta_dos(numeros):
    total = 0
    for n in numeros:
        total -= n
        print(total)
    return total

resultado_resta_dos = resta_dos([10, 4, 3, 1])
print("El resultado de la lista es",resultado_resta_dos)

def resta_tres(*numeros):
    total = 0
    for n in numeros:
        total -= n
        print(total)
    return total

resultado_resta_tres = resta_tres(10, 5, 2, 6)
print("El resultado de la tupla es",resultado_resta_tres) """


#Pasar un diccionario como parámetro
""" def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(clave, ": ", valor)

diccionario_uno = {"nombre": "Pepe",  "edad": 30,  "profesion": "programador"}
diccionario_dos = {"nombre": "Paco",  "edad": 28,  "profesion": "desarrollador"}
imprimir_diccionario(diccionario_uno)
imprimir_diccionario(diccionario_dos)

#Ejemplo
def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(clave, ":", valor) 

diccionario_frutas = {"nombre" : "naranja", "sabor" : "dulce", "zumo": "sí"}

diccionario_animales = {"nombre": "perro", "sonido": "ladrido", "peligroso": "puede"}

diccionario_anidado = {"persona": {"nombre": "Juan", "apellido" : "Pérez"}, "empresa": "Adecco"}

imprimir_diccionario(diccionario_frutas)
imprimir_diccionario(diccionario_animales)
imprimir_diccionario(diccionario_anidado)"""

#Pasar una función como parámetro

""" def suma_fun(a, b):
    return a + b 

def resta_fun(a, b):
    return a - b 

def aplicar_operacion(funcion, a, b):
    return funcion(a, b)

operacion_suma =  aplicar_operacion(suma_fun, 5, 3)
operacion_resta = aplicar_operacion(resta_fun, 5, 3)
print("El resultado de la suma es:", operacion_suma)
print("El resultado de la resta es:", operacion_resta)

#Ejemplo
def multiplicacion_fun(a, b):
    return a * b

def division_fun(a, b):
    return a / b

def operar(funcion_dos, a, b):
    return funcion_dos(a, b)

operacion_multiplicacion = aplicar_operacion(multiplicacion_fun,6,3)
operacion_division = aplicar_operacion(division_fun,6,3)
print("El resultado de la multiplicación es", operacion_multiplicacion)
print("El resultado de la división es", operacion_division) """

""" #EJEMPLO ARGUMENTOS POR DEFECTO Y ARGUMENTOS POSICIONALES

#Programa para calcular el salario de un empleado en función de su nivel y de sus horas trabajadas

#Bienvenida al programa
print("Bienvenido al programa para calcular salarios")

#Definimos la función que nos permitirá calcular el salario de cada empleado en función de su nivel y de sus horas trabajadas
def calcular_salario_horas(horas_trabajadas, nivel="Junior"):
    if nivel == "Junior":
        salario_por_hora = 10
    elif nivel == "Senior":
        salario_por_hora = 15
    elif nivel == "Experto":
        salario_por_hora = 20
    salario_total = horas_trabajadas * salario_por_hora
    return salario_total

#Preguntamos al usuario cuantas horas ha trabajado cada nivel en esta semana
horario_junior = int(input("Ponga las horas trabajadas como junior: "))
horario_senior = int(input("Ponga las horas trabajadas como senior: "))
horario_experto = int(input("Ponga las horas trabajadas como experto: "))

#Devolver los salarios para cada nivel con argumentos por defecto y argumentos posicionales
salario_junior = calcular_salario_horas(horario_junior)
salario_senior = calcular_salario_horas(horario_senior, "Senior")
salario_experto = calcular_salario_horas(horario_experto, "Experto")

#Imprimo los resultados de los salarios
print("\nSalario del Junior:", salario_junior)
print("Salario del Senior:", salario_senior)
print("Salario del Experto:", salario_experto) """

#EJEMPLO ARGUMENTOS DE LONGITUD VARIABLE

#Programa para calcular el total de los pagos que una empresa tiene que efectuar a sus empleados durante un mes

#Bienvenida al programa
""" print("Bienvenido al programa para el total de pago de los salarios de tu empresa.")

#Definir la función que me permira calcular el sumatorio de los ingresos de todos los empleados
def sumar_ingresos(*ingresos):
    total = sum(ingresos)
    return total

#Pedir al usuario los salarios de sus empleados utilizando una estructura de control que le permita al usuario salir del bucle cuando haya introducido todos los datos.

salarios_empleados = []

while True:
    salarios = str(input("Introduzca su salario: "))
    if salarios.lower() == "fin":
        break
    else:
        salarios_empleados.append(int(salarios))

#Llamamos a la función y le pasamos como argumentos los salarios de todos los empleados que ese mes están en situación activa en la empresa
total_salarios = sumar_ingresos(*salarios_empleados)
print("Total a pagar: ",total_salarios) """