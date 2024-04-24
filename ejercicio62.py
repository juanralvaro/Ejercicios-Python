"""En este ejercicio, vamos a crear un programa que simula una lotería. La lotería consistirá en extraer aleatoriamente números de una lista de números posibles. Utilizaremos los diferentes métodos del módulo **`random`** para realizar estas extracciones.

1. **Definición de la lotería**:
    - Crea una lista llamada **`numeros_posibles`** que contenga todos los números posibles para la lotería, desde 1 hasta 50:
        
        ```python
        numeros_posibles = list(range(1, 51))
        ```
        
2. **Método `randint(a, b)`**:
    - Utiliza el método **`randint(a, b)`** para seleccionar aleatoriamente un número de la lista **`numeros_posibles`**. Imprime este número seleccionado.
3. **Método `uniform(a, b)`**:
    - Utiliza el método **`uniform(a, b)`** para seleccionar aleatoriamente un número de la lista **`numeros_posibles`**. Imprime este número seleccionado.
4. **Método `choice(seq)`**:
    - Utiliza el método **`choice(seq)`** para seleccionar aleatoriamente un número de la lista **`numeros_posibles`**. Imprime este número seleccionado."""
    
import random

numeros_posibles = list(range(1, 51))
print(numeros_posibles)

numero_randint = random.randint(1, 50)
print(f"El número seleccionado con randint es: {numero_randint}")

numero_uniform = random.uniform(1,50)
print(f"El número seleccionado con uniform es: {numero_uniform}")

numero_choice = random.choice(numeros_posibles)
print(f"El número seleccionado con choice es: {numero_choice}")