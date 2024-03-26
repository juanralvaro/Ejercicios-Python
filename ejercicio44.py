""" Vamos a crear un programa que registre los nombres de los invitados a una fiesta. El programa solicitará al usuario que introduzca el nombre de cada invitado y lo agregará a una lista. Cuando el usuario escriba "fin", el programa mostrará la lista de invitados y terminará.

Instrucciones:

1. Inicia el programa con un mensaje de bienvenida.
2. Crea una lista vacía llamada **`invitados`**.
3. Utiliza un bucle **`while`** para solicitar al usuario que introduzca el nombre de un invitado.
4. Dentro del bucle, agrega cada nombre introducido por el usuario a la lista **`invitados`**.
5. Si el usuario escribe "fin", sal del bucle.
6. Después de salir del bucle, muestra un mensaje de despedida y la lista de invitados. """

print("Bienvenido al registrador de invitados.")

invitados = []

while True:
    invitado = str(input("Introduzca el nombre de un invitado o 'fin' para cerrar la lista: "))
    invitados.append(invitado)
    if invitado == "Fin":
        break
invitados.remove("Fin")
print("Gracias por usar el registro. Los invitados son:",invitados)