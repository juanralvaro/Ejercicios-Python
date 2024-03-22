""" Crea un programa que gestione una lista de tareas pendientes, un conjunto de elementos de una lista de compras y un diccionario de contactos. 

1. **Creación de las Colecciones de Datos:**
    - Inicia el programa creando las siguientes colecciones de datos:
        - Una lista llamada **`tareas_pendientes`** que contenga al menos 5 tareas pendientes.
        - Un conjunto llamado **`lista_compras`** que incluya los elementos de una lista de compras con al menos 5 ítems.
        - Un diccionario llamado **`agenda_contactos`** que contenga los nombres y números de teléfono de al menos 5 contactos.
2. **Operaciones con la Lista de Tareas Pendientes:**
    - Utiliza el método **`append()`** para agregar una nueva tarea a la lista de tareas pendientes.
    - Utiliza el método **`remove()`** para eliminar una tarea específica de la lista de tareas pendientes.
    - Utiliza el método **`sort()`** para ordenar las tareas pendientes alfabéticamente.
    - Utiliza el método **`clear()`** para vaciar la lista de tareas pendientes.
3. **Operaciones con el Conjunto de la Lista de Compras:**
    - Utiliza el método **`add()`** para agregar un nuevo ítem a la lista de compras.
    - Utiliza el método **`discard()`** para eliminar un ítem específico de la lista de compras.
    - Utiliza el método **`clear()`** para vaciar el conjunto de la lista de compras.
4. **Operaciones con el Diccionario de Contactos:**
    - Utiliza el método **`update()`** para agregar nuevos contactos al diccionario de contactos.
    - Utiliza el método **`pop()`** para eliminar un contacto específico del diccionario de contactos.
    - Utiliza el método **`sorted()`** para ordenar los contactos por nombre y mostrarlos en orden alfabético.
    - Utiliza el método **`clear()`** para vaciar el diccionario de contactos.
5. **Mostrar Resultados:**
    - Después de cada operación, muestra el estado actual de cada colección de datos.
6. **Finalizar el Programa:**
    - Proporciona una opción para que el usuario pueda salir del programa cuando lo desee. """

# Creación de las colecciones de datos
tareas_pendientes = ['Hacer la compra', 'Estudiar para el examen', 'Llamar al médico', 'Enviar correo electrónico', 'Preparar la cena']
lista_compras = {'Manzanas', 'Leche', 'Pan', 'Huevos', 'Arroz'}
agenda_contactos = {'Juan': '123456789', 'María': '987654321', 'Carlos': '456789123', 'Ana': '321654987', 'Luisa': '654321987'}

# Operaciones con la lista de tareas pendientes
tareas_pendientes.append('Sacar al perro')
print("Tareas pendientes después de agregar una nueva tarea:", tareas_pendientes)
tareas_pendientes.remove('Llamar al médico')
print("Tareas pendientes después de eliminar una tarea:", tareas_pendientes)
tareas_pendientes.sort()
print("Tareas pendientes ordenadas alfabéticamente:", tareas_pendientes)
tareas_pendientes.clear()
print("Tareas pendientes después de vaciar la lista:", tareas_pendientes)

# Operaciones con el conjunto de la lista de compras
lista_compras.add('Cerveza')
print("Lista de compras después de agregar un ítem:", lista_compras)
lista_compras.discard('Leche')
print("Lista de compras después de eliminar un ítem:", lista_compras)
lista_compras.clear()
print("Lista de compras después de vaciar el conjunto:", lista_compras)

# Operaciones con el diccionario de contactos
nuevos_contactos = {'Pedro': '654987321', 'Elena': '789456123'}
agenda_contactos.update(nuevos_contactos)
print("Agenda de contactos después de agregar nuevos contactos:", agenda_contactos)

# Ordenar los contactos por nombre y mostrarlos en orden alfabético
contactos_ordenados = sorted(agenda_contactos.items())
print("Contactos ordenados alfabéticamente:", contactos_ordenados)

# Eliminar un contacto específico del diccionario de contactos
agenda_contactos.pop('María')
print("Agenda de contactos después de eliminar un contacto:", agenda_contactos)

# Vaciar el diccionario de contactos
agenda_contactos.clear()
print("Agenda de contactos después de vaciar el diccionario:", agenda_contactos)