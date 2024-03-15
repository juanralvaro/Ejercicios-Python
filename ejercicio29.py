""" Vamos a crear un programa que gestione listas de reproducción de música utilizando conjuntos y las funciones/métodos que hemos aprendido.

1. Define dos listas de reproducción iniciales, **`playlist_a`** y **`playlist_b`**, cada una con al menos cinco canciones representadas por nombres de canciones (strings).
2. Crea conjuntos a partir de estas listas de reproducción.
3. Implementa la funcionalidad para agregar una nueva canción a una lista de reproducción.
4. Implementa la funcionalidad para eliminar una canción de una lista de reproducción.
5. Utiliza el método de conjunto **`union`** para crear una nueva lista de reproducción que contenga todas las canciones de **`playlist_a`** y **`playlist_b`**.
6. Utiliza el método de conjunto **`intersection`** para crear una nueva lista de reproducción que contenga solo las canciones que están en ambas **`playlist_a`** y **`playlist_b`**.
7. Utiliza el método de conjunto **`difference`** para crear una nueva lista de reproducción que contenga las canciones que están en **`playlist_a`** pero no en **`playlist_b`**.
8. Imprime las listas de reproducción resultantes y verifica que las funcionalidades y métodos están trabajando correctamente. """


#Bienvenida
print("Bienvenido al programa de listas de reproducción musical.")

#1. Lista de canciones disponibles en el sistema
playlist_a = ["Madrid City", "Columbia", "Flowers", "Quédate", "Despechá"]
playlist_b = ["Columbia", "Quédate", "Supernova", "La última", "Playa del inglés"]
print("Playlist A:",playlist_a,"\nPlaylist B: ",playlist_b)
print("-_-_-")

#2. Crear conjuntos
playlist_a_conjunto = set(playlist_a)
playlist_b_conjunto = set(playlist_b)

print("-_-_-")

#3. Añadir canción a la lista
playlist_a.extend(["Nochentera"])
print("Playlist tras añadido:",playlist_a)

print("-_-_-")

#4. Eliminar canción de la lista
playlist_a.remove("Flowers")
print("Playlist tras borrado:",playlist_a)

print("-_-_-")

#5. Unión de listas
playlist_total_conjunto = playlist_a_conjunto.union(playlist_b_conjunto)
playlist_total = list(playlist_total_conjunto)

#6. Intersección de listas
playlist_comun_conjunto = list(playlist_a_conjunto & playlist_b_conjunto)
playlist_comun = list(playlist_comun_conjunto)

#7. Diferencia entre listas
playlist_diferente_conjunto = playlist_a_conjunto.difference(playlist_b_conjunto)
playlist_diferente = list(playlist_diferente_conjunto)

#8. Imprimir las playlists resultantes
print("Playlist de canciones totales:", playlist_total)
print("-_-_-")

print("Playlist de canciones comunes:", playlist_comun)
print("-_-_-")

print("Playlist de canciones que sólo están en la lista A:", playlist_diferente)
#Despedida
print("-_-_-")
print("Gracias por escuchar música. ¡Hasta luego!")