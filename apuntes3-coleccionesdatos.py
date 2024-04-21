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

#Método count(): Este método nos devuelve el número de veces que aparece un valor en la tupla

""" tupla_count = (1, 2, 3, 1, 2, 3, 1, 2, 3)
veces_dos = tupla_count.count(2)
print("\nNúmero de veces que aparece el valor 2: ",veces_dos) """

#Método index(valor, [inicio], [fin]): Devuelve el índice de la primera ocurrencia de un valor en la tupla

""" tupla_index = 10, 20, 30 , 40, 10, 50, 90, 10, 30, 40
indice = tupla_index.index(10)
print("\nIndex de la primera ocurrencia de 10: ", indice)
indice_dos = tupla_index.index(10, 1)
print("\nIndex de la segunda ocurrencia de 10: ", indice_dos)
indice_tres = tupla_index.index(10, 5, 8)
print("\nIndex de la ocurrencia de 10 entre los index 5 y 7: ", indice_tres) """

#Método len(): Devuelve la longitud (número de elementos) de mi tupla
""" tupla_longitud = 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 12, 2, 1, 2
print("La longitud de la tupla es:", len(tupla_longitud))
longitud = len(tupla_longitud)
print(f"La longitud es {longitud}") """

#Método sorted(): Devuelve una LISTA ordenada a partir de los elementos de la tupla. Yo NO ESTOY MODIFICANDO MI TUPLA (ni cambio el orden..), estoy creando una nueva colección de datos (lista) a partir de los datos existentes en la tupla. Hace un 2x1: convierte(convierte creando una nueva colección de datos, no incidiendo sobre la colección de datos original) + ordena
""" tupla_desordenada = 4, 6, 2, 7, 3, 5, 1, 8, 7, 0, 9
coleccion_ordenada = sorted(tupla_desordenada) """
"""Esta instrucción realiza los siguientes pasos:
1- Lee los elementos de la tupla
2- Crea una nueva lista
3- Incluye en la nueva lista los valores de la tupla ordenados
4- Almacena la lista en la variuable coleccion_ordenada"""
""" print(coleccion_ordenada, tupla_desordenada) """

#conversión lista a tupla
""" lista_a_tupla = [1, 2, 3, 4, 5]
conversion_a_tupla = tuple(lista_a_tupla)
print(conversion_a_tupla, lista_a_tupla) """

#conversión tupla a lista
""" tupla_a_lista = 1, 2, 3, 4, 5
conversion_a_lista = list(tupla_a_lista)
print(conversion_a_lista, tupla_a_lista) """

#Operar con tuplas: Puedo realizar operaciones de concatenación (+) y de multiplicación (*)

""" tupla_uno = 1, 7, 3
tupla_dos = 4, 2, 6
concatenacion_tuplas = tupla_uno + tupla_dos
repetir_tuplas = tupla_uno * 3
print("Tuplas concatenadas:", concatenacion_tuplas, "\nTuplas repetidas:",repetir_tuplas) """

#Ejemplos:

""" tupla = 1, 4, 7
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

tupla_contar = 7, 34, 7, 29, 28, 23, 4, 6, 7, 2, 5, 6, 6, 7
valor_siete = tupla_contar.count(7)
print("Veces que aparece el siete:", valor_siete)

tupla_index = 23, 12, 123, 23, 5, 12, 23
primer_12 = tupla_index.index(12)
print("Primer índice donde sale el 12:", primer_12)
primer_23_sin_contar_el_primero = tupla_index.index(23, 1, 6)
print("Segundo índice donde sale el 23:", primer_23_sin_contar_el_primero)
tercer_23 = tupla_index.index(23, 4, 7)#Los índices son del 0 al 6, pero para buscar hasta el final de la lista hay que poner el número total de elementos de la tupla
print("Tercer índice donde está el 23:", tercer_23)

#Práctica oficial:
tupla_practica = 1, 2, 3, 50, 60, 70, 1, 2, 3, 50, 60, 70 """

"""  1- ¿Cuál es el index de la primera ocurrencia de 60?
 2- ¿Cuál es el index de la segunda ocurrrencia de 60?
 3- ¿Cuál es el index de la segunda ocurrencia de 2?
 4- ¿Cuál es el index de la primera ocurrencia de 3, entre los index 1 y 7?
 """
