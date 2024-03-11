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

#***************LISTAS EN PYTHON: Colecciones de datos mutables, a cuyos elementos accedemos a través de un index y que nos permiten incluir cualquier tipo de dato. Pueden contener elementos duplicados 

#Sintaxis de las listas
""" mi_lista = [1, 2, 3, 0.3, 'Hola', True]
print(mi_lista)
 """
#Acceder a los elementos de la lista
""" primer_elemento = mi_lista[0]
print(primer_elemento)
print(mi_lista[3])
 """
#Modificar un elemento de la lista
""" mi_lista[4] = "Adios"
print(mi_lista)
 """
#--Métodos más habituales de las listas en Python

#Método append(): Agregar un elemento al final de nuestra lista. 
""" mi_lista.append("Nuevo elemento")
tipo_lista = type(mi_lista)
print(mi_lista, "El tipo de datos de la lista es:", tipo_lista)
 """

#Método remove(): Eliminar un elemento de nuestra lista. 
""" mi_lista.remove([2])
print(mi_lista)
 """

#--> ¿Cómo hacer que el usuario añada elementos a la lista?
""" lista_usuario = [] #Creamos una lista vacia
nuevo_elemento = int(input("Introduce un número: "))
lista_usuario.append(nuevo_elemento)
tipo_de_datos = type(nuevo_elemento) #Comprobamos si es int o str...etc
print("lista actualizada:", lista_usuario, "El tipo de dato introducido es:", tipo_de_datos)
 """
#Método sort() - Ordena la lista en su sitio, en la propia lista
""" lista_ordenada = ["Hola", "Adios", "Buenos días", "Adaia"]

lista_ordenada.sort()
print("La lista ordenada es:", lista_ordenada) #La misma variable, pero actualizada (ordenada) """

#Método sorted(): Ordenar los elementos de una lista dando lugar a una nueva lista
""" nueva_lista_ordenada =  sorted([9, 8, 7, 6, 5, 4,  3, 2, 1])
nueva_lista_dos = [4, 6, 2, 7, 7, 2, 5, 7]
nueva_lista_ordenada_dos = sorted(nueva_lista_dos)
print("Lista ordenada uno: ", nueva_lista_ordenada, "Lista ordenada dos: ", nueva_lista_ordenada_dos)
print(lista_ordenada, nueva_lista_dos)
 """ 
#Ordenar de forma descendente
""" descendente_sort = [2, 9, 5, 7, 6, 8, 1, 2]
descendente_sorted = [2, 9, 5, 7, 6, 8, 1, 2]

descendente_sort.sort(reverse=True)
nueva_descendente_sorted = sorted(descendente_sorted, reverse=True)
print("Resultado de las listas ordenadas descendentemente: \nSort:", descendente_sort, "\nSorted:", nueva_descendente_sorted)"""

#Método len(): Comprueba la longitud o número de elementos de una lista
"""lista_longitud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La longitud de la lista es: ",len(lista_longitud))"""

#Método count(): Devuelve el número de ocurrencias de un elemento en la lista
"""nueva_lista_tres = [1, 2, 3, 1, 3, 2, 3, 3, 3, 3]
print("Hay", nueva_lista_tres.count(2), "elementos '2' en la lista.")"""

#Método len(): Comprueba la longitud o número de elementos de una lista
""" lista_longitud = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La longitud de la lista es: ",len(lista_longitud)) """

#Método count(): Devuelve el número de ocurrencias de un elemento en la lista
""" nueva_lista_tres = [1, 2, 3, 1, 3, 2, 3, 3, 3, 3]
print("Hay", nueva_lista_tres.count(2), "elementos '2' en la lista.") """

#Método pop(): Elimina y devuelve el elemento que se encuentra en la posición indicada, o el último elemento si no se proporciona un índice.
""" lista_pop = [0, 1, 2, 3, 4, 1]
elemento = lista_pop.pop(4)# Resultado: lista=[1, 3], elemento=2
print("Lista sin el elemento eliminado:", lista_pop,"\nElemento eliminado:", elemento) """

#Método reserve(): Invierte los elementos de la lista
""" lista_pop.reverse()
print("Lista invertida:", lista_pop) """

#Método copy(): Crea y devuelve una copia superficial de la lista.
""" copia_de_mi_lista = lista_pop.copy()
print("Copia de mi lista:", copia_de_mi_lista) """

#INTRODUCCIÓN BUCLE FOR: Una estructura de control que me va a permitir ITERAR sobre los elementos de una secuencia. Lo utilizo para iterar sobre listas, tuplas, cadenas de caracteres o sobre cualquier otro elementos ITERABLES.
""" lista_frutas = ["manzana", "pera", "plátano"]
for fruta in lista_frutas:
    print("Soy", fruta) """

