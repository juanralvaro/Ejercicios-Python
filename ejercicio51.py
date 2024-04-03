""" Imagina que estás desarrollando un programa para verificar si un número es divisible por una serie de divisores dados. Para esto, debes crear una función llamada **`verificar_divisibilidad(numero, divisores)`** que tome un número y una lista de divisores como entrada y devuelva un mensaje indicando si el número es divisible por alguno de los divisores.

**Requisitos:**

- La función **`verificar_divisibilidad`** debe tomar como argumentos el número a verificar y una lista de divisores.
- Si el número es divisible por alguno de los divisores dados, la función debe devolver "El número es divisible por al menos uno de los divisores".
- Si el número no es divisible por ninguno de los divisores dados, la función debe devolver "El número no es divisible por ninguno de los divisores". """

divisores = [2, 3]

def verificar_divisibilidad(numero: int, divisores: list) -> bool:
    """
    1. Objetivo
    Verificar si un número es divisible por alguno de los números de una lista dada y retornar si es divisible o no por esos números.
    2. Argumentos
    - numero (int): el número del que se pretende verificar su divisibilidad.
    - divisores (list): una lista de números a los cuales se quiere verificar la división.
    3. Qué retorna
    Un mensaje que dice si el número es divisible o no por alguno de los divisores.
    """
    if numero % divisores[0] == 0 or numero % divisores[1] == 0:
        return "El número es divisible por al menos uno de los divisores"
    else:
        return "El número no es divisible por ninguno de los divisores"
    
print(verificar_divisibilidad(5,divisores))