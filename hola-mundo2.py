""" #OPERADORES DE ASIGNACIÓN---------------------------


#Operador de asignación simple - " = " --> Para asignar un valor a una variable.
nombre_variable = "valor"
asignacion_multiple, asignacion_multiple_dos = "valor1", "valor2" 

#Operador de adición y asignación " += "
b = 3
a = 5
b += a # b se va a incrementar por el valor de a --> b = b + a
print(b)

# Resta y asignación " -= "
c = 10
c -= 2 # c= c - 2 * 2
print(c)

#Multiplicación y asignación " *= "
d = 4
d *= c # d= d * c
print(d)

#División y asignación "  /= "
e = 8
e /= 2 # e = e / 2
print(e)

#Cociente y asignación " //= "
f = 9
f //= 3 # f = f // 3
print(f)

#Módulo y asignación "%="
g = 7
g  %= 2 # g = g % 2
print(g)

#Potencia y asignación " **= "
h = 2
h **= 3 # h = h ^ 3
print(h) """

""" #OPERADORES DE COMPARACIÓN---------------------------

#Operador igual ==
a = "Hola"
b = "Hola"
resultado_igual = a == b 


#Operador No igual !=
resultado_no_igual = a != b


#Mayor que >
e = 8
f = 10
mayor_que = e > f


#Menor que <
menor_que = e < f


#Mayor o igual >=
g = 15
h = 10
resultado_mayor_o_igual = g >= h


#Menor o igual <=
resultado_menor_o_igual = g <= h
print(resultado_menor_o_igual)
 """
a = 7
b = 5
a += b
print(a)

c = 5
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