#Ejemplos
""" lista2 = ["Juan", 42, 1.84]
print(lista2)

segundo_elemento = lista2[1]
print(segundo_elemento)

lista2[2] = 1.83
print(lista2)

lista3 = ["a", "b", "c", 1, 2, 3]
print(lista3)

tercer_elemento = lista3[2]
print(tercer_elemento)
print(lista3[5])

lista3[4] = "o"
print(lista3)

lista2.append("New element")
print(lista2)
lista2.append("Más añadidos")
lista2.append("Todavía más")
print(lista2)

lista_personal = []
nuevo_dato = input("Introduce un nuevo dato: ")
lista_personal.append(nuevo_dato)
tipo_dato = type(nuevo_dato)
print("Mi lista personal contiene", lista_personal, "su nuevo dato es un", tipo_dato)
otro_nuevo_dato = int(input("Introduce otro nuevo dato: "))
lista_personal.append(otro_nuevo_dato)
tipo_dato = type(otro_nuevo_dato)
print("Mi lista personal contiene", lista_personal, "cuyo último dato es", tipo_dato)
ultimo_dato = float(input("Introduce el último dato: "))
lista_personal.append(ultimo_dato)
tipo_dato = type(ultimo_dato)
print("Mi lista personal final contiene", lista_personal, "cuyo dato final es de tipo", tipo_dato) 

lista_mess1 = ["Adiós", "Hola", "Cabeza", "Ética", "Ácido"]
lista_mess1.sort()
print(lista_mess1)

lista_mess2 = [2, 6, 89, 234, 0.2, 4, 17]
lista_not_mess = sorted(lista_mess2)
print(lista_mess2, lista_not_mess)

lista_mess1.sort(reverse=True)
lista_not_mess_rev = sorted(lista_mess2, reverse=True)
print(lista_mess1, lista_not_mess_rev) 

lista_nueva = [1, 2, 3, 4, 5, 6]
print(lista_nueva)
lista_nueva.insert(2, 2.5)
print(lista_nueva)

lista_animales = ["Perro", "Gato", "Ratón"]
print(lista_animales)
lista_animales.extend(["Cuervo", "Águila", "León"])
print(lista_animales)
lista_animales.extend(["Pájaro", "Nutria", "Ballena"])
print(lista_animales)

lista_numerica = [1, 4, 2, 4, 2, 1]
lista_numerica.remove(1)
print(lista_numerica)
lista_numerica.remove(2)
print(lista_numerica)

lista_numerica_dos = [1, 3, 2, 4, 3, 4, 2, 1]
indice_tres = lista_numerica_dos.index(3)
print(indice_tres)

lista_numerica_dos.clear()
print(lista_numerica_dos)

lista_larga = [1, 2, 4, 8.20, "Hola", [2, 3]]
print(len(lista_larga))

lista_de_cuenta = [2, 3, 23, 5, 2, 5, 3, 2, 5]
print(lista_de_cuenta.count(2))

lista_variable = [0, 2, 4, 5, 7]
elemento_out = lista_variable.pop(3)
print(lista_variable,"sin el",elemento_out)

lista_variable.reverse()
print(lista_variable)

lista_copiada = lista_variable.copy()
print(lista_copiada)

lista_animales = ["perro", "gato", "ratón"]
for animal in lista_animales:
    print("Soy un",animal)"""

# COLECCIONES DE DATOS: TUPLAS ***************************
"""Tipo de estructura de datos que nos permite almacenar datos y que además son INMUTABLES, lo que las hace más rápidas a la hora de acceder a ellas
tupla_vacia = ()
mi_primera_tupla = (10, "Hola", True) 
mi_tupla = 1, 2, 3, "oso", False #Puedo crear una tupla sin utilizar los ()
print( "El tipo de datos de mi tupla es:", type(mi_tupla), mi_primera_tupla)"""

#Acceder a los elementos de mi tupla
""" tupla_acceso = 0, 1, 2, "Pepe", 4
print("Accediendo a mi tupla:", tupla_acceso[3])
tupla_dentro_tupla = 1, 5, 8, ("y", "w", "z"), 5, 6
print("Tupla dentro de otra tupla:", tupla_dentro_tupla[3][0]) """

#Modificar los elementos de mi tupla --> ERROR: TypeError: 'tuple' object does not support item assignment
#Excepción: modificar elementos de una lista que esté en mi tupla
""" modificar_tupla = 1, 2, 3, 4, 5, ["hola", "adios", "pepe"]
print("Tupla antes de modificación:", modificar_tupla)
#modificar_tupla[2] = 2
#print("Intentando modificar la tupla: ", modificar_tupla)
modificar_tupla[5][1] = "ADIOS"
print("Tupla después de modificación:",modificar_tupla) """

#Asignar el valor de los elementos de una tupla a variables
""" tupla_asigna = 3, 4, 5
x, y, z = tupla_asigna
print("Asignación múltiple:",x, y, z) """

#Convertir una lista en una tupla --> tuple()
""" lista_inicial = [7, 9, 11]
lista_convertida_tupla = tuple(lista_inicial) #Casting de datos para convertir una lista en una tupla
print("Tipo de lista convertida:", type(lista_convertida_tupla), "& Tipo de lista antes de la conversión:", type(lista_inicial)) """

tupla = 1, 4, 7
print(tupla)
print(tupla[1])

tupla_en_tupla = 1, 5, 8, ("a", "b"), 6
print(tupla_en_tupla[2], tupla_en_tupla [3][1])

tupla_con_lista = 2, 4, ["buenas", "tardes"]
print(tupla_con_lista)
tupla_con_lista[2][1] = "noches"
print(tupla_con_lista)

tupla_valores = 4, 7, 8, 3
a, b, c, d = tupla_valores
print(a, b, c, d)