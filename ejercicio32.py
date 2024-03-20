""" 1. Crea un diccionario llamado **`agenda_telefonica`** que contenga al menos cinco contactos, donde cada contacto tenga un nombre como clave y un número de teléfono como valor.
2. Utiliza el método **`clear()`** para eliminar todos los elementos del diccionario y verifica que ahora está vacío.
3. Utiliza el método **`update()`** para agregar nuevos contactos a la agenda. Puedes agregar múltiples contactos al mismo tiempo proporcionando un diccionario adicional con los nuevos contactos.
4. Utiliza el método **`copy()`** para crear una copia del diccionario original y verifica que la copia es independiente del original.
5. Utiliza el método **`get()`** para obtener el número de teléfono de un contacto existente y de un contacto inexistente. Asegúrate de proporcionar un valor predeterminado para el caso en que el contacto no exista.
6. Utiliza el método **`pop()`** para eliminar un contacto de la agenda y devolver su número de teléfono. Verifica que el contacto ya no está en la agenda y que el método devuelve el valor correcto.
7. Utiliza el método **`popitem()`** para eliminar el último contacto añadido a la agenda y verifica que el método devuelve una tupla con el contacto eliminado.
8. Utiliza el método **`keys()`** para obtener una lista de todas las claves en la agenda.
9. Utiliza el método **`values()`** para obtener una lista de todos los valores en la agenda.
10. Utiliza el método **`items()`** para obtener una lista de tuplas, donde cada tupla contiene una clave y su valor correspondiente en la agenda.
11. Utiliza el método **`setdefault()`**  para comprobar si tenemos apuntado el teléfono de tu profesora, y si no está apuntado, que lo incluya en tu diccionario. """

# Paso 1: Crear el diccionario inicial
agenda_telefonica = {
    "Juan": "123456789",
    "María": "987654321",
    "Pedro": "456789123",
    "Ana": "321654987",
    "Luis": "654321789"
}

# Paso 2: Limpiar el diccionario
agenda_telefonica.clear()
print("Diccionario después de limpiar:", agenda_telefonica)

# Paso 3: Agregar nuevos contactos
nuevos_contactos = {
    "Carlos": "111222333",
    "Sofía": "444555666"
}
agenda_telefonica.update(nuevos_contactos)
agenda_telefonica.update(Luis="666666666")
print("Diccionario después de agregar nuevos contactos:", agenda_telefonica)

# Paso 4: Crear una copia del diccionario original
copia_agenda = agenda_telefonica.copy()
print("Copia del diccionario original:", copia_agenda)

# Paso 5: Obtener números de teléfono con el método get()
print("Número de teléfono de Juan:", agenda_telefonica.get("Juan"))
print("Número de teléfono de Luis:", agenda_telefonica.get("Luis"))
print("Número de teléfono de Ana (no existe):", agenda_telefonica.get("Ana", "No encontrado"))

# Paso 6: Eliminar un contacto con el método pop()
telefono_pedro = agenda_telefonica.pop("Pedro")
print("Teléfono de Pedro eliminado:", telefono_pedro)
print("Diccionario después de eliminar a Pedro:", agenda_telefonica)

# Paso 7: Eliminar el último contacto con el método popitem()
ultimo_contacto_eliminado = agenda_telefonica.popitem()
print("Último contacto eliminado:", ultimo_contacto_eliminado)
print("Diccionario después de eliminar el último contacto:", agenda_telefonica)

# Paso 8: Obtener una lista de claves con el método keys()
print("Claves en la agenda:", agenda_telefonica.keys())

# Paso 9: Obtener una lista de valores con el método values()
print("Valores en la agenda:", agenda_telefonica.values())

# Paso 10: Obtener una lista de tuplas clave-valor con el método items()
print("Elementos en la agenda:", agenda_telefonica.items())

# Paso 11: Comprobar si tenemos el teléfono de la profesora en la agenda
telefono_profesora = agenda_telefonica.setdefault('Alejandra')
print("Teléfono profesora:", agenda_telefonica.items())