"""primer_sesenta = tupla_practica.index(60)
print("Index primer sesenta:", primer_sesenta)
segundo_sesenta = tupla_practica.index(60, 5)
print("Index segundo sesenta:", segundo_sesenta)
segundo_dos = tupla_practica.index(2, 2)
print("Index segundo dos:", segundo_dos)
primer_tres_entre_index_uno_y_siete = tupla_practica.index(3, 1, 7)
print("Index primer 3 entre index 1 y 7:", primer_tres_entre_index_uno_y_siete)

tupla_longitud = 2, 45, 25, 2, 12, 52, 2, 5, 3, 2, 23, 23, 1
print("Longitud de la tupla:", len(tupla_longitud))
longitud = len(tupla_longitud)
print(f"La longitud es: {longitud}.")

tupla_desordenada = 1, 5, 2, 29, 29, 2, 28, 0, 12, -1
coleccion_con_orden = sorted(tupla_desordenada)
print(coleccion_con_orden)
tupla_con_orden = tuple(coleccion_con_orden)
print(tupla_con_orden)

tupla1 = 2, 5, 3
tupla2 = 5, 1, 4
concatenacion_tuplas = tupla1 + tupla2
repeticion_tuplas = tupla1 * 3
print(concatenacion_tuplas, repeticion_tuplas)"""

#*************** CONJUNTOS / SETS **********************
"""Colecciones de datos no ordenadas, a las que no voy a poder acceder a los elementos a través de su index y cuya sintaxis se construye utilizando el símbolo "{}". Admite cualquier tipo de datos. No pueden contener elementos duplicados. No aplica una forma específica para acceder a los elementos.
CARACTERÍSTICAS FUNDAMENTALES:
· Elementos únicos: No pueden contener duplicados, ni otros conjuntos directamente, ya que los elementos de un conjunto deben ser inmutables, y los conjuntos son mutables.
· No ordenados
· Mutables
· Sintaxis de creacción: {} & set() 
· Admite la mayoría de tipos de dato, dentro de las colecciones de datos solo admitirá tuplas. Además, será ilógico incluir valores booleanos dentro de nuestro conjunto.
    logico = True, False #Puedo acceder por index y es inmutable
    ilogico = {True, False} #No puedo acceder por index y además no mantiene el orden de insercción
"""
""" mi_primer_conjunto = {"elemento1", "elemento2", 3, 4, 4.1, True} #Se crea utilizando las {}
print(mi_primer_conjunto)
print("Este es mi primer conjunto:", mi_primer_conjunto)"""

#Ejemplo
""" conjunto_autores = {"Federico García Lorca", "Carlos Ruiz-Zafón", "Miguel de Cervantes", "Paulo Coelho", "José Saramago", "Federico García Lorca", "Javier Cercas", "Miguel de Cervantes", "María Moliner", "Rosa Chacel"}
print(conjunto_autores)
 """

#También podemos crear conjuntos utilizando el método de constructor set()
""" mi_primer_set = set([2, 5, 6, 2, 3, 4]) 
print(mi_primer_set)  """

""" conjunto_y_tupla = {1, 2, 3, (4, 5)}
print("Conjunto y tupla:", conjunto_y_tupla) """

#Ejemplo
""" set_autores = set(["Federico García Lorca", "Miguel de Cervantes", "Paulo Coelho", "Miguel de Cervantes", "Rosa Chacel", "José Saramago"])
print(set_autores) """


#------------OPERACIONES CON CONJUNTOS-----------------
#Conjuntos de referencia
""" conjunto_uno = {1, 2, 3, 4, 5} 
conjunto_dos = {5, 2, 8, 4, 0}  """

#Ejemplo1
""" conjunto1 = {1, 3, 5, 4, 9}
conjunto2 = {2, 4, 6, 3, 0} """

#Union (|) o union(): Une los conjuntos, sin respetar el orden de inserción y también pudiendo mezclar los valores de ambos conjuntos en la salida del nuevo conjunto creado. Devuelve un nuevo conjunto que contenga todos los elementos que estén en al menos 1 conjunto.
""" union = conjunto_uno | conjunto_dos
union_dos = conjunto_uno.union(conjunto_dos)
print("Unión con tubería: ", union, "\nUnión con método union()", union_dos) """

#Ejemplo2
""" union1 = conjunto1 | conjunto2
union2 = conjunto1.union(conjunto2)
print("Unión con tubería:",union1,"\nUnión con método union:",union2) """

#Además
"""conjunto_mas_tupla = {1, 2, 3, (3, 5)}
print(conjunto_mas_tupla)"""

#Intersección (&) o .intersection(): Devuelve un nuevo conjunto que contiene todos los elementos que estan en los dos conjuntos.
""" interseccion = conjunto_dos & conjunto_uno
interseccion_dos = conjunto_uno.intersection(conjunto_dos)
print("Interseccion con &:", interseccion, "\nIntersección con método intersection():", interseccion_dos) """

