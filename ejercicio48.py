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

diccionario_libros = {"El Quijote" : 2, "La sombra del viento": 6, "Futbolísimos": 8, "Reina Roja": 1, "Fariña": 5}

# Función para prestar un libro
def prestar_libro(titulo, cantidad_prestada):
    if titulo in diccionario_libros and diccionario_libros[titulo] >= cantidad_prestada:
        diccionario_libros[titulo] -= cantidad_prestada
        print(f"¡Libro '{titulo}' prestado ({cantidad_prestada} ejemplar(es))!")
    else:
        print(f"No hay suficientes ejemplares de '{titulo}' para el préstamo.")

prestar_libro("El Quijote",1)
prestar_libro("El Quijote",1)
prestar_libro("El Quijote",1)

def retornar_libro(titulo, cantidad_prestada):
    if titulo in diccionario_libros and diccionario_libros[titulo] <= cantidad_prestada:
        diccionario_libros[titulo] += cantidad_prestada
        print(f"¡Libro '{titulo}' retornado ({cantidad_prestada} ejemplar(es))!")
    else:
        print(f"¡No tenemos tantos ejemplares de '{titulo}'!")

retornar_libro("El Quijote",1)
retornar_libro("El Quijote",1)
retornar_libro("El Quijote",1)

""" retorno = retornar_libro
print(retorno)
 """
def ver_inventario(diccionario_libros):
    for clave, valor in diccionario_libros.items():
        print(clave,":",valor)
        
ver_inventario(diccionario_libros)