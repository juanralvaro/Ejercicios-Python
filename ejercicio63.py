"""En este ejercicio, vamos a simular una aventura espacial donde exploramos diferentes planetas en busca de recursos. Utilizaremos el módulo **`random`** para tomar decisiones aleatorias durante la aventura.

1. **Selección aleatoria del destino inicial**:
    - Utiliza el método **`choice(seq)`** para seleccionar aleatoriamente un planeta de una lista de destinos posibles. Imprime el planeta seleccionado como el destino inicial de la aventura.
2. **Generación aleatoria de eventos en el espacio**:
    - Utiliza el método **`randint(a, b)`** para generar aleatoriamente un número que represente un evento en el espacio. Dependiendo del número generado, simula diferentes eventos como encuentros con asteroides, tormentas solares, o avistamientos de naves extraterrestres.
3. **Selección aleatoria de recursos en un planeta**:
    - Utiliza el método **`choice(seq)`** para seleccionar aleatoriamente un recurso importante de una lista de recursos disponibles en el planeta explorado. Imprime el recurso seleccionado."""
    
import random

destinos = ["Mercurio", "Venus", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno", "Plutón"]

destino_choice = random.choice(destinos)
print("El destino elegido con choice es:",destino_choice)

eventos = list(range(1,4))
evento_choice = random.randint(1,3)
print("El evento elegido con choice es:",evento_choice)
if evento_choice == 1:
    print("Me encuentro con un extraterrestre")
elif evento_choice == 2:
    print("Me encuentro con un asteroide")
else:
    print("Me encuentro con una tormenta solar")
    
recursos = ["agua", "oro", "diamantes", "minerales"]
recurso_choice = random.choice(recursos)
print("El recurso explorado es", recurso_choice)