#Ejemplo mío
""" intersection1 = conjunto1 & conjunto2
intersection2 = conjunto1.intersection(conjunto2)
print("Intersección con &:",intersection1,"\nIntersección con intersection:",intersection2) """

#Diferencia (-) o difference(): Devuelve un nuevo conjunto que contiene los elementos que están en el primer conjunto, pero no en el segundo.
""" diferencia = conjunto_dos - conjunto_uno
diferencia_dos = conjunto_uno.difference(conjunto_dos)
print("Diferencia entre conjuntos:\n Diferencia con - :\n", diferencia,"\nDiferencia con método difference():\n", diferencia_dos) """

#Mi ejemplo
""" diferencia1 = conjunto1 - conjunto2
diferencia2 = conjunto1.difference(conjunto2)
print("Diferencia con -:",diferencia1,"\nDiferencia con difference",diferencia2)
diferencia3 = conjunto2 - conjunto1
print("Diferencia cambiando el orden:",diferencia3) """

#Diferencia simétrica (^) o symmetric_difference(): Devuelve un nuevo conjunto que contenga todos los elementos que están en alguno de los conjuntos, pero no en ambos.
""" diferencia_simetrica = conjunto_uno ^ conjunto_dos
diferencia_simetrica_dos =  conjunto_dos.symmetric_difference(conjunto_uno)
print("Diferencia simétrica con ^:", diferencia_simetrica,"\nDiferencia simétrica con método symmetric_difference()", diferencia_simetrica_dos) """


#Mi ejemplo
""" diferencia_simetrica = conjunto1 ^ conjunto2
diferencia_simetrica_dos = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica con ^:",diferencia_simetrica,"\nDiferencia simétrica con symmetric_difference:",diferencia_simetrica_dos) """

#Subconjunto issubset(): Evaluamos si todos los elementos del primer conjunto están presentes en el segundo conjunto. Devuelve True si todos los elementos del primer están en el segundo y False de lo contrario.
""" conjunto_tres = {1, 2, 3, 4, 5} 
conjunto_cuatro = {1, 2, 3, 4, 5, 6, 7, 8} 
subconjunto = conjunto_tres.issubset(conjunto_cuatro)
print("Todos los valores del primer conjunto están presentes en el segundo:", subconjunto) #True """

#Superconjunto issuperset(): Evaluar si todos los elementos del segundo conjunto estan presentes en el primero. Devuelve True si todos los elementos del segundo conjunto están presentes en el primero
""" superconjunto = conjunto_tres.issuperset(conjunto_cuatro)
valores_diferentes = conjunto_cuatro - conjunto_tres
print("Todos los valores del segundo conjunto están presentes en el primero:", superconjunto, "porque al primer conjunto le faltan estos valores:", valores_diferentes)  """

#Ejemplos

"""conjunto3 = {1, 2, 3, 4, 5}
conjunto4 = {1, 2, 3, 4, 5, 6, 7, 8}
subconjunto = conjunto3.issubset(conjunto4)
print("¿Están todos los valores de conjunto3 en conjunto4?",subconjunto)
superconjunto = conjunto3.issuperset(conjunto4)
print("¿Contiene conjunto3 todos los valores de conjunto4?",superconjunto)
valores_faltantes = conjunto4 - conjunto3
print("conjunto3 no tiene todos los valores de conjunto4: le faltan",valores_faltantes) """

#*************** CONJUNTOS / SETS **********************

#Bucle For para iterar sobre los elementos de mi set/conjunto
""" conjunto_iterable = {5, 6, 7, 8}
for elemento in conjunto_iterable:
    print(elemento)
print(conjunto_iterable)

conjunto_iterable_dos = set([3, 4, 5, 6])
for elemento_dos in conjunto_iterable_dos:
    print(elemento_dos) """

#Comprobar si un valor esta presente en mi conjunto
""" presente_set = {"rojo", "azul", "verde"}
color_seleccionado = str(input("Introduce un color:\n"))
print(f"¿Esta el color {color_seleccionado} en mi set?",color_seleccionado in presente_set) """

#Ejemplo
""" conjunto = {1, 2, 3, 4}
for elemento in conjunto:
    print(elemento)
lo_que_busco = int(input("Elemento a buscar: "))
print(f"¿Está {lo_que_busco} en el conjunto?",lo_que_busco in conjunto)"""


#-----------------MÉTODOS DE SETS/CONJUNTOS---------------

