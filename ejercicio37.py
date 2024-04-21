""" 1. Define un diccionario llamado **`enciclopedia_plantas`** que contenga información sobre diferentes plantas. Cada planta será representada por un diccionario anidado con las siguientes claves: "nombre", "especie", "familia", "origen", "altura" y "usos". Puedes agregar al menos 3 plantas con esta estructura.
2. Crea una lista llamada **`nombres_plantas`** que contenga los nombres de todas las plantas presentes en la enciclopedia.
3. Agrega una nueva planta a la enciclopedia. Para ello, solicita al usuario que ingrese los detalles de la nueva planta y agrégalos al diccionario principal **`enciclopedia_plantas`**.
4. Imprime la información de todas las plantas de la enciclopedia. Recorre la lista de nombres de plantas (**`nombres_plantas`**) y utiliza cada nombre para acceder al diccionario correspondiente en **`enciclopedia_plantas`** y mostrar toda la información de la planta.
5. Finalmente, muestra el número total de plantas presentes en la enciclopedia. Utiliza la función **`len()`** para determinar la longitud de la lista de nombres de plantas. """

#Bienvenida
print("Bienvenido al diccionario de plantas.")

#1. Definición diccionario

enciclopedia_plantas = {
    "Planta 1" : {
        "nombre" : str(input("Introduzca el nombre científico de la planta: ")),
        "especie" : str(input("Introduzca la especie de la planta: ")),
        "familia" : str(input("Introduzca la familia de la planta: ")),
        "origen" : str(input("Introduzca el origen de la planta: ")),
        "altura" : float(input("Introduzca el tamaño de la planta en metros: ")),
        "usos" : str(input("Introduzca los usos de la planta: "))
    },
    "Planta 2" : {
        "nombre" : str(input("Introduzca el nombre científico de la planta: ")),
        "especie" : str(input("Introduzca la especie de la planta: ")),
        "familia" : str(input("Introduzca la familia de la planta: ")),
        "origen" : str(input("Introduzca el origen de la planta: ")),
        "altura" : float(input("Introduzca el tamaño de la planta en metros: ")),
        "usos" : str(input("Introduzca los usos de la planta: "))
    },
    "Planta 3" : {
        "nombre" : str(input("Introduzca el nombre científico de la planta: ")),
        "especie" : str(input("Introduzca la especie de la planta: ")),
        "familia" : str(input("Introduzca la familia de la planta: ")),
        "origen" : str(input("Introduzca el origen de la planta: ")),
        "altura" : float(input("Introduzca el tamaño de la planta en metros: ")),
        "usos" : str(input("Introduzca los usos de la planta: "))
    }
}

#2. Lista con nombres de plantas
nombres_plantas = list(enciclopedia_plantas.values())

#3. Agregar una nueva planta
nueva_planta = {
        "nombre" : str(input("Introduzca el nombre científico de la planta: ")),
        "especie" : str(input("Introduzca la especie de la planta: ")),
        "familia" : str(input("Introduzca la familia de la planta: ")),
        "origen" : str(input("Introduzca el origen de la planta: ")),
        "altura" : float(input("Introduzca el tamaño de la planta en metros: ")),
        "usos" : str(input("Introduzca los usos de la planta: "))
    
}
enciclopedia_plantas.update(nueva_planta)
nombres_plantas.append(nueva_planta)
print(nombres_plantas)

#4. Imprimir información de las plantas
for planta in nombres_plantas:
    print(planta)

#5. Plantas presentes en la enciclopedia
longitud_planta = len(nombres_plantas)
print(f"Hay {longitud_planta} plantas en la enciclopedia.")
print(nombres_plantas)