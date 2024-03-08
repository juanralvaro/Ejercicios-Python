""" Crear un programa en Python que simule la gestión de las tareas pendientes. 

1. Utiliza una lista para almacenar las tareas y realiza las siguientes operaciones:
    1. Agregar tres tareas al final de la lista.
    2. Mostrar todas las tareas actuales
    3. Verificar si una tarea específica, tarea_buscar, está presente en vuestra lista
    4. Eliminar la segunda tarea de la lista
    5. Mostrar el número de tareas después de eliminar la del punto d. """

#Bienvenida
print("Bienvenido al programa de gestión de tareas.")

#Nueva lista
lista_tareas = []

#Agregar tres tareas al final de la lista
nueva_tarea1 = str(input("\nIntroduzca la tarea en formato 'tarea_xxx': "))
nueva_tarea2 = str(input("Introduzca la tarea en formato 'tarea_xxx': "))
nueva_tarea3 = str(input("Introduzca la tarea en formato 'tarea_xxx': "))

lista_tareas.extend([nueva_tarea1,nueva_tarea2,nueva_tarea3])

#Mostrar las tareas actuales
print(lista_tareas)

#Verificar si una tarea específica, tarea_buscar, está presente en vuestra lista
print("\nLa tarea 'tarea_buscar' está presente", lista_tareas.count("tarea_buscar"),"veces.")

#Eliminar la segunda tarea de la lista
lista_tareas.remove("tarea_limpiar")

#Mostrar el número de tareas después de eliminar la del punto d
print("\nQuedan estas tareas:",lista_tareas)