#Método add(): Agregar un elemento al conjunto. Si el elemento que yo agrego YA EXISTE en el conjunto, no realizará ningún cambio. 
""" conjunto_aniade = {1, 2, 3}
conjunto_aniade.add(4)
conjunto_aniade.add(2)
print(conjunto_aniade) """

#Ejemplo 2
""" otro_conjunto = {"rojo", "azul", "amarillo"}
otro_conjunto.add("verde")
print(otro_conjunto) """

#Método remove(): Eliminar un elemento de mi conjunto pasándole el valor del elemento por argumentos. Si el elemento no está en mi conjunto, me devolverá un error. 
""" conjunto_borrar = {1, 2, 3}
conjunto_borrar.remove(2)
#conjunto_borrar.remove(4) #KeyError
print(conjunto_borrar) """

#Otro ejemplo
""" tercer_conjunto = {2, 4, 6}
tercer_conjunto.remove(2)
print(tercer_conjunto)
#tercer_conjunto.remove(8)
#print(tercer_conjunto)  #Este código arrojaría una excepción si se ejecutara """

#Método discard(): Eliminar un elemento de mi conjunto pasándole el valor del elemento por argumentos. Si el elemento no está en mi conjunto, NO REALIZA NINGUN CAMBIO Y TAMPOCO ME GENERA UN ERROR. 
""" conjunto_descartar = {1, 2, 3}
conjunto_descartar.discard(2)
conjunto_descartar.discard(4) #--> No me devuelve un KeyError
print(conjunto_descartar) """

#Otro ejemplo
""" cuarto_conjunto = {2, 4, 6}
cuarto_conjunto.remove(2)
cuarto_conjunto.discard(8)
print(tercer_conjunto) """

#Método clear(): Elimina TODOS los elementos de mi conjunto
""" conjunto_limpiar = {1, 2, 3, 4}
conjunto_limpiar.clear()
print(conjunto_limpiar) #Devuelve set() --> Un conjunto/set vacio """

#Ejemplo2
"""conjunto.clear()
otro_conjunto.clear()
tercer_conjunto.clear()
cuarto_conjunto.clear()
(print(conjunto,otro_conjunto,tercer_conjunto,cuarto_conjunto)) """

#Método len(): Devuelve la cantidad de elementos que están presentes en mi conjunto/set.
""" conjunto_longitud = {1, 2, 3, 4, 5, 7, 7, 6, 5, 6}
print("El número de elementos en mi conjunto es:", len(conjunto_longitud))
longitud = len(conjunto_longitud)
print("El número de elementos en mi conjunto es:", longitud) """

#Ejemplo
""" conjunto = {4, 6, 21, 9, 239, 2, 29, 29, 7}
largo = len(conjunto)
print("Tamaño del conjunto:",largo) """

#Método copy(): Crea una copia superficial del conjunto
""" conjunto_a_copiar = {9, 8, 7, 6}
conjunto_copiado = conjunto_a_copiar.copy()
print("Conjunto original: ", conjunto_a_copiar)
print("Conjunto copiado: ", conjunto_copiado) """

#Ejemplo2
""" conjunto_original = {34, 2, 23, 23, 17}
conjunto_copia = conjunto_original.copy()
print("Conjunto original:", conjunto_original)
print("Copia del conjunto original:",conjunto_copia) """

#Método update(): Nos permite agregar elementos de otro conjunto, de una lista o de otro iterable a nuestro conjunto actual. Como parámetros le pasamos el iterable cuyos elementos se van a agregar a mi conjunto actual. NO DEVUELVE UN NUEVO CONJUNTO, MODIFICA EL CONJUNTO ACTUAL.
""" conjunto_a_actualizar = {1, 2, 3, 4}
lista_a_agregar = [4, 5, 6]
conjunto_actualizado = conjunto_a_actualizar.update(lista_a_agregar)
print("Conjunto actualizado con lista nos devuelve None porque este método modifica el conjunto original pero no almacena o devuelve ningún otro valor explícito: ", conjunto_actualizado)
print("Conjunto actualizado con lista: ", conjunto_a_actualizar) """

#Mi ejemplo
""" conjunto = {1, 2, 3, 4}
lista = [4, 5]
conjunto.update(lista)
print(conjunto) """

#-----------------MÉTODOS DE PYTHON---------------

