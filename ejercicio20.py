""" Bienvenidos al primer reto de programación del curso. Para este reto, al ser un ejercicio en grupo, el objetivo es que utilicéis no solo los conocimientos que habéis adquirido, si no también vuestra imaginación. 

El reto consiste en crear un programa, de temática libre, que incluya en la lógica del programa toda la sintaxis que hemos visto hasta ahora. A saber:

- Métodos de entrada y salida de información: print() e input()
- Métodos para formateo de cadenas de caracteres: lower() y upper()
- Operadores de Python
- Colecciones de datos: listas
- Bucle for iterando sobre una lista """

#Bienvenida
print("\nBienvenid@ al sistema de registros de la biblioteca municipal.")

#Introducción libros
print("\nA continuación va a introducir tres libros con su título y autor: \n")

libro_uno = []
libro_dos = []
libro_tres = []

libro_uno.append(str(input("Introduzca el título del primer libro: ")))
libro_uno.append(str(input("Introduzca el autor del primer libro: ")))
libro_dos.append(str(input("Introduzca el título del segundo libro: ")))
libro_dos.append(str(input("Introduzca el autor del segundo libro: ")))
libro_tres.append(str(input("Introduzca el título del tercer libro: ")))
libro_tres.append(str(input("Introduzca el autor del tercer libro: ")))

#Lista de libros de la biblioteca
lista_biblioteca = [libro_uno, libro_dos, libro_tres]

#Lista de títulos de los libros en mayúscula
lista_titulo = [libro_uno[0].upper(), libro_dos[0].upper(), libro_tres[0].upper()]

#Lista de autores de los libros en minúscula
lista_autor = [libro_uno[1].lower(), libro_dos[1].lower(), libro_tres[1].lower()]

#Ordenar los títulos y autores
lista_titulo.sort()
lista_autor.sort()

#Ver lista de libros
print("\nEsta es la lista de libros de la biblioteca:")
for libro in lista_titulo:
	print(libro)

#Ver lista de autores
print("\nEsta es la lista de autores de la biblioteca:")
for autor in lista_autor:
	print(autor)

#Ver lista de libros y autores
print("\nEsta es la lista de libros con autores de la biblioteca:")
for obra in lista_biblioteca:
	print("libro:",obra[0],",autor:", obra[1])

#Número de libros hoy en la biblioteca
print("Hay",len(lista_biblioteca),"libros en la biblioteca.")

#Comparación con los de ayer
lista_biblioteca_ayer = [] #Se supone que hoy la inauguramos.
print("¿Es cierto que hay más libros hoy en la biblioteca que ayer?",len(lista_biblioteca) >= len(lista_biblioteca_ayer))

#Búsqueda de libros por autor
busca_autor = str(input("\nBusca el numero de libros del autor: "))
busca_autor= busca_autor.lower()
print("\nDel autor", busca_autor,"hay esta cantidad de libros:", lista_autor.count(busca_autor))
