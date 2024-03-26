""" Vamos a crear un programa que permita gestionar una lista de la compra. El programa solicitará al usuario que introduzca los elementos que desea comprar y los agregará a una lista. Cuando el usuario escriba "fin", el programa mostrará la lista de la compra y terminará.
    
    Instrucciones:
    
    1. Inicia el programa con un mensaje de bienvenida.
    2. Crea una lista vacía llamada **`lista_compra`**.
    3. Utiliza un bucle **`while`** para solicitar al usuario que introduzca un elemento que desea comprar.
    4. Dentro del bucle, agrega cada elemento introducido por el usuario a la lista **`lista_compra`**.
    5. Si el usuario escribe "fin", sal del bucle.
    6. Después de salir del bucle, muestra un mensaje de despedida y la lista de la compra. """    

print("Bienvenido a la lista de la compra PRO.")

lista_compra = []

while True:
    elemento = str(input("\nIntroduzca un elemento que desee comprar; si ya acabó diga 'fin': "))
    lista_compra.append(elemento)
    if elemento == "fin":
        break
lista_compra.remove("fin")
print("\nGracias por comprar estos productos:", lista_compra)