""" 1. Define un diccionario vacio llamado **`peliculas`** Y solicita al usuario que agrege al menos cinco películas. Cada película debe tener un título como clave y su año de lanzamiento como valor. 
2. Utiliza un bucle **`for`** junto con el método **`keys()`** para iterar sobre el diccionario e imprimir solo los títulos de las películas.
3. Utiliza un bucle **`for`** junto con el método **`items()`** para iterar sobre el diccionario e imprimir tanto los títulos de las películas como sus años de lanzamiento.
4. Utiliza un bucle **`for`** junto con el método **`values()`** para iterar sobre el diccionario e imprimir solo los años de lanzamiento de las películas. Dentro del bucle, realiza las siguientes operaciones con los años de lanzamiento:
    - Comprueba si el año es mayor que 2000 utilizando un operador de comparación.
    - Comprueba si el año es divisible por 5 utilizando un operador de módulo (%).
    - Comprueba si el año es igual a 1995 utilizando un operador de comparación.
    - Asigna el año a una nueva variable y muéstralo junto con un mensaje personalizado.
5. Después de completar las iteraciones, muestra un mensaje de conclusión. """

#Bienvenida
print("Bienvenido al gestor de películas.")

#1. Introducción de películas
peliculas = {
    str(input("Agregue el título de una película: ")):int(input("Agregue el año de la película: ")),
    str(input("Agregue el título de una película: ")):int(input("Agregue el año de la película: ")),
    str(input("Agregue el título de una película: ")):int(input("Agregue el año de la película: ")),
    str(input("Agregue el título de una película: ")):int(input("Agregue el año de la película: ")),
    str(input("Agregue el título de una película: ")):int(input("Agregue el año de la película: "))
}
print(peliculas)

#2. Obtener los títulos de las películas
for titulo in peliculas.keys():
    print(titulo)

#3. Obtener películas y año de lanzamiento
for titulo in peliculas.items():
    print(titulo)

#4. Obtener año de lanzamiento y hacer operaciones
for anio in peliculas.values():
    print(anio)
    cine_moderno = anio > 2000
    print("¿Es o no cine moderno?",cine_moderno)
    divisible_por_5 = anio % 5 == 0
    print("¿Es el año del estreno divisible por 5?",divisible_por_5)
    es_1995 = anio == 1995
    print("¿Es el año del estreno 1995?",es_1995)
    anio_nuevo = anio
    print(f"El año {anio_nuevo} fue asignado a la variable 'anio_nuevo'.")

#5. Conclusión
print("Gracias por venir al gestor de películas.")