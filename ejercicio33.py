""" Crea un programa que gestione una lista de tareas pendientes, un conjunto de elementos de una lista de compras y un diccionario de contactos. 

1. **Creación de las Colecciones de Datos:**
    - Inicia el programa creando las siguientes colecciones de datos:
        - Una lista llamada **`tareas_pendientes`** que contenga al menos 5 tareas pendientes.
        - Un conjunto llamado **`lista_compras`** que incluya los elementos de una lista de compras con al menos 5 ítems.
        - Un diccionario llamado **`agenda_contactos`** que contenga los nombres y números de teléfono de al menos 5 contactos.
2. **Operaciones con la Lista de Tareas Pendientes:**
    - Utiliza el método **`append()`** para agregar una nueva tarea a la lista de tareas pendientes.
    - Utiliza el método **`remove()`** para eliminar una tarea específica de la lista de tareas pendientes.
    - Utiliza el método **`clear()`** para vaciar la lista de tareas pendientes.
    - Utiliza el método **`sort()`** para ordenar las tareas pendientes alfabéticamente.
3. **Operaciones con el Conjunto de la Lista de Compras:**
    - Utiliza el método **`add()`** para agregar un nuevo ítem a la lista de compras.
    - Utiliza el método **`discard()`** para eliminar un ítem específico de la lista de compras.
    - Utiliza el método **`clear()`** para vaciar el conjunto de la lista de compras.
4. **Operaciones con el Diccionario de Contactos:**
    - Utiliza el método **`update()`** para agregar nuevos contactos al diccionario de contactos.
    - Utiliza el método **`pop()`** para eliminar un contacto específico del diccionario de contactos.
    - Utiliza el método **`clear()`** para vaciar el diccionario de contactos.
    - Utiliza el método **`sorted()`** para ordenar los contactos por nombre y mostrarlos en orden alfabético.
5. **Mostrar Resultados:**
    - Después de cada operación, muestra el estado actual de cada colección de datos.
6. **Finalizar el Programa:**
    - Proporciona una opción para que el usuario pueda salir del programa cuando lo desee. """

#Bienvenida
print("Bienvenido al gestor de lista de tareas, conjunto de lista de compras y diccionario de contactos.")

#1. Creación de lista, colección y diccionario
tareas_pendientes = ["cocinar", "poner la lavadora", "fregar", "planchar",  "hacer la compra"]
lista_de_compras = {"carne", "pescado", "lejía", "pan", "verduras"}
diccionario_de_contactos = {
    "José": 989232911,
    "María": 686113434,
    "Pedro": 926238712,
    "Ángeles": 682329212,
    "Antonio": 987232812
}

#2. Operaciones con la lista de tareas pendientes
tareas_pendientes.append("limpiar los cristales")
print("Cambio 1:",tareas_pendientes)
tareas_pendientes.remove("cocinar")
print("Cambio 2:",tareas_pendientes)
#tareas_pendientes.clear() -> lo dejo para el final para que el ejercicio con sort tenga sentido
print("Cambio 3:",tareas_pendientes)
tareas_pendientes.clear()
print("Cambio 4:",tareas_pendientes)

#3. Operaciones con el conjunto de la lista de compras
lista_de_compras.add("queso")
print("Cambio 1:",lista_de_compras)
lista_de_compras.discard("carne")
print("Cambio 2:",lista_de_compras)
lista_de_compras.clear()
print("Cambio 3:",lista_de_compras)

#4. Operaciones con el diccionario de contactos
diccionario_de_contactos.update(Paula=672391932)
print("Cambio 1:",diccionario_de_contactos)
diccionario_de_contactos.pop("José")
print("Cambio 2:",diccionario_de_contactos)
#diccionario_de_contactos.clear() -> lo dejo para el final para que el ejercicio con sorted tenga sentido
contactos_a_ordenar = diccionario_de_contactos.keys()
contactos_ordenados = sorted(contactos_a_ordenar)
print("Cambio 3:",contactos_ordenados)
diccionario_de_contactos.clear()
print("Cambio 4:",diccionario_de_contactos)

#6. Opción de salida
opcion_de_salida = bool(input("¿Quiere salir? Diga True si sí, False si no. "))

#Despedida
print("Gracias por usar el gestor. ¡Buen día!")