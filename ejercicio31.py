""" 1. Crea un diccionario llamado **`agenda_telefonica`** que contenga los nombres de algunas personas como claves y sus números de teléfono como valores.
2. Imprime el diccionario completo para verificar su contenido.
3. Accede al número de teléfono de una persona específica en la agenda telefónica e imprímelo.
4. Añade una nueva entrada a la agenda telefónica para una persona adicional junto con su número de teléfono.
5. Modifica el número de teléfono de una persona existente en la agenda telefónica.
6. Elimina una entrada de la agenda telefónica para una persona que ya no necesita ser contactada.
7. Imprime el diccionario actualizado para verificar los cambios realizados. """

#Bienvenida
print("Bienvenidos a nuestra agenda telefónica.")

#1. Inicialización del diccionario
agenda_telefonica = {
    "Juan": "982211211",
    "Javier": "812128812",
    "María": "928232812",
    "José": "898127621"
}

#2. Imprimir el diccionario
print("Agenda telefónica: \n",agenda_telefonica)

#3. Acceder al número de teléfono de Juan y lo imprime
telefono_juan = agenda_telefonica.get("Juan")

#4. Introducir un nuevo nombre y número
agenda_telefonica["Raquel"] = "981129222"

#5. Cambiar un número de teléfono
agenda_telefonica["José"] = "972391222"

#6. Eliminar una entrada
del agenda_telefonica["Javier"]

#7. Mostrar el diccionario
print("Agenda telefónica modificada:\n",agenda_telefonica)

#Despedida
print("Gracias por usar la agenda telefónica. ¡Hasta la vista!")