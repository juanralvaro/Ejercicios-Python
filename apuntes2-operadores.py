#OPERADORES EN PYTHON----------------------------------------

#Tipos de operadores
""" - operadores básicos: suma, resta, multiplicación, división, cociente de la división, módulo y potencia. Nos sirven para realizar operaciones matemáticas simples.  """
#SUMA "+"
""" resultado_suma =  5 + 3 
#resultado_suma =  "Hola" + 3 --> No permite operar con tipos de datos diferentes: TypeError """
""" print("La suma es:", resultado_suma ) """

#RESTA "-"
""" resultado_resta = 10 - 3
#resultado_resta =  "Hola" - 3 --> No permite operar con tipos de datos diferentes: TypeError
print("La resta es: " + str(resultado_resta)) #Para concatenar dos valores con el símbolo + necesitamos que sean del mismo tipo, si no lo son, necesitamos realizar una conversión """

#MULTIPLICACIÓN "*"
""" resultado_multiplicacion = 4 * 5
print("La multiplicación es:", resultado_multiplicacion)
print(f"La multiplicación es: {resultado_multiplicacion}") """

#DIVISIÓN "/"
""" resultado_division = 8 / 2
print("El resultado de la división es:", resultado_division)
print(f"El resultado de la división es: {int(resultado_division)}") #Para que salga sólo el entero sin decimales puedo convertir el valor de la variable utilizando el método int() """

#COCIENTE de la división "//" --> Resultado de la división como número entero
""" cociente = 8 // 2
print("Cociente: ", cociente)
print(f"Cociente: {float(cociente)}")
 """
#MÓDULO (Resto de la división) "%"
""" resto = 9 % 2
print("Resto:", resto)
print(f"Resto: {resto}")
 """
#POTENCIA "**"
"""
potencia = 2 ** 3
print("La potencia es:", potencia)
print(f"La potencia es:{potencia}")
 """

""" print("Bienvenido al programa de operaciones aritméticas.")
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

print(f"La suma de {num1} y {num2} es {num1 + num2}.")
print(f"La resta de {num1} y {num2} es {num1 - num2}.")
print(f"La multiplicación de {num1} y {num2} es {num1 * num2}.")
print(f"La división de {num1} y {num2} es {num1 / num2}.")
print(f"El cociente de {num1} y {num2} es {num1 // num2}.")
print(f"El resto resultado de la división entre {num1} y {num2} es {num1 & num2}.")
print(f"La potencia de {num1} y {num2} es {num1 ** num2}.") """

#numero_decimal = 3.148538475489579347
#decimal_acortado = round(numero_decimal, 5)
#decimal_acortado = "{:.7f}".format(numero_decimal)
#print(decimal_acortado)

#OPERADORES DE ASIGNACIÓN---------------------------


#Operador de asignación simple - " = " --> Para asignar un valor a una variable.
""" nombre_variable = "valor"
asignacion_multiple, asignacion_multiple_dos = "valor1", "valor2"  """

#Operador de adición y asignación " += "
""" b = 3
a = 5
b += a # b se va a incrementar por el valor de a --> b = b + a
print(b) """

# Resta y asignación " -= "
""" c = 10
c -= 2 # c= c - 2 * 2
print(c) """

#Multiplicación y asignación " *= "
""" d = 4
d *= c # d= d * c
print(d) """

#División y asignación "  /= "
""" e = 8
e /= 2 # e = e / 2
print(e) """

#Cociente y asignación " //= "
""" f = 9
f //= 3 # f = f // 3
print(f) """

#Módulo y asignación "%="
""" g = 7
g  %= 2 # g = g % 2
print(g) """

#Potencia y asignación " **= "
""" h = 2
h **= 3 # h = h ^ 3
print(h) """ """

""" #OPERADORES DE COMPARACIÓN---------------------------

#Operador igual ==
""" a = "Hola"
b = "Hola"
resultado_igual = a == b 
 """

#Operador No igual !=
""" resultado_no_igual = a != b
 """

#Mayor que >
""" e = 8
f = 10
mayor_que = e > f
 """

#Menor que <
""" menor_que = e < f
 """

#Mayor o igual >=
""" g = 15
h = 10
resultado_mayor_o_igual = g >= h
 """

#Menor o igual <=
""" resultado_menor_o_igual = g <= h
print(resultado_menor_o_igual)
 """
""" a = 7
b = 5
a += b
print(a)
 """
#Ejemplos
""" c = 5
d = 2
c -= d
print(c)

e = 8
f = 3
e *= f
print(e)

g = 8
g /= 2
print(g)
print(f"{g:.0f}")

h = 10
h //= 3
print(h)

i = 3
i &= 2
print(i)

j = 3
j **= 4
print(j)

k = 5
l = 6
es_igual = k == l
print(es_igual)

m = 5.0
n = 5
es_igual_2 = m == n
print(es_igual_2)

o = "Hola"
p = "Mola"
es_igual_3 = o == p
print(es_igual_3)

q = 5
r = 4
es_mayor = q > r
print(es_mayor)

s = 4
t = 3
es_menor = s < t
print(es_menor)

u = 10
v = 10
es_mayor_o_igual = u >= v
print(es_mayor_o_igual)

w = 7
y = 5
es_menor_o_igual = w <= y
print(es_menor_o_igual) 

a = "Hola"
b = "Mundo"
c = 24
d = "Hola"
print(id(a), id(b), id(c), id(d))

print(a is b)
print(a is not b)
print(a is d)
print(id(a) is id(d))

e = "Juan"
f = "Juan"
print(id(e), id(f))
print(e is f)
print(id(e) is id(f))

a = 10
b = 12
print("¿a es b?", (e is f))
print("¿a no es b?", (e is not f))

coche = "Ferrari"
resultado_in = "i" in coche
resultado_not_in = "i" not in coche
print(resultado_in)
print(resultado_not_in)

euros = [0.25,0.50,0.75]
resultado_in = 1.25 in euros
resultado_not_in = 1.25 not in euros
print(resultado_in)
print(resultado_not_in)

y = 2 > 1
print("¿Y es cierto?", y)

x = 2 < 1
print("¿X es cierto?", x)  """