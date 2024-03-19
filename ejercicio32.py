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

#Bienvenida
print("Bienvenido a la agenda telefónica de su móvil.")

#1. Creación de la agenda
agenda_telefonica = {
    "Juan": 923912918,
    "María": 951292913,
    "Andrés": 698923972,
    "Patricia": 698237233,
    "Mario": 912872029
}
print("Agenda telefónica original:",agenda_telefonica)

#2. Borrado de datos
agenda_telefonica.clear()
print("Agenda telefónica borrada:",agenda_telefonica)

#3. Añadido de datos
nuevos_contactos = {"Paula": 881902312, "Sergio": 981232912, "Antonio":664013487}
agenda_telefonica.update(nuevos_contactos)
print("Agenda actualizada:",agenda_telefonica)

#4. Copia de datos
agenda_copia = agenda_telefonica.copy()
print("Agenda original copiada:",agenda_copia,".\nAgenda actual:",agenda_telefonica)
print("¿ID's iguales?",id(agenda_copia), id(agenda_telefonica))

#5. Get
valor1 = agenda_telefonica.get("Juan")
valor2 = agenda_telefonica.get("Sandra", 823782372)
print("Teléfonos obtenidos:",valor1, valor2)

#6. Hacer pop
valor_eliminado_pop = agenda_telefonica.pop("Sergio")
print("Valor eliminado:",valor_eliminado_pop,". Agenda actualizada:",agenda_telefonica)

#7. Hacer popitem
valor_eliminado_popitem = agenda_telefonica.popitem()
print("Valor eliminado",valor_eliminado_popitem,". Agenda actualizada",agenda_telefonica)

#8. Lista de llaves
llaves = agenda_telefonica.keys()
print("Llaves de la agenda",llaves)

#9. Lista de valores
valores = agenda_telefonica.values()
print("Valores de la agenda",valores)

#10. Items de la agenda
items = agenda_telefonica.items()
print("Items de la agenda", items)

#11. Uso de setdefault
valor_set_default = agenda_telefonica.setdefault('Alejandra', 624871454)
print("Teléfono de la profesora",valor_set_default,". Agenda actualizada",agenda_telefonica)

#Despedida
print("Gracias por usar la agenda. Hasta la próxima.")