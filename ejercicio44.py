""" Vamos a crear un programa que registre los nombres de los invitados a una fiesta. El programa solicitará al usuario que introduzca el nombre de cada invitado y lo agregará a una lista. Cuando el usuario escriba "fin", el programa mostrará la lista de invitados y terminará.

Instrucciones:

1. Inicia el programa con un mensaje de bienvenida.
2. Crea una lista vacía llamada **`invitados`**.
3. Utiliza un bucle **`while`** para solicitar al usuario que introduzca el nombre de un invitado.
4. Dentro del bucle, agrega cada nombre introducido por el usuario a la lista **`invitados`**.
5. Si el usuario escribe "fin", sal del bucle.
6. Después de salir del bucle, muestra un mensaje de despedida y la lista de invitados. """

# Mensaje de bienvenida
print("Bienvenido al registro de invitados a la fiesta.")

# Lista para almacenar los nombres de los invitados
invitados = []

# Bucle para solicitar los nombres de los invitados
while True:
    nombre = input("Ingrese el nombre del invitado (o escriba 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break  # Salir del bucle si el usuario escribe 'fin'
    else:
        invitados.append(nombre)  # Agregar el nombre del invitado a la lista

# Mensaje de despedida y lista de invitados
print("\nLista de invitados:")
for invitado in invitados:
    print("-", invitado)
    
#Mensaje de despedida y lista de invitados de Daniel

print("\nLos invitados son los siguientes:\n")
for i in range (len(invitados)):
	print(f"{i+1}. {invitados[i]}")

print("\nGracias por usar el registro de invitados. ¡Que disfruten la fiesta!")

invitados = []      # Creo una lista de invitados vacia

#Otra opción

print("\n - BIENVENID@ AL PYTHON FESTIVAL 2025 - \n")   # Bienvenida

invitados = []

while True:  # Bucle infinito
    invitados.append(str(input("Introduce el nombre de un invitado o la palabra FIN:  ").upper()))   # invitado a la lista!
    if invitados[-1] == "FIN":  # Si el último invitado es igual a FIN 
        invitados.pop()  # Elimina "FIN" como último elemento de la lista 
        print("\n - LISTA DE INVITADOS - \n", invitados, "\n FIN DE LA APLICACIÓN")  # Imprime la lista de invitados y final
        break  # sale del bucle