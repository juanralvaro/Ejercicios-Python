""" Vamos a comparar los métodos de conjuntos y tuplas en Python. Para ello, sigue los siguientes pasos:

1. Define una tupla llamada **`tupla_numeros`** que contenga al menos 5 números enteros.
2. Define un conjunto llamado **`conjunto_numeros`** que contenga los mismos números que la tupla **`tupla_numeros`**.
3. Utiliza el método **`add()`** para agregar un nuevo número al conjunto **`conjunto_numeros`**.
4. Utiliza el método **`remove()`** para eliminar un número específico del conjunto **`conjunto_numeros`**.
5. Utiliza el método **`union()`** para unir el conjunto **`conjunto_numeros`** con otro conjunto que contenga algunos números adicionales.
6. Utiliza el método **`intersection()`** para encontrar la intersección entre el conjunto **`conjunto_numeros`** y otro conjunto que tenga algunos números en común y algunos números diferentes.
7. Utiliza el método **`difference()`** para encontrar la diferencia entre el conjunto **`conjunto_numeros`** y otro conjunto que tenga algunos números en común y algunos números diferentes.
8. Utiliza el método **`symmetric_difference()`** para encontrar la diferencia simétrica entre el conjunto **`conjunto_numeros`** y otro conjunto que tenga algunos números en común y algunos números diferentes.
9. Convierte la tupla **`tupla_numeros`** en un conjunto utilizando la función **`set()`** y realiza las mismas operaciones que realizaste con el conjunto **`conjunto_numeros`**.
10. Compara los resultados obtenidos y observa las diferencias en el comportamiento de los métodos entre conjuntos y tuplas. """

#1. Definir tupla
tupla_numeros = (1, 5, 2, 8, 3)
print("Tupla números: ", tupla_numeros)

#2. Definir conjunto
conjunto_numeros = {1, 5, 2, 8, 3}
print("Conjunto números: ", conjunto_numeros)

#3. Añadir a conjunto
conjunto_numeros.add(9)
print("Conjunto después de añadir 9: ", conjunto_numeros)

#4. Quitar de conjunto
conjunto_numeros.remove(8)
print("Conjunto después de quitar 8: ", conjunto_numeros)

#5. Unir conjunto
conjunto_a_unir = {7, 0, 11}
conjunto_numeros.union(conjunto_a_unir)
print("Unión entre conjuntos: ", conjunto_numeros.union(conjunto_a_unir))

#6. Intersección de conjuntos
conjunto_a_desunir = {2, 6, 3}
conjunto_numeros.intersection(conjunto_a_desunir)
print("Intersección entre conjuntos: ", conjunto_numeros.intersection(conjunto_a_desunir))

#7. Diferencia de conjuntos
conjunto_a_diferenciar = {1, 4, 6, 8}
conjunto_numeros.difference(conjunto_a_diferenciar)
print("Diferencia de conjuntos: ", conjunto_numeros.difference(conjunto_a_diferenciar))

#8. Diferencia simétrica de conjuntos
conjunto_a_diferenciar_simetricamente = {1, 5, 8, 7}
conjunto_numeros.symmetric_difference(conjunto_a_diferenciar_simetricamente)
print("Diferencia simétrica de conjuntos: ", conjunto_numeros.symmetric_difference(conjunto_a_diferenciar_simetricamente))

#9. Conversión de tupla a conjunto y realización de operaciones
conjunto_desde_tupla = set(tupla_numeros)
print(conjunto_desde_tupla)

conjunto_desde_tupla.add(9)
print("Conjunto desde tupla después de añadir 9: ",conjunto_desde_tupla)

conjunto_desde_tupla.remove(8)
print("Conjunto desde tupla después de quitar 8: ",conjunto_desde_tupla)

conjunto_a_unir = {7, 0, 11}
conjunto_desde_tupla.union(conjunto_a_unir)
print("Unión del conjunto desde tupla con otro: ", conjunto_desde_tupla.union(conjunto_a_unir))

conjunto_a_desunir = {2, 6, 3}
conjunto_desde_tupla.intersection(conjunto_a_desunir)
print("Intersección del conjunto desde tupla con otro: ", conjunto_desde_tupla.intersection(conjunto_a_desunir))

conjunto_a_diferenciar = {1, 4, 6, 8}
conjunto_desde_tupla.difference(conjunto_a_diferenciar)
print("Diferencia de conjunto desde tupla: ", conjunto_desde_tupla.difference(conjunto_a_diferenciar))

conjunto_a_diferenciar_simetricamente = {1, 5, 8, 7}
conjunto_desde_tupla.symmetric_difference(conjunto_a_diferenciar_simetricamente)
print("Diferencia simétrica de conjuntos: ", conjunto_desde_tupla.symmetric_difference(conjunto_a_diferenciar_simetricamente))

#10. Diferencias
print("Tal y como está definido el ejercicio, no hay diferencias... más allá de que los elementos de las tuplas están desordenados y los de los conjuntos no.")