"""Crea una clase llamada **`Persona`** que represente a una persona con los siguientes atributos:

- **`nombre`**: El nombre de la persona.
- **`edad`**: La edad de la persona.

La clase **`Persona`** debe tener los siguientes métodos:

1. **`__init__(self, nombre, edad)`:** Método constructor que inicializa los atributos **`nombre`** y **`edad`**.
2. **`__str__(self)`:** Método especial que devuelve una representación de cadena de la instancia de la clase. Debe devolver una cadena que incluya el nombre y la edad de la persona.

Además, crea una clase llamada **`Estudiante`** que herede de la clase **`Persona`** y tenga un atributo adicional:

- **`grado`**: El grado del estudiante.

La clase **`Estudiante`** debe tener un método adicional:

1. **`__str__(self)`:** Método especial que sobrescribe el método **`__str__`** de la clase base **`Persona`** para incluir el nombre, la edad y el grado del estudiante.

Escribe un programa principal que:

- Cree una instancia de la clase **`Persona`** con un nombre y una edad.
- Muestre la representación de cadena de la instancia de la clase **`Persona`**.
- Cree una instancia de la clase **`Estudiante`** con un nombre, una edad y un grado.
- Muestre la representación de cadena de la instancia de la clase **`Estudiante`**."""

class Persona:
    def __init__(self, nombre: str, edad: int):
        """
        Objetivo: Crear una persona con un nombre y una edad.
        
        Argumentos:
        
        -self: referencia al objeto actual cuando se llama al método.
        -nombre (str): nombre de la persona.
        -edad (int): edad de la persona.
        
        Retorna: nada.
        """
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        """
        Objetivo: devolver el nombre y edad de la persona.
        
        Argumentos:
        
        -self: referencia al objeto actual cuando se llama al método.
        -nombre (str): nombre de la persona.
        -edad (int): edad de la persona.
        
        Retorna: un string formateado que muestra el nombre y la edad de la persona.
        """
        
        return f"La persona se llama {self.nombre} y tiene {self.edad} años."
        
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, grado: str):
        """
        Objetivo: Crear un estudiante con un nombre, una edad y el grado que cursa.
        
        Argumento:
        
        -self: referencia al objeto actual cuando se llama al método.
        
        Método:
        
        super().__init__: sobreescribe el método __init__ de persona.
        
        Retorna: nada.
        """
        super().__init__(nombre, edad)
        self.grado = grado
        
    def __str__(self):
        """
        Objetivo: devolver el nombre y edad de la persona.
        
        Argumento:
        
        -self: referencia al objeto actual cuando se llama al método.

        Método:
        
        super().__init__: sobreescribe el método __init__ de persona.
        
        Retorna: un string formateado que muestra el nombre, la edad y el grado de la persona.
        """
        return f"El estudiante se llama {self.nombre}, tiene {self.edad} años, y estudia {self.grado}."
        
persona_uno = Persona("Juan", 42)
print(persona_uno)
estudiante_uno = Estudiante("María",23,"Informática")
print(estudiante_uno)