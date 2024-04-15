""" 
EJERCICIO RÁPIDO 1: Implementa un bucle while que permita al usuario crear instancias de la clase libro, aportando el nombre de la instancia y los valores correspondientes a cada uno de los atributos que forman la propia instancia, hasta que el usuario decida salir del programa para agregar libros a la biblioteca. Antes de salir del programa tenemos que mostrar al usuario la cantidad de libros en biblioteca actualizada.
· Creamos una estructura de control del bucle While que se corresponda con un bucle infinito.
· Solicitamos al usuario la entrada de los datos de la nueva instancia que queremos crear: 
    · Título
    · Autor
    · Páginas
· Creamos un nuevo objeto de la clase libro con los valores de sus atributos introducidos por el usuario.
· Le pregguntamos al usuario si quiere crear un nuevo objeto o si quiere salir del programa.
· Antes de salir del programa y despedirnos, imprimimos por pantalla la cantidad actualizada de los libros de mi biblioteca.
"""

class Libro:
    cantidad_libros_en_biblioteca = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.cantidad_libros_en_biblioteca += 1
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de paginas: {self.paginas}\n")

libro_uno = Libro("Yerma","García Lorca",200)
libro_dos = Libro("Cien años de soledad","García Márquez",300)

biblioteca = [libro_uno,libro_dos]
while True:
#    for i, nuevo_libro in enumerate(Libro.cantidad_libros_en_biblioteca, start=1):
    nuevo_libro = Libro(str(input("Introduce el nombre del libro u 'No' para terminar: \n")), str(input("Introduce el autor del libro o 'No' para terminar: \n")), int(input("Mostrar el número de páginas del libro o '0' para terminar: \n")))
    if nuevo_libro.titulo == "No" or nuevo_libro.autor == "No" or nuevo_libro.paginas == 0:
        break

print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca-1}")
for libro in biblioteca:
    print(libro)
    
""" #SOLUCIÓN CARLOS:
# Lista para almacenar los libros
biblioteca = []
while True:
    print("\n--- Agregar un nuevo libro a la biblioteca ---")
    titulo = str(input("Ingrese el título del libro (o escriba 'salir' para finalizar): "))
    
    if titulo.lower() == "salir":
        break  # Salir del bucle si el usuario ingresa "salir"
    
    autor = str(input("Ingrese el autor del libro: "))
    paginas = int(input("Ingrese el número de paginas del libro: "))
    
    # Crear una instancia de la clase Libro
    nuevo_libro = Libro(titulo, autor, paginas)
    
    # Agregar el libro a la biblioteca
    biblioteca.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado a la biblioteca.")

#Mostar la cantidad actual de libros en mi biblioteca  
print(f"La cantidad de libros en la biblioteca es: {Libro.cantidad_libros_en_biblioteca}")
print("Muchas gracias por usar el programa de gestión de biblioteca, hasta la próxima") """