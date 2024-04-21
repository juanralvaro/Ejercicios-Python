""" Desarrolla un programa en Python que permita administrar el préstamo y devolución de libros en una biblioteca.

1. Crea una clase llamada **`Libro`** con los siguientes atributos:
    - **`titulo`**: El título del libro.
    - **`autor`**: El autor del libro.
    - **`genero`**: El género del libro.
    - **`usuario`**: El usuario al que se ha prestado el libro.
2. La clase **`Libro`** debe tener los siguientes métodos:
    - **`prestar(self, usuario)`**: Método que permite prestar el libro a un usuario. Actualiza el atributo **`usuario`** con el usuario al que se ha prestado el libro.
    - **`devolver(self)`**: Método que permite devolver el libro. Actualiza el atributo **`usuario`** a **`None`**.
3. Crea una clase llamada **`Biblioteca`** con los siguientes atributos:
    - **`libros_disponibles`**: Una lista que almacena los libros disponibles en la biblioteca.
    - **`libros_prestados`**: Una lista que almacena los libros prestados.
4. La clase **`Biblioteca`** debe tener los siguientes métodos:
    - **`agregar_libro(self, libro)`**: Método que permite agregar un libro a la biblioteca.
    - **`mostrar_libros_disponibles(self)`**: Método que muestra los libros disponibles en la biblioteca.
    - **`prestar_libro(self, indice, usuario)`**: Método que permite prestar un libro de la biblioteca a un usuario.
    - **`devolver_libro(self, indice)`**: Método que permite devolver un libro prestado a la biblioteca.
5. Crea una clase llamada **`Usuario`** con un atributo **`nombre`** que represente a los usuarios de la biblioteca.
6. Desarrolla un programa principal que permita al usuario:
    - Agregar libros a la biblioteca.
    - Mostrar los libros disponibles en la biblioteca.
    - Prestar un libro a un usuario.
    - Devolver un libro a la biblioteca.
    - Mostrar los libros prestados y a quién han sido prestados. """
    
#SOLUCIÓN

class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.usuario = None

    def prestar(self, usuario):
        if self.usuario is None:
            self.usuario = usuario
            print(f"El libro '{self.titulo}' ha sido prestado a {usuario.nombre}.")
            return True
        else:
            print(f"El libro '{self.titulo}' ya está prestado a {self.usuario.nombre}.")
            return False

    def devolver(self):
        if self.usuario is not None:
            print(f"El libro '{self.titulo}' ha sido devuelto.")
            self.usuario = None
        else:
            print(f"El libro '{self.titulo}' no está prestado.")

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"El libro '{libro.titulo}' ha sido añadido a la biblioteca.")

    def mostrar_libros_disponibles(self):
        print("Libros disponibles en la biblioteca:")
        for i, libro in enumerate(self.libros_disponibles, start=1):
            print(f"{i}. Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}")

    def prestar_libro(self, indice, usuario):
        if 0 < indice <= len(self.libros_disponibles):
            libro = self.libros_disponibles[indice - 1]
            if libro.prestar(usuario):
                self.libros_disponibles.pop(indice - 1)
                self.libros_prestados.append(libro)
        else:
            print("Índice de libro no válido.")

    def devolver_libro(self, indice):
        if 0 < indice <= len(self.libros_prestados):
            libro = self.libros_prestados.pop(indice - 1)
            libro.devolver()
            self.libros_disponibles.append(libro)
        else:
            print("Índice de libro no válido.")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Menú de opciones
print("Bienvenido a la biblioteca.")
print("Seleccione una opción:")
print("1. Agregar un libro")
print("2. Mostrar libros disponibles")
print("3. Prestar un libro")
print("4. Devolver un libro")
print("5. Mostrar libros prestados")
print("6. Salir")

while True:
    opcion = input("Ingrese el número de la opción seleccionada: ")

    if opcion == '1':
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        nuevo_libro = Libro(titulo, autor, genero)
        biblioteca.agregar_libro(nuevo_libro)
    elif opcion == '2':
        biblioteca.mostrar_libros_disponibles()
    elif opcion == '3':
        biblioteca.mostrar_libros_disponibles()
        indice = int(input("Ingrese el número del libro que desea prestar: "))
        nombre_usuario = input("Ingrese su nombre: ")
        usuario = Usuario(nombre_usuario)
        biblioteca.prestar_libro(indice, usuario)
    elif opcion == '4':
        biblioteca.mostrar_libros_disponibles()
        indice = int(input("Ingrese el número del libro que desea devolver: "))
        biblioteca.devolver_libro(indice)
    elif opcion == '5':
        print("Libros prestados:")
        for i, libro in enumerate(biblioteca.libros_prestados, start=1):
            print(f"{i}. Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}, Prestado a: {libro.usuario.nombre}")
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")