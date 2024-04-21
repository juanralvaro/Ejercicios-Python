#BONUS TRACK: El usuario debe introducir cuantas filas y columnas quiere en su cuadrado vacío
"""

*****
*   *
*   *
*   *
***** 

"""

altura = int(input("Introduce la altura: "))
anchura = int(input("Introduce la anchura: "))
for i in range(altura): #si altura = 7:  0, 1, 2, 3, 4, 5, 6
    for j in range(anchura): #si anchura = 6:  0, 1, 2, 3, 4, 5
        if i == 0 or i == altura -1 or j == 0 or j == anchura-1:
            print ("*",end="")
        else:
            print (" ", end="")
    print()


""" Por cada valor que encuentres en los valores 0 - 5, ejecuta el siguiente código:
    --> Primera columna - Iteración j == 0: True
    --> Segunda columna - Iteración j == 1: False
    --> Tercera columna - Iteración j == 2: False
    --> Cuarta columna - Iteración j == 3: False
    --> Quinta columna - Iteración j == 4: False
    --> Sexta columna - Iteración j == 5: True
    
Lo ejecuta tantas veces como indica el bucle externo, donde la primera y la última vez (iteración i == 0 e i == 6) lo llenará todo de estrellas.
    
******
*    * 
*    * 
*    * 
*    * 
*    * 
******
 
 """