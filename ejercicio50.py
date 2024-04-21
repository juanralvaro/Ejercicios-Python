""" Has sido contratado por una empresa de detectives para desarrollar un programa que les ayude a identificar si una serie de palabras en clave son utilizadas en un mensaje. Crea una función llamada **`buscar_palabras_clave(mensaje)`** que tome un mensaje como entrada y devuelva un mensaje indicando si se encontraron o no palabras clave en el mensaje.

1. Define una lista de palabras clave que se utilizarán para buscar en el mensaje.
2. La función **`buscar_palabras_clave`** debe tomar como argumento el mensaje a analizar.
3. Si alguna de las palabras clave está presente en el mensaje, la función debe devolver "Se han encontrado palabras clave en el mensaje".
4. Si ninguna de las palabras clave está presente, la función debe devolver "No se han encontrado palabras clave en el mensaje".
5. Resuelve este ejercicio dos veces: la primera aplicando el retorno condicional y la segunda aplicando el retorno temprano """

#-- Resultado aplicando el retorno condicional --

# Definir las palabras clave
palabras_clave = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave(mensaje):
    """Descripción:
    buscar_palabras_clave _summary_

    Argumentos de la función: 
        mensaje (_type_): _description_

    Retorno:
        _type_: _description_
    """
    encontrado = False
    for palabra in palabras_clave:
        if palabra in mensaje:
            encontrado = True
            break
    if encontrado:
        return "Se han encontrado palabras clave en el mensaje"
    else:
        return "No se han encontrado palabras clave en el mensaje"

# Ejemplos de uso
mensaje1 = str(input("Ingresa una frase para evaluar:\n"))
mensaje2 = str(input("Ingresa una frase para evaluar:\n"))
mensaje3 = str(input("Ingresa una frase para evaluar:\n"))

print("Mensaje 1:")  
buscar_palabras_clave(mensaje1)
print("Mensaje 2:")  
buscar_palabras_clave(mensaje2)
print("Mensaje 3:") 
buscar_palabras_clave(mensaje3)

#-- Resultado aplicando el retorno temprano --

# Definir las palabras clave
palabras_clave1 = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave1(mensaje):
    for palabra in palabras_clave1:
        if palabra in mensaje:
            return "Se han encontrado palabras clave en el mensaje"
    return "No se han encontrado palabras clave en el mensaje"

# Ejemplos de uso
mensaje1 = str(input("Ingresa una frase para evaluar:\n"))
mensaje2 = str(input("Ingresa una frase para evaluar:\n"))
mensaje3 = str(input("Ingresa una frase para evaluar:\n"))

print("Mensaje 1:")  
buscar_palabras_clave1(mensaje1)
print("Mensaje 2:")  
buscar_palabras_clave1(mensaje2)
print("Mensaje 3:") 
buscar_palabras_clave1(mensaje3)

#-- Resultado aplicando el retorno condicional y mostrando al usuario todas las palabras que coinciden con las palabras clave  --

# Definir las palabras clave
palabras_clave2 = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave2(mensaje):
    """Descripción:
    buscar_palabras_clave2 _summary_

    Argumentos de la función: 
        mensaje (_type_): _description_

    Retorno:
        _type_: _description_
    """
    encontrado = []
    for palabra in palabras_clave2:
        if palabra in mensaje:
            encontrado.append(palabra)
    if len(encontrado) >= 1:
        print("Se han encontrado palabras clave en el mensaje:", encontrado)
    else:
        print("No se han encontrado palabras clave en el mensaje")

# Ejemplos de uso
mensaje1 = str(input("Ingresa una frase para evaluar:\n"))
mensaje2 = str(input("Ingresa una frase para evaluar:\n"))
mensaje3 = str(input("Ingresa una frase para evaluar:\n"))

print("Mensaje 1:")  
buscar_palabras_clave2(mensaje1)
print("Mensaje 2:")  
buscar_palabras_clave2(mensaje2)
print("Mensaje 3:") 
buscar_palabras_clave2(mensaje3)

#-- Resultado aplicando el retorno condicional y solo una palabra a evaluar en mi función--

# Definir las palabras clave
palabras_clave3 = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave3(palabra):
    """Descripción:
    buscar_palabras_clave3 _summary_

    Argumentos de la función: 
        mensaje (_type_): _description_

    Retorno:
        _type_: _description_
    """

    if palabra in palabras_clave2:
        return "Se han encontrado palabras clave en la palabra"
    else:
        return "No se han encontrado palabras clave en la palabra"

# Ejemplos de uso
palabra1 = str(input("Ingresa una palabra para evaluar:\n"))
palabra2 = str(input("Ingresa una palabra para evaluar:\n"))
palabra3 = str(input("Ingresa una palabra para evaluar:\n"))

print("palabra 1:", buscar_palabras_clave3(palabra1))  
print("palabra 2:", buscar_palabras_clave3(palabra2))  
print("palabra 3:", buscar_palabras_clave3(palabra3))