#Método split(): se utiliza EN CADENAS DE TEXTO para dividirlas en una lista de subcadenas. Podemos incluir el separador como parámetro y va a representar el caracter o la cadena que se utilizará como separador. Es opcional. Si no lo especificamos, el método split() va a tomar como referencia los espacios en blanco entre las palabras como separador por defecto.
#Separador "-"
""" frase_uno = "Hola-que tal"
lista_palabras_uno = frase_uno.split("-")
print("Lista de palabras separadas por guión: ", lista_palabras_uno) """
#Separador ","
""" frase_dos = "Hola,que,tal"
lista_palabras_dos = frase_dos.split(",")
print("Lista de palabras separadas por comas: ", lista_palabras_dos) """
#Sin separador
""" frase_tres = "Hola que tal"
lista_palabras_tres = frase_tres.split()
print("Lista de palabras sin separador: ", lista_palabras_tres) """

#Otro ejemplo
""" frase = "A ver, qué pasa, ¿y eso?"
separacion1 = frase.split()
separacion2 = frase.split(",")
separacion3 = frase.split("y")
print("Frase original:",frase)
print("Separación sin caracter a indicar:",separacion1)
print("Separación con comas:",separacion2)
print("Separación con letra y:",separacion3) """

#Update con split
""" conjunto = {"Hola", "Adiós"}
nuevo = ["Qué tal,familia"]
conjunto.update(nuevo[0].split(",")) #Separamos la frase en una lista de palabras
print("Nuevo conjunto: ", conjunto) """

#*************** DICCIONARIOS **********************
"""
Colecciones de datos que nos van a permitir almacenar elementos con formato "clave":valor.
Clave --> KEY, keys(): Siempre van entre comillas dobles, pueden ir también entre comillas simples, pero las reglas de estilo recomiendan dobles para las claves
Valor --> VALUE, values() :Siempre van entre comillas, pueden ir entre comillas dobles o simples, pero las reglas de estilo recomiendan simples para las claves
Elementos  --> Entries, items()
 """

#diccionario_vacio = {} #creamos un diccionario vacio
#conjunto_vacio = set()
""" mi_primer_diccionario = {
    "nombre": 'pepe',
    "edad":  30,
    "ciudad": "Málaga"
}
print(mi_primer_diccionario) """

#Crear un diccionario con método constructor dict()
""" mi_segundo_diccionario = dict([ 
    ("Nombre","Juan"), #Utilizamos comas para separar las claves y el valor
    ("apellido","Rodríguez"), #utilizamos comas para separar cada uno de los elementos de nuestros diccionarios (pares clave,valor), los cuales incluímos entre paréntesis
    ("Edad", 12)
])
print(mi_segundo_diccionario) """

#Crear un diccionario con método constructor dict() versión II:
""" mi_tercer_diccionario = dict(
    Nombre='Paco',
    Edad=45,
    Ciudad="Madrid"
)
print(mi_tercer_diccionario) """

""" diccionario_uno = {
    "Nombre": 'Juan Raimundo',
    "Apellido": 'Álvaro Núñez',
    "Edad": 42,
    "Ciudad": 'Betanzos',
    "Provincia": 'A Coruña'
}

diccionario_dos = dict([
    ("Nombre",'Juan Raimundo'),
    ("Apellidos",'Álvaro Núñez'),
    ("Edad",42),
    ("Residencia",'Betanzos'),
    ("Provincia",'A Coruña')
])

diccionario_tres = dict(
    Nombre="Juan Raimundo",
    Apellidos="Álvaro Núñez",
    Edad=42,
    Ciudad="Betanzos",
    Comunidad="Galicia"
)

print(diccionario_uno)
print(diccionario_dos)
print(diccionario_tres)

dic1 = {
    "Juan":'nombre',
    "Álvaro":'apellido',
    "núñez":'segundo_apellido'
}

dic2 = dict([
    ("Edad", 3),
    ("Nombre", 'Juan'),
    ("Apellidos", 'álvaro núñez')
])

dic3 = dict(
    Nombre='Juan',
    Apellido='Álvaro',
    Edad=32
)

print(dic1, dic2, dic3)"""

#Accedo a los valores de un diccionario por clave en formato index
""" valor_nombre = mi_tercer_diccionario["Nombre"] 
print(valor_nombre) """

#Accedo a los valores de un diccionario por clave con el método get() al cual le pasamos como parámetro la clave a la que quiero acceder.
""" valor_edad = mi_tercer_diccionario.get("Edad")
print("La edad de Paco el de las naranjas es:", valor_edad) """

#Modificar un diccionario
""" diccionario_modificable = {
    "Nombre": "Pepa",
    "Edad": 50,
    "Ciudad": "Barcelona"
}
diccionario_modificable["Nombre"] = "María"  """
#diccionario_modificable.get("Edad") = 23 --> SyntaxError porque get() directamente no me va a permitir cambiar el dato
#diccionario_modificable["Carnet"] = True #Cuando accedo a un KEY que no existe, se añade automáticamente al diccionario
"""print(diccionario_modificable)"""

