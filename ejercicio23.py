""" Vamos a trabajar con una tupla que representa las temperaturas diarias de una ciudad durante una semana. La tupla se llama **`temperaturas`** y contiene valores en grados Celsius. Realiza las siguientes tareas:

1. Crea una tupla llamada **`temperaturas`** con al menos 7 valores de temperaturas diarias.
2. Imprime la longitud de la tupla.
3. Utiliza el método **`count`** para determinar cuántas veces aparece la temperatura 25 en la tupla.
4. Encuentra el índice de la primera aparición de la temperatura 18 utilizando el método **`index`**.
5. Crea una nueva tupla llamada **`temperaturas_ordenadas`** que contenga las temperaturas ordenadas de manera ascendente de la tupla **`temperaturas`**.
6. Concatena la tupla original con la nueva tupla **`temperaturas_ordenadas`**.
7. Repite la tupla original tres veces y almacénala en una nueva tupla llamada **`temperaturas_repetidas`**.
8. Imprime todas las tuplas resultantes y observa los cambios.

**Nota:** Asegúrate de utilizar los métodos y operadores vistos en clase. """

#1. Creación tupla
temperaturas = 23, 25, 29, 26, 12, 18, 14, 25, 12, 25

#2. Impresión tupla original
print("Longitud tupla original:",len(temperaturas))

#3. Contar las veces que aparece el valor 25
veces_valor_veinticinco = temperaturas.count(25)
print("Veces valor 25:",veces_valor_veinticinco)

#4. Encontrar índice del primer valor 18
primer_indice_dieciocho = temperaturas.index(18)
print("Primer índice valor 18:",primer_indice_dieciocho)

#5. Crear tupla temperaturas_ordenadas
ordenar_temperaturas = sorted(temperaturas)
temperaturas_ordenadas = tuple(ordenar_temperaturas)

#6. Concatenar tupla original y ordenada
concatenacion_tupla_original_y_ordenada = temperaturas + temperaturas_ordenadas

#7. Multiplicar tupla original y almacenarla en una nueva
temperaturas_repetidas = temperaturas * 3

#8. Imprimir tuplas resultantes
print("Tupla temperaturas:",temperaturas)
print("Tupla temperaturas ordenadas:",temperaturas_ordenadas)
print("Tuplas concatenadas:",concatenacion_tupla_original_y_ordenada)
print("Tupla repetida:",temperaturas_repetidas)