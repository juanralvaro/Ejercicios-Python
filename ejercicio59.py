""" - 59- Reto de programación III
    
    **Objetivo:**
    El objetivo de este ejercicio es que cada grupo de estudiantes plantee un programa de Python que incluya fallos de sintaxis, de concepto y de estilo. Los demás grupos deberán resolver los desafíos planteados por los otros grupos.
    
    **Premio:**
    
    Selección del orden de presentación de proyectos. 
    
    **Instrucciones:**
    
    1. **Creación de programas:**
        - Cada grupo debe crear un programa en Python que contenga al menos 10 fallos de sintaxis, de concepto o de estilo.
        - El programa debe utilizar la sintaxis y los conceptos vistos hasta el momento en el curso, incluyendo hasta la POO.
        - ENTREGA MARTES 16 ABRIL ANTES DE LAS 12
        - Programas a corregir
            - Grupo 1 - Nacho, Nader, Óscar, Justo, Fran Amado -
                
                ```python
                
                ```
                
            - Grupo 2 - Jordi, Juan, Estefanía, Manuel, Xavi -
                
                ```python
                
                ```
                
            - Grupo 3 - Geovanna, Sarai, Roberto, Cecilia -
                
                ```python
                
                
            - Grupo 4 - Fran, Ginés, David -
                
                ```python
                
                ```
                
            - Grupo 5 - Adrián, Alejandro, Daniel, Raquel, Jose Carlos -
                
                ```python
                
                ```
                
    2. **Resolución de desafíos:**
        - Los demás grupos deberán intentar resolver los desafíos planteados por los otros grupos.
        - Se recomienda trabajar en equipo para identificar y corregir los fallos en los programas de los otros grupos.
        - El grupo que logre corregir todos los fallos correctamente en el menor tiempo posible será el ganador.
        - REALIZACIÓN MARTES 16 EN CLASE:
            - Estaréis divididos en salas, cada sala un grupo
            - Daremos el pistoletazo de salida y os podéis organizar para resolver los retos como queráis
            - La profesora estará en la sala principal. Una vez que el grupo termine se lo comunicará a la profesora en el chat público de la sala principal.
            - La profesora revisará el documento enviado para comprobar si es totalmente correcto. Si el documento no es correcto, se avisará al grupo una vez que el resto de grupos haya entregado su documento con las correcciones en esa ronda.
            - Ganará el equipo que resuelva CORRECTAMENTE antes el reto
    3. **Reflexión:**
        - Al finalizar el ejercicio, se realizará una corrección sobre los errores cometidos, las soluciones encontradas y los conceptos aprendidos, la cual se reflejará como siempre en comentarios en la propia corrección del ejercicio.
    
    **Notas:**
    
    - Se puede utilizar cualquier tema o contexto para los programas, siempre y cuando se respeten los requisitos del ejercicio.
    - Se recomienda que los programas sean lo suficientemente desafiantes para que los otros grupos tengan que esforzarse en resolver los problemas planteados. """

class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.socio = None

    def alquilar(self, socio):
        if self.socio is None:
            self.socio = socio
            print(f"La película '{self.titulo}' ha sido alquilada a {socio.nombre}.")
            return True
        else:
            print(f"La película '{self.titulo}' ya está alquilada a {self.socio.nombre}.")
            return False

    def devolver(self):
        if self.socio is not None:
            print(f"La película '{self.titulo}' ha sido devuelta.")
            self.socio = None
        else:
            print(f"La película '{self.titulo}' no está alquilada.")

class Videoclub:
    def __init__(self):
        self.peliculas_disponibles = []
        self.peliculas_alquiladas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas_disponibles.append(pelicula)
        print(f"La película '{pelicula.titulo}' ha sido añadida al videoclub.")

    def mostrar_peliculas_disponibles(self):
        print("Películas disponibles en el videoclub:")
        for i, pelicula in enumerate(self.peliculas_disponibles, start=1):
            print(f"{i}. Título: {pelicula.titulo}, Director: {pelicula.director}, Género: {pelicula.genero}")

    def alquilar_pelicula(self, indice, socio):
        if 0 < indice <= len(self.peliculas_disponibles):
            pelicula = self.peliculas_disponibles[indice - 1]
            if pelicula.alquilar(socio):
                self.peliculas_disponibles.pop(indice - 1)
                self.peliculas_alquiladas.append(pelicula)
        else:
            print("Índice de película no válido.")

    def devolver_pelicula(self, indice):
        if 0 < indice <= len(self.peliculas_alquiladas):
            pelicula = self.peliculas_alquiladas.pop(indice - 1)
            pelicula.devolver()
            self.peliculas_disponibles.append(pelicula)
        else:
            print("Índice de película no válido.")

class Socio:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear una instancia del videoclub
videoclub = Videoclub()

# Menú de opciones
print("Bienvenido al videoclub.")
print("Seleccione una opción:")
print("1. Agregar una pelicula")
print("2. Mostrar peliculas disponibles")
print("3. Alquilar una pelicula")
print("4. Devolver una pelicula")
print("5. Mostrar peliculas alquiladas")
print("6. Salir")

while True:
    opcion = input("Ingrese el número de la opción seleccionada: ")

    if opcion == '1':
        titulo = input("Ingrese el título de la película: ")
        director = input("Ingrese el director de la película: ")
        genero = input("Ingrese el género de la película: ")
        nueva_pelicula = pelicula(titulo, director, genero)
        videoclub.agregar_pelicula(nueva_pelicula)
    elif opcion == '2':
        videoclub.mostrar_peliculas_disponibles()
    elif opcion == '3':
        videoclub.mostrar_peliculas_disponibles()
        indice = int(input("Ingrese el número de películas que desea alquilar: "))
        nombre_socio = input("Ingrese su nombre: ")
        socio = Socio(nombre_socio)
        videoclub.alquilar_pelicula(indice, socio)
    elif opcion == '4':
        videoclub.mostrar_peliculas_disponibles()
        indice = int(input("Ingrese el número de la pelicula que desea devolver: "))
        videoclub.devolver_pelicula(indice)
    elif opcion == '5':
        print("Películas prestadas:")
        for i, pelicula in enumerate(videoclub.peliculas_alquiladas, start=1):
            print(f"{i}. Título: {pelicula.titulo}, Director: {pelicula.director}, Género: {pelicula.genero}, Alquilada a: {pelicula.socio.nombre}")
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")