"""INCISO"""

#Modificar la cadena a capitalize() #hacer que la primera palabra del string comience en mayúscula
""" nombre_capitalize = valor_nombre.capitalize()
print("Esto es un capitalize:",nombre_capitalize) """

#Modificar la cadena a title() #hacer que todas las palabras del string comiencen en mayúscula
"""nombre_title = valor_nombre.title()
print("Esto es un título:",nombre_title)"""

""" valor_nombre = dic2["Apellidos"]
print(valor_nombre.capitalize())

valor_nombre = dic2["Apellidos"]
print(valor_nombre.title()) 

 """
#Los diccionarios pueden ser anidados
"""diccionario_anidado = {
    "clave": {
        "valor1": "dato1",
        "valor2": "dato2",
        "valor3": "dato3",
    },
    "clave2": "string1"
}
"""

#Ejemplo

""" diccionario_anidado = {
    "persona1":{
        "Nombre":"Juan",
        "Apellido":"Álvaro"
    },
    "persona2":{
        "Nombre":"María",
        "Apellido":"González"
    },
    "persona3":{
        "Nombre":"Alejandra",
        "Apellido":"Espinosa"
    },
    "persona4":{
        "Nombre":"Gema",
        "Apellido":"Carmona"
    }
}

print(diccionario_anidado)"""

""" anidado_dos = {
    "Persona":{
        "Nombre":'Juan',
        "Apellido":'Álvaro'
    },
    "Profesión":'Empresario'
}
print(anidado_dos) """


""" edad = diccionario_uno.get("Edad")
print("Edad de Juan:",edad)
edad2 = diccionario_dos["Edad"]
print("Edad de Juan",edad2)

diccionario_mutable = {
    "Nombre": 'Juan',
    "Apellido": 'Álvaro',
    "Edad": 42
}

diccionario_mutable["Nombre"] = "Juan Raimundo"
diccionario_mutable["Ciudad"] = "Betanzos"
print(diccionario_mutable) """

#¿Qué debo tener en cuenta al definir las claves de mis diccionarios?

"""· Naming: Es recomendable utilizar nombres descriptivos y significativos para las claves, de modo que reflejen el tipo de datos que representan. Por ejemplo, en un diccionario que almacena información de una persona, las claves podrían ser 'nombre', 'apellido', 'edad', etc.

· Duplicados: Las claves en un diccionario deben ser únicas. Si se intenta agregar una clave que ya existe, el valor asociado con esa clave se actualizará con el nuevo valor. Por lo tanto, es importante asegurarse de que las claves sean únicas para evitar la pérdida de datos.

· Inmutabilidad (de las claves de un diccionario, no de los valores, los valores son mutables): Las claves de un diccionario deben ser objetos inmutables, lo que significa que no pueden cambiar de valor después de ser creadas. Esto generalmente limita las claves a tipos de datos inmutables como cadenas, enteros y tuplas. Las listas y otros diccionarios no pueden usarse como claves porque son mutables.

· Hashable: Para que un objeto pueda ser utilizado como clave en un diccionario, debe ser "hashable", es decir, debe poder generar un valor hash único que se utilizará para buscar y almacenar la clave en la tabla hash interna del diccionario. 

· Caracteres especiales: Las claves de un diccionario pueden incluir caracteres especiales como guiones bajos (_), guiones (-), números, letras y otros caracteres especiales, siempre que cumplan con las reglas de nomenclatura de Python y sean "hashable"."""

#Acceder a diccionarios anidados: Para acceder a los elementos de los diccionarios anidados al diccionario principal, simplemente utilizamos la notación de corchetes [ ] y el nombre de la clave correspondiente. Podemos acceder a cualquier nivel de anidación dentro del diccionario principal utilizando la notación de corchetes y las claves adecuadas.
contacto = {
    'nombre': 'Juan',
    'apellido': 'Gómez',
    'edad': 30,
    'telefono': '123456789',
    'nombre': 'Pepe', #En claves modificadas prevalece el valor que sea dispuesto en último lugar
    'email': 'juan@example.com',
    'direccion': {
        'calle': 'Calle Principal',
        'numero': '123',
        'ciudad': 'Ciudad Principal',
        'codigo_postal': '12345',
        'pais': 'País Principal'
    },
    'redes_sociales': {
        'twitter': '@juan_gomez',
        'facebook': 'JuanGomez',
        'instagram': 'juangomezofficial'
    },
    'intereses': ['viajes', 'lectura', 'deporte']
}

