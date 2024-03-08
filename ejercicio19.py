""" Crear un programa en Python que simule la gestión de las tareas pendientes. 

1. Utiliza una lista para almacenar las tareas y realiza las siguientes operaciones:
    1. Agregar tres tareas al final de la lista.
    2. Mostrar todas las tareas actuales
    3. Verificar si una tarea específica, tarea_buscar, está presente en vuestra lista
    4. Eliminar la segunda tarea de la lista
    5. Mostrar el número de tareas después de eliminar la del punto d. """

# Programa gestión de tareas (listas)

# Inicializar la lista de tareas
tareas = []

# 1. Agregar tres tareas al final de la lista de forma simultánea
print("Agregar tres tareas:")
tareas.append(str(input("Tarea 1: ")))
tareas.append(str(input("Tarea 2: ")))
tareas.append(str(input("Tarea 3: ")))

# 2. Mostrar todas las tareas actuales
print("\nTareas actuales:")
print("-", tareas[0])
print("-", tareas[1])
print("-", tareas[2])

# 3. Verificar si una tarea específica está presente en la lista
tarea_buscar = input("\nIngrese una tarea a buscar: ")
""" Otra forma de resolverlo: 
tarea_en_lista = tarea_buscar in tareas
print("La tarea que acabas de añadir esta en la lista:", tarea_en_lista)
"""
contador_tarea = tareas.count(tarea_buscar)
print(f"\nLa tarea '{tarea_buscar}' está presente {contador_tarea} veces en la lista.")

# 4. Eliminar la segunda tarea de la lista
tareas.remove(tareas[1])

# 5. Mostrar el número de tareas después de eliminar la del punto 4
print("\nNúmero de tareas después de eliminar una tarea:", len(tareas))