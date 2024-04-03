""" Has sido contratado por una empresa de detectives para desarrollar un programa que les ayude a identificar si una serie de palabras en clave son utilizadas en un mensaje. Crea una función llamada **`buscar_palabras_clave(mensaje)`** que tome un mensaje como entrada y devuelva un mensaje indicando si se encontraron o no palabras clave en el mensaje.

1. Define una lista de palabras clave que se utilizarán para buscar en el mensaje.
2. La función **`buscar_palabras_clave`** debe tomar como argumento el mensaje a analizar.
3. Si alguna de las palabras clave está presente en el mensaje, la función debe devolver "Se han encontrado palabras clave en el mensaje".
4. Si ninguna de las palabras clave está presente, la función debe devolver "No se han encontrado palabras clave en el mensaje".
5. Resuelve este ejercicio dos veces: la primera aplicando el retorno condicional y la segunda aplicando el retorno temprano """

# Retorno condicional
def buscar_palabras_clave(mensaje: str) -> bool:
    """
    1. Objetivo:
    El objetivo de la función es buscar unas palabras clave y retornar si se han encontrado o no.
    2. Argumento:
    - mensaje (str): Es el nombre del mensaje a analizar.
    3. Qué retorna:
    Una expresión que nos indica si se han encontrado o no palabras clave en el mensaje.
    """
    palabras_clave  = ["python", "programación"]
    if mensaje in palabras_clave:
        return "Se han encontrado palabras clave en el mensaje"
    else:
        return "No se han encontrado palabras clave en el mensaje"

# Retorno temprano
def buscar_palabras_clave(mensaje: str) -> bool:
    """
    1. Objetivo:
    El objetivo de la función es buscar unas palabras clave y retornar si se han encontrado o no.
    2. Argumento:
    - mensaje (str): Es el nombre del mensaje a analizar.
    3. Qué retorna:
    Una expresión que nos indica si se han encontrado o no palabras clave en el mensaje.
    """
    palabras_clave = ["python", "programación"]
    if mensaje is palabras_clave[0] or palabras_clave[1]:
        return "Se han encontrado palabras clave en el mensaje"
    return "No se han encontrado palabras clave en el mensaje"