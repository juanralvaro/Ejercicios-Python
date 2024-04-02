""" Crea un programa en Python que permita al usuario jugar un juego interactivo de suma. El programa debe seguir las siguientes reglas:

1. Solicita al usuario que introduzca un número que servirá como límite para la suma.
2. Utiliza un bucle **`while`** para permitir al usuario introducir números y sumarlos.
3. Muestra la suma parcial después de cada entrada del usuario.
4. Cuando la suma alcance o supere el límite introducido por el usuario, muestra un mensaje indicando que el límite ha sido alcanzado.
5. Agradece al usuario por jugar a nuestro juego y deséale un buen día 😊. """

print("Bienvenido al juego interactivo de suma.")

limite = int(input("Introduce una cantidad límite: "))

while True:
    numero = int(input("Introduce un número: "))
    suma = numero
    while suma <= limite:
        numero = int(input("Introduce un número: "))
        suma += numero
        print(f"La suma es {suma}")
    else:
        print("Ha alcanzado el límite.")
        break
    
print("Gracias por jugar. ¡Buen día!")