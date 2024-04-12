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
    
class Libro:
    def __init__(self, titulo:str, autor:str, genero:str, usuario:str):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.usuario = ""
     
    def prestar(self, usuario):
        indice = []
        if self.titulo in indice:
            print(f"He prestado el libro {self.titulo} a {self.usuario}")
        self.usuario = usuario

    def devolver(self):
        self.usuario = None
        
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []
        self.libros_prestados = []
    
    def agregar_libro(self, libro):
        agregar_libro = input("¿Desea agregar un libro? (s/n): ")
        if agregar_libro == "s":
            self.libros_disponibles.append(libro)
    
    def mostrar_libros_disponibles(self):
        for libro in self.libros_disponibles:
            print(libro.titulo, libro.autor)
    
    def prestar_libro(self, indice, usuario):
        for libro in self.libros_disponibles:
            libro.prestar(usuario)
            self.libros_prestados.append(libro)
            self.libros_disponibles.remove(libro)
        
    def devolver_libro(self, indice):
        for libro in self.libros_disponibles:
            libro = self.libros_prestados[indice]
            libro.devolver()
            self.libros_disponibles.append(libro)
            self.libros_prestados.remove(libro)
        
class Usuario:
    def __init__(self, usuario):
        self.usuario = usuario
        
usuario_uno = Usuario("Juan")

usuario_dos = Usuario("Juan")

libro_uno = Libro("El Quijote", "Cervantes", "Fantástico", usuario_uno)
libro_dos = Libro("Yerma", "Lorca", "Drama", usuario_dos)
biblioteca = Biblioteca()

biblioteca.agregar_libro(libro_uno)
biblioteca.agregar_libro(libro_dos)
biblioteca.mostrar_libros_disponibles()

libro_uno.prestar(usuario_uno)

#biblioteca.prestar_libro(libro_dos, usuario_uno)
biblioteca.mostrar_libros_disponibles()