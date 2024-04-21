""" 1. Crea cuatro diccionarios, uno para cada tipo de colección de datos: listas, tuplas, conjuntos y diccionarios.
2. Cada diccionario contendrá las siguientes claves con sus respectivos valores:
    - **Definición:** Una breve definición del tipo de colección de datos.
    - **Mutabilidad:** Una descripción de si la colección es mutable o inmutable.
    - **Acceso a elementos:** Una explicación de cómo se accede a los elementos en la colección.
    - **Tipos de datos:** Los tipos de datos que la colección puede contener.
    - **Orden:** Una descripción sobre si la colección mantiene el orden de los elementos.
    - **Duplicados:** Una explicación sobre si la colección permite elementos duplicados.
    - **Métodos:** Un diccionario anidado que incluya los métodos relevantes para cada tipo de colección, donde la clave será el nombre del método y el valor será una breve descripción de su función.
3. Cada diccionario debe estar almacenado en una variable con un nombre que represente el tipo de colección correspondiente (por ejemplo, **`diccionario`**, **`conjunto`**, **`listas`**, **`tuplas`**).
4. Implementa un programa que permita a los usuarios consultar la información sobre cada tipo de colección de datos.
    - El programa debe solicitar al usuario que introduzca el nombre de la colección de datos que desea consultar.
    - Luego, el programa mostrará todos los detalles y métodos asociados con la colección seleccionada. """

#1,2,3. Creación de diccionarios, entrada de datos y asignación de nombres

listas = {
    "Definición listas": "definición",
    "Mutabilidad listas": "descripción",
    "Acceso a elementos listas": "explicación",
    "Tipos de datos listas": "tipos de datos",
    "Orden listas": "explicación",
    "Duplicados listas": "explicación",
    "Métodos listas": {
        "método relevante listas 1": "descripción 1",
        "método relevante listas 2": "descripción 2", 
        "método relevante listas 3": "descripción 3"
    }
}

print(listas)

tuplas = { 
    "Definición tuplas": "definición",
    "Mutabilidad tuplas": "descripción",
    "Acceso a elementos tuplas": "explicación",
    "Tipos de datos tuplas": "tipos de datos",
    "Orden tuplas": "explicación",
    "Duplicados tuplas": "explicación",
    "Métodos tuplas": {
        "método relevante tuplas 1": "descripción 1",
        "método relevante tuplas 2": "descripción 2",
        "método relevante tuplas 3": "descripción 3"
    }
}

print(tuplas)

conjuntos = {
    "Definición conjuntos": "definición",
    "Mutabilidad conjuntos": "descripción",
    "Acceso a elementos conjuntos": "explicación",
    "Tipos de datos conjuntos": "tipos de datos",
    "Orden conjuntos": "explicación",
    "Duplicados conjuntos": "explicación",
    "Métodos conjuntos":{
        "método relevante conjuntos 1": "descripción 1",
        "método relevante conjuntos 2": "descripción 2",
        "método relevante conjuntos 3": "descripción 3"
    }
}

print(conjuntos)

diccionarios = {
    "Definición diccionarios": "definición", 
    "Mutabilidad diccionarios": "descripción", 
    "Acceso a elementos diccionarios": "explicación", 
    "Tipos de datos diccionarios": "tipos de datos", 
    "Orden diccionarios": "explicación", 
    "Duplicados diccionarios": "explicación", 
    "Métodos diccionarios": {
        "método relevante diccionarios 1": "descripción 1",
        "método relevante diccionarios 2": "descripción 2",
        "método relevante diccionarios 3": "descripción 3"
    }
}

#4. Creación de buscador de información
print("Bienvenido al buscador de información en diccionarios.")

diccionario = [listas, tuplas, conjuntos, diccionarios]

diccionario_buscado = diccionario[int(input("Introduzca el diccionario buscado: 0 - listas, 1 - tuplas, 2 - conjuntos, 3 - diccionarios: "))]

print(diccionario_buscado)