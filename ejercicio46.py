#RETO DE LA PIRÁMIDE

""" Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. Luego, utiliza un bucle **`for`** y el parámetro **`end`** en la función **`print()`** para imprimir un patrón de asteriscos con forma de pirámide, como se muestra en el ejemplo a continuación:

Si el usuario introduce el número 5 la salida debería ser:

```python
    *
   ***
  *****
 *******
*********
```

1. Solicita al usuario ingresar un número entero positivo que representará la altura de la pirámide.
2. Utiliza un bucle **`for`** para iterar sobre cada fila de la pirámide.
3. En cada iteración del bucle, imprime una cadena de asteriscos con un número creciente de asteriscos, seguido de un espacio en blanco, y especifica el parámetro **`end`** de la función **`print()`** para que no haya salto de línea después de imprimir cada fila.

Recuerda validar la entrada del usuario para garantizar que sea un número entero positivo. """

""" filas = int(input("Introduce el número de filas: "))

for i in range(1, filas + 1):
    print(" " * (filas - i) + "*" * (2 * i - 1), end = " ")
    print() """

altura = int(input("Altura: "))

for i in range(1, altura + 1): # empiezo con la primera posicion hasta la posicion que escribe altura
    for j in range(altura - i):
        print(" ", end="") # cada vez que imprimo pues elimino  el espacio de la ultima columna.
    for k in range(i): # 0, 1, 2,...
        print("*", end=" ") # y aqui pues se crea # 
    print()