# Acceder al número de teléfono
"""print("Teléfono:", contacto['telefono'])"""

# Acceder al número de casa de la dirección
"""print("Número de casa:", contacto['direccion']['numero'])"""

# Acceder al código postal
"""print("El código postal es:",contacto['direccion']['codigo_postal'])"""

# Acceder a la ciudad principal
"""print("La ciudad principal es:",contacto['direccion']['ciudad'])"""

# Acceder al nombre de usuario de Twitter
"""print("Usuario de Twitter:", contacto['redes_sociales']['twitter'])"""

# Acceder al primer interés
"""print("Primer interés:", contacto['intereses'][0])"""



#--------------------MÉTODOS DICCIONARIOS------------------

#Método clear(): Elimina todos los elementos del diccionario, dejándolo vacío.
diccionario = {'a': 1, 'b': 2, 'c': 3}
"""diccionario.clear()
print(diccionario)  # Salida: {}"""

#Método copy(): Devuelve una copia superficial del diccionario.
"""diccionario_copia = diccionario.copy()
print(diccionario_copia)  # Salida: {'a': 1, 'b': 2, 'c': 3}"""

#Método get(): devuelve el valor de una clave especificada. Si la clave no existe, devuelve un valor predeterminado (None si no se especifica otro valor)
""" valor = diccionario.get('b')
print(valor)  # Salida: 2 """

#Método items(): Devuelve todos los pares clave-valor en el diccionario como tuplas.
""" pares = diccionario.items()
print(pares)  # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)]) """

#Método keys(): Devuelve una lista de todas las claves en el diccionario.
""" claves = diccionario.keys()
print(claves)  # Salida: dict_keys(['a', 'b', 'c']) """

#Método values(): Devuelve todos los valores en el diccionario.
""" valores = diccionario.values()
print(valores)  # Output: dict_values([1, 2, 3]) """

#Método pop(): Elimina un elemento por su clave y devuelve su valor. Si la clave no existe, lanza una excepción KeyError. ELIMINA + ALMACENA EL VALOR ELIMINADO
""" diccionario = {'a': 1, 'b': 2, 'c': 3}
valor_eliminado = diccionario.pop('a')
print("Valor eliminado: ", valor_eliminado, "\n Diccionario sin el valor 'a':", diccionario) """

#Método popitem(): Elimina y devuelve el último par clave-valor insertado en el diccionario. La salida de este par será una tupla. Si el diccionario esta vacio, nos va arrojar un KeyError. NO ADMITE ARGUMENTOS
""" par_eliminado = diccionario.popitem()
print("\n Par eliminado: ", par_eliminado, "\n Diccionario sin los valores del par eliminado:", diccionario)
par_eliminado_dos = diccionario.popitem() #Aquí el diccionario se queda vacio
#par_eliminado_tres = diccionario.popitem() --> KeyError: 'popitem(): dictionary is empty
print("diccionario final:", diccionario) """

#update(): Este método actualiza el dicionario con los elementos de otro diccionario. También puede actualizar el diccionario con pares CLAVE=VALOR proporcionados al métodos como argumentos (de palabra clave)
""" diccionario_uno = {'a': 1, 'b': 2}
diccionario_dos = {'c': 3, 'd': 4}
diccionario_uno.update(diccionario_dos)
print("\nDiccionario uno:", diccionario_uno, "\nDiccionario dos:", diccionario_dos)
diccionario_dos.update(diccionario_uno)
print("\nDiccionario uno, 2º parte:", diccionario_uno, "\nDiccionario dos. 2º parte:", diccionario_dos)
diccionario_uno.update(e=5, f=6)
print(diccionario_uno)"""

#Método setdefault(): Devuelve el valor de UNA clave que nosotros le especificamos pasándola como argumento. A diferencia del método get(), si la clave no existe, nos la va a insertar en el diccionario con el valor que le hemos especificado (Si no le especificamos un valor, la incluye con el valor None)
""" valor_setdefault = diccionario_uno.setdefault('g', 20)
valor_setdefault_dos = diccionario_uno.setdefault('h', 10)
valor_setdefault_tres = diccionario_uno.setdefault('i')
print(valor_setdefault)
print(valor_setdefault_dos)
print(valor_setdefault_tres)
print(diccionario_uno) """

#Ejemplos
""" total_contactos = contacto.items()
total_claves = contacto.keys()
total_valores = contacto.values()

print("Contactos totales:\n",total_contactos)
print("Claves totales:\n",total_claves)
print("Valores totales:\n",total_valores)

valor1 = contacto.get("nombre")

print(valor1) """

