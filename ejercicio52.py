""" - 52- Clase básica Persona (Dificultad baja)
    1. Crea una clase llamada **`Persona`** con los siguientes atributos:
        - **`nombre`**: El nombre de la persona.
        - **`edad`**: La edad de la persona.
    2. La clase **`Persona`** debe tener los siguientes métodos:
        - **`__init__(self, nombre, edad)`**: Método constructor que inicializa los atributos **`nombre`** y **`edad`**.
        - **`presentarse(self)`**: Método que imprime un mensaje de presentación de la persona, mostrando su nombre y edad.
    3. Desarrolla un programa principal que permita al usuario:
        - Crear instancias de la clase **`Persona`**.
        - Establecer los valores de los atributos **`nombre`** y **`edad`**.
        - Invocar el método **`presentarse()`** para cada instancia creada."""
        
class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, y tengo {self.edad} años."

print("Bienvenido al gestor de personas.")
print("Por favor, ingrese nombre y edad de la primera persona:")
    
persona1 = Persona(str(input()), int(input()))

print("Por favor, ingrese nombre y edad de la segunda persona:")

persona2 = Persona(str(input()), int(input()))

print("Que se presenten las personas:")

print(persona1.presentarse())
print(persona2.presentarse())