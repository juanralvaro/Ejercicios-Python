""" Escribe un programa en Python que realice las siguientes operaciones con conjuntos:

1. **Creación de conjuntos:**
    - Crea dos conjuntos llamados **`set1`** y **`set2`** con al menos tres elementos cada uno.
2. **Unión de conjuntos:**
    - Realiza la unión de los conjuntos **`set1`** y **`set2`** y almacena el resultado en un nuevo conjunto llamado **`union`**.
3. **Intersección de conjuntos:**
    - Encuentra la intersección entre los conjuntos **`set1`** y **`set2`** y almacena el resultado en un nuevo conjunto llamado **`interseccion`**.
4. **Diferencia de conjuntos:**
    - Encuentra la diferencia entre los conjuntos **`set1`** y **`set2`** (elementos en **`set1`** pero no en **`set2`**) y almacena el resultado en un nuevo conjunto llamado **`diferencia`**.
5. **Diferencia simétrica de conjuntos:**
    - Encuentra la diferencia simétrica entre los conjuntos **`set1`** y **`set2`** (elementos que están en uno de los conjuntos pero no en ambos) y almacena el resultado en un nuevo conjunto llamado **`diferencia_simetrica`**.
6. **Subconjunto:**
    - Verifica si el conjunto **`set1`** es un subconjunto del conjunto **`set2`** y muestra el resultado.
7. **Superconjunto:**
    - Verifica si el conjunto **`set1`** es un superconjunto del conjunto **`set2`** y muestra el resultado.
8. **Mostrar resultados:**
    - Muestra los conjuntos resultantes **`union`**, **`interseccion`**, **`diferencia`** y **`diferencia_simetrica`**, así como los resultados de las verificaciones de subconjunto y superconjunto. """

#Creación de programa para operar con conjuntos
print("Bienvenido al programa Venn de operación de conjuntos.\n")

#1. Creación de conjuntos
set1 = {1, 5, 2, 11, 23}
set2 = {3, 5, 6, 8, 11}

#2. Unión de conjuntos
union = set1 | set2 #o union = set1.union(set2)

#3. Intersección de conjuntos
interseccion = set1 & set2 #o interseccion = set1.intersection(set2)

#4. Diferencia de conjuntos
diferencia = set1 - set2 #o diferencia = set1.difference(set2)

#5. Diferencia simétrica de conjuntos
diferencia_simetrica = set1 ^ set2  #o diferencia_simetrica = set1.symmetric_difference(set2)

#6. Subconjunto
subconjunto = set1.issubset(set2) #(sin operador alternativo)

#7. Superconjunto
superconjunto = set1.issuperset(set2) #(sin operador alternativo)

#8. Muestra de resultados
print("La unión de set1 y set2 es:",union)
print("La intersección de set1 y set2 es:",interseccion)
print("La diferencia de set1 y set2 es:",diferencia)
print("La diferencia simétrica de set1 y set2 es:",diferencia_simetrica)
print("Subconjunto: ¿es set1 un subconjunto de set2?:",subconjunto)
print("Superconjunto: ¿es set1 un superconjunto de set2?:",superconjunto)