""" elimino_valor = diccionario.pop('b')
print("Valor eliminado:",elimino_valor,"\nDiccionario actualizado:", diccionario)

elimino_valor_dos = diccionario.popitem()
print("Valor eliminado:", elimino_valor_dos,"\nDiccionario actualizado",diccionario)

elimino_valor_tres = diccionario.popitem()
print("Valor eliminado:", elimino_valor_tres,"\nDiccionario actualizado:",diccionario)

elimino_valor_cuatro = diccionario.popitem()
print("Valor eliminado:",elimino_valor_cuatro,"\nDiccionario actualizado:",diccionario)

dictionary_one = {"one": 1, "two": 2}
dictionary_two = {"three": 3, "four": 4}
dictionary_one.update(dictionary_two)
print("Diccionario 1:",dictionary_one,"\nDiccionario 2:",dictionary_two)
dictionary_two.update(dictionary_one)
print("Diccionario 1 again:",dictionary_one,"\nDiccionario 2 again:",dictionary_two)
dictionary_one.update(five=5, six=6)
print(dictionary_one)
valor_setdefault = dictionary_one.setdefault("five")
print(valor_setdefault)
valor_setdefault_dos = dictionary_one.setdefault('seven', 7)
print(valor_setdefault_dos)
valor_setdefault_tres = dictionary_one.setdefault('eight')
print(valor_setdefault_tres)
print(dictionary_one)
dictionary_one.update(eight=8)
print(dictionary_one) """

#------------ITERANDO UN DICCIONARIO------------
#Bucle for: En Python se utiliza para iterar sobre una secuencia (listas, tuplas o diccionarios), con el objetivo de ejecutar un bloque de código una vez para cada uno de los elementos de esa secuencia. Sintaxis:

"""for elemento in secuencia:
    # Bloque de código a ejecutar
"""

#Ejemplo de iteración básica sobre un diccionario (solo una variable que empaqueta todo el elemento)
""" diccionario = {
    'perro': 'animal que ladra',
    'gato': 'animal que maulla',
    'pájaro': 'animal que pia'
    } """

""" for elemento in diccionario: #Cuando estoy iterando sobre un diccionario, el bucle for de forma predeterminada itera sobre las claves. Es decir, cuando estamos iterando sobre un diccionario que contiene elementos (pares CLAVE - VALOR), la variable que definimos para identificar cada uno de esos elementos itera sobre la clave
    print(elemento, ":", diccionario[elemento]) """

#Iterando diccionarios con el método items(): Este método devuelve cada uno de los elementos del diccionario como una tupla. Por ende, cada tupla tiene dos objetos dentro (la clave y el valor)
""" for clave, valor in diccionario.items():
    print(clave, ":", valor) """


#Iterando diccionarios con el método keys(): Este método en iteraciones sobre diccionarios nos va a devolver las claves del diccionario. 
""" for clave in diccionario.keys():
    print("La clave es: ", clave)
    print("El valor es:", diccionario[clave]) #Como no estoy iterando sobre los valores en el bucle for, para poder acceder a ellos necesitaré hacerlo a través de la clave """

#Iterando diccionarios con el método values(): Este método en iteraciones sobre diccionarios nos va a devolver los valores del diccionario. 
""" for valor in diccionario.values():
    print("-El valor es: ", valor) """

""" semana = {
    "Primer día": "Lunes",
    "Segundo día": "Martes",
    "Tercer día": "Miércoles",
    "Cuarto día": "Jueves",
    "Quinto día": "Viernes",
    "Sexto día": "Sábado",
    "Séptimo día": "Domingo",
}

for dia in semana:
    print(dia,":",semana[dia])

for dia, nombre in semana.items():
    print(dia,":",nombre)

for dia in semana.keys():
    print("El orden del día es:",dia)
    print("El día se llama", semana[dia]) #Es un extra que no existe al revés en values()

for nombre in semana.values():
    print("El día de la semana se llama:",nombre)

ventas_enero = {
    "ratón": 70,
    "teclados": 100,
    "pantallas": 50
}
productos_vendidos = 0

for producto, cantidad in ventas_enero.items():
    productos_vendidos += cantidad

print(productos_vendidos)

productos_vendidos_dos = 0

for cantidad in ventas_enero.values():
    productos_vendidos_dos += cantidad

print(productos_vendidos_dos)

productos_vendidos_tres = 0

for producto in ventas_enero.keys():
    productos_vendidos_tres += ventas_enero[producto]

print(productos_vendidos_tres) """