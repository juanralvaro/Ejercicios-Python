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

#Previo. Bienvenida
print("Bienvenido a la Biblioteca de videojuegos Akira Toriyama.")

#1. Creación de conjuntos de videojuegos: los defino como set porque sólo con las llaves me salen diccionarios
conjunto_aventura = set()
conjunto_accion = set()
conjunto_estrategia = set()
conjunto_deportes = set()

#2. Añadir videojuegos a conjuntos: pongo inputs y los asigno a otras variables
mas_juegos_aventura = (str(input("Introduzca sus videojuegos de aventura separados por comas sin espacios: ")))
mas_juegos_accion = (str(input("Introduzca sus videojuegos de acción separados por comas sin espacios: ")))
mas_juegos_estrategia = (str(input("Introduzca sus videojuegos de estrategia separados por comas sin espacios: ")))
mas_juegos_deportes = (str(input("Introduzca sus videojuegos de deportes separados por comas sin espacios: ")))

#3.1 Convertir cadenas en conjuntos: pongo en mayúsculas los videojuegos y los asigno a unas terceras variables, luego a éstas les aplico un split con comas y las añado a los conjuntos
juegos_aventura = mas_juegos_aventura.upper()
juegos_accion = mas_juegos_accion.upper()
juegos_estrategia = mas_juegos_estrategia.upper()
juegos_deportes = mas_juegos_deportes.upper()
#3.2 Añadir con update: añado los separadores a los conjuntos originales
conjunto_aventura.update(juegos_aventura.split(","))
conjunto_accion.update(juegos_accion.split(","))
conjunto_estrategia.update(juegos_estrategia.split(","))
conjunto_deportes.update(juegos_deportes.split(","))

#4. Resumen categorías videojuegos
print(f"\nLa categoría de videojuegos de aventura contiene los videojuegos {conjunto_aventura}, que contiene {len(conjunto_aventura)} videojuegos.")
print(f"\nLa categoría de videojuegos de acción contiene los videojuegos {conjunto_accion}, que contiene {len(conjunto_accion)} videojuegos.")
print(f"\nLa categoría de videojuegos de estrategia contiene los videojuegos {conjunto_estrategia}, que contiene {len(conjunto_estrategia)} videojuegos.")
print(f"\nLa categoría de videojuegos de deportes contiene los videojuegos {conjunto_deportes}, que contiene {len(conjunto_deportes)} videojuegos.")

#5. Usando operadores: uso intersection para los juegos en aventura o acción, difference para los juegos en estrategia que no estén en deportes, y unions encadenadas para todos los juegos únicos (aclaro que en mis listas no repite ninguno en ninguna categoría)
juegos_en_aventura_o_accion = conjunto_aventura.intersection(conjunto_accion)
print("\nVideojuegos de aventura o acción:",juegos_en_aventura_o_accion)

juegos_en_estrategia_pero_no_en_deportes = conjunto_estrategia.difference(conjunto_deportes)
print("\nVideojuegos de estrategia que no están en deportes:",juegos_en_estrategia_pero_no_en_deportes)

todos_los_videojuegos_unicos = conjunto_aventura.union(conjunto_accion.union(conjunto_estrategia.union(conjunto_deportes)))
print("\nTodos los videojuegos únicos en todas las categorías:",todos_los_videojuegos_unicos)

#Post. Adiós
print("\n¡Gracias por venir!")