""" Biblioteca de videojuegos
    
    Vamos a crear un programa en Python que simule la gestión de una biblioteca de videojuegos. Para ello, vamos a utilizar conjuntos para representar diferentes categorías de videojuegos y realizar operaciones sobre ellos.
    
    1. Define los siguientes conjuntos para representar diferentes categorías de videojuegos:
        - **`aventura`**: Contiene videojuegos de aventura.
        - **`accion`**: Contiene videojuegos de acción.
        - **`estrategia`**: Contiene videojuegos de estrategia.
        - **`deportes`**: Contiene videojuegos de deportes.
    2. Utiliza la función **`input()`** para permitir al usuario agregar videojuegos a cada categoría. Pídele al usuario que ingrese los nombres de los videojuegos separados por comas.
    3. Convierte las cadenas ingresadas por el usuario en conjuntos utilizando el método **`split()`** y luego agregalos a los conjuntos correspondientes utilizando el método **`update()`**.
    4. Muestra al usuario un resumen de las categorías de videojuegos y la cantidad de videojuegos en cada una utilizando la función **`print()`** y la función **`len()`** .
    5. Utiliza operadores de conjuntos para realizar algunas operaciones como:
        - Mostrar los videojuegos que están presentes en la categoría de acción y aventura.
        - Mostrar los videojuegos que están presentes en la categoría de estrategia pero no en la de deportes.
        - Mostrar todos los videojuegos únicos presentes en todas las categorías.
    
    Instrucciones adicionales:
    
    - Asegúrate de manejar correctamente la entrada del usuario (separadores, uso de mayúsculas y minúsculas y realizar las conversiones necesarias de datos utilizando casting de datos.
    - Recuerda usar la función **`split()`** para dividir la entrada del usuario en elementos separados y el método **`update()`** para agregar elementos a los conjuntos. """

aventura = set()
accion = set()
estrategia = set()
deportes = set()

# Solicitar al usuario que ingrese videojuegos para cada categoría
print("Bienvenido a la gestión de la biblioteca de videojuegos.")
print("Ingresa los videojuegos para cada categoría separados por comas.")

# Pedir al usuario que ingrese los videojuegos para cada categoría
aventura_input = str(input("Videojuegos de aventura: ")).lower()
accion_input = str(input("Videojuegos de acción: ")).lower()
estrategia_input = str(input("Videojuegos de estrategia: ")).lower()
deportes_input = str(input("Videojuegos de deportes: ")).lower()

# Actualizar conjuntos con los videojuegos ingresados por el usuario
aventura.update(aventura_input.split(","))
accion.update(accion_input.split(","))
estrategia.update(estrategia_input.split(","))
deportes.update(deportes_input.split(","))

# Mostrar resumen de categorías y cantidad de videojuegos en cada una
print("\nResumen de categorías de videojuegos:")
print(f"Aventura ({len(aventura)}): {aventura}")
print(f"Acción ({len(accion)}): {accion}")
print(f"Estrategia ({len(estrategia)}): {estrategia}")
print(f"Deportes ({len(deportes)}): {deportes}")

# Operaciones con conjuntos
print("\nOperaciones con conjuntos:")
print("Videojuegos de acción y aventura:", accion.intersection(aventura))
print("Videojuegos de estrategia pero no de deportes:", estrategia.difference(deportes))
print("Todos los videojuegos únicos en todas las categorías:", aventura.union(accion, estrategia, deportes))