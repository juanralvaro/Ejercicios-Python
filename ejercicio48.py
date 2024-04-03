""" Vamos a crear un programa que utilice un diccionario para gestionar información sobre libros en una biblioteca. Cada libro estará representado por su título como clave y el número de ejemplares disponibles como valor.

1. Define un diccionario llamado **`biblioteca`** con al menos cinco libros y la cantidad de ejemplares disponibles para cada uno.
2. Implementa una función llamada **`prestar_libro`** que acepte el título de un libro y la cantidad de ejemplares que se van a prestar. La función deberá restar la cantidad prestada del total de ejemplares disponibles. Asegúrate de manejar casos en los que la cantidad prestada sea mayor que la cantidad disponible.
3. Implementa una función llamada **`devolver_libro`** que acepte el título de un libro y la cantidad de ejemplares que se van a devolver. La función deberá sumar la cantidad devuelta al total de ejemplares disponibles. Asegúrate de manejar casos en los que la cantidad devuelta sea mayor que la cantidad prestada.
4. Implementa una función llamada **`ver_inventario`** que imprima todos los libros en la biblioteca y la cantidad de ejemplares disponibles.
5. Utiliza las funciones para realizar operaciones de préstamo, devolución e imprimir el inventario.

*Ejemplo de salida:*

*¡Libro 'Python for Beginners' prestado (3 ejemplar(es))!
No hay suficientes ejemplares de 'History of World Wars' para el préstamo.
¡Libro 'Python for Beginners' devuelto (2 ejemplar(es))!
No se puede devolver 'Introduction to Poetry' porque no está en el inventario.*

*Inventario de la Biblioteca:
Python for Beginners: 8 ejemplar(es)
Data Science 101: 5 ejemplar(es)
The Art of Fiction: 8 ejemplar(es)
History of World Wars: 12 ejemplar(es)
Introduction to Poetry: 7 ejemplar(es)* """

# Diccionario de libros en la biblioteca
biblioteca = {
    'Python for Beginners': 10,
    'Data Science 101': 5,
    'The Art of Fiction': 8,
    'History of World Wars': 12,
    'Introduction to Poetry': 7
}

# Función para prestar un libro
def prestar_libro(titulo, cantidad_prestada):
    """
    1 - Objetivo
    El objetivo de la función es prestar un libro. En esta ocasión no retorna nada.
    2 - Argumentos
    - titulo (str): Es el título del libro que se quiere prestar.
    - cantidad_prestada (int): Es la cantidad de libros que se van a prestar.
    3 - Qué retorna
    No retorna nada al ser "prestar libro" algo abstracto.
    """
    if titulo in biblioteca and biblioteca[titulo] >= cantidad_prestada:
        biblioteca[titulo] -= cantidad_prestada
        print(f"¡Libro '{titulo}' prestado ({cantidad_prestada} ejemplar(es))!")
    else:
        print(f"No hay suficientes ejemplares de '{titulo}' para el préstamo.")

# Función para devolver un libro
def devolver_libro(titulo, cantidad_devuelta):
    """
    1 - Objetivo
    El objetivo de la función es devolver un libro. En esta ocasión no retorna nada.
    2 - Argumentos
    - titulo (str): Es el título del libro que se quiere devolver.
    - cantidad_devuelta (int): Es la cantidad de libros que se van a devolver.
    3 - Qué retorna
    No retorna nada al ser "devolver libro" algo abstracto.
    """
    if titulo in biblioteca:
        biblioteca[titulo] += cantidad_devuelta
        print(f"¡Libro '{titulo}' devuelto ({cantidad_devuelta} ejemplar(es))!")
    else:
        print(f"No se puede devolver '{titulo}' porque no está en el inventario.")

# Función para ver el inventario de la biblioteca
def ver_inventario():
    """
    1 - Objetivo
    Ver el inventario de la biblioteca.
    2 - Argumentos
    - No se usan argumentos.
    3 - Qué retorna
    No retorna nada. Imprime por pantalla los títulos y las cantidades de cada uno.
    """
    print("Inventario de la Biblioteca:")
    for libro, cantidad in biblioteca.items():
        print(f"{libro}: {cantidad} ejemplar(es)")

# Préstamo de libros
prestar_libro('Python for Beginners', 3)
prestar_libro('History of World Wars', 10)  # Intento de préstamo excesivo

# Devolución de libros
devolver_libro('Python for Beginners', 2)
devolver_libro('Introduction to Poetry', 5)  # Intento de devolución excesiva

# Ver el inventario actualizado
ver_inventario()

#SOLUCIÓN ALTERNATIVA

# David ejercicio 49
""" blibio_libros = {"libro1": 10, "libro2": 10 , "libro3": 50 , "libro4": 30, "libro5": 20}


def prestar_libro():
   libro = input("Dinos que libro quieres\n")
   if libro in blibio_libros:
      cantidad = int(input(f"cuantos ejemplares necesitas del libro {libro}\n"))
      if cantidad > blibio_libros[libro]:
          print("no tenemos tantos ejemplares")
      else:
         blibio_libros[libro] -=  cantidad
         print(blibio_libros)
         
   else:
      print("No tenemos este libro")

def devolver_libro():
   libro = input("Dinos que libro devuelves\n")
   if libro in blibio_libros:
      cantidad = int(input(f"cuantos ejemplares devuelves del libro {libro}\n"))
      blibio_libros[libro] +=  cantidad
      print(blibio_libros)
   else:
      print("No tenemos este libro en el archivo")

def ver_inventario():
   print(blibio_libros)

prestar_libro()
devolver_libro()
ver_inventario() """