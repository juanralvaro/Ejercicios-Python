#RETOS

"""1. Crea dos conjuntos/sets nuevos dentro de un conjunto.
2. Accede a uno de los elementos de tu conjunto y modifícalo."""

#Reto 1. 1. Definimos dos conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}

#2. Creamos un conjunto que contenga los dos conjuntos anteriores

#TAL CUAL ESTÁ DEFINIDO, NO SE PUEDE RESOLVER: LOS CONJUNTOS SON INMUTABLES.
#HABRÍA QUE CONVERTIRLOS EN TUPLAS PARA RESOLVERLO
tupla1 = tuple(conjunto1)
tupla2 = tuple(conjunto2)
conjunto_de_conjuntos = {tupla1, tupla2}
print(conjunto_de_conjuntos)

#Reto 2. 1. Unión de conjuntos
#TAL CUAL ESTÁ DEFINIDO, NO SE PUEDE RESOLVER: LOS CONJUNTOS SON IMUTABLES
#HABRÍA QUE CONVERTIRLOS EN LISTAS PARA RESOLVERLO
list1 = list(conjunto1)
list1[0] = 7
conjunto1 = set(list1)
print(conjunto1)