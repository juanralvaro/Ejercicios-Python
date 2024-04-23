"""Crea una clase llamada **`Animal`** que represente a un animal con los siguientes atributos:

- **`nombre`**: El nombre del animal.
- **`especie`**: La especie del animal.

La clase **`Animal`** debe tener los siguientes métodos:

1. **`__init__(self, nombre, especie)`:** Método constructor que inicializa los atributos **`nombre`** y **`especie`**.
2. **`__str__(self)`:** Método especial que devuelve una representación de cadena de la instancia de la clase. Debe devolver una cadena que incluya el nombre y la especie del animal.
3. **`sonido(self)`:** Método que imprime un mensaje que representa el sonido que hace el animal.

Crea una subclase de **`Animal`** llamada **`Perro`** que represente a un perro. La clase **`Perro`** debe tener los siguientes atributos de clase adicionales:

- **`total_perros`**: Un contador que lleva la cuenta de la cantidad total de perros creados.

La clase **`Perro`** debe tener los siguientes métodos adicionales:

1. **`__init__(self, nombre)`:** Método constructor que inicializa el atributo **`nombre`** y aumenta el contador **`total_perros`**.
2. **`__str__(self)`:** Método especial que sobrescribe el método **`__str__`** de la clase base **`Animal`** para incluir el nombre, la especie y una descripción del perro.
3. **`sonido(self)`:** Método que imprime un ladrido, representando el sonido de un perro.

Escribe un programa principal que:

- Cree varias instancias de la clase **`Perro`** con diferentes nombres.
- Muestre la representación de cadena de cada instancia de la clase **`Perro`**.
- Llame al método **`sonido()`** de cada instancia de la clase **`Perro`**.
- Muestre el valor del contador **`total_perros`** al finalizar."""

class Animal:
    sonido = "sonar"
    def __init__(self, nombre, especie):
        """
        Objetivo: Crear un animal con un nombre y una especie.
        
        Argumentos:
        
        -self: referencia al objeto actual cuando se llama al método.
        -nombre (str): nombre del animal.
        -especie (int): especie del animal.
        
        Retorna: nada.
        """
        self.nombre = nombre
        self.especie = especie
        
    def __str__(self):
        """
        Objetivo: devolver el nombre y la especie del animal.
        
        Argumento:
        
        -self: referencia al objeto actual cuando se llama al método.

        Método:
        
        super().__init__: sobreescribe el método __init__ de animal.
        
        Retorna: un string formateado que muestra el nombre y la especie del animal.
        """
        return f"El animal se llama {self.nombre} y pertenece a la especie {self.especie}."
    
    def sonido(self):
        """
        Objetivo: imprime el sonido del animal.
        
        Argumento:
        
        -self: referencia al objeto actual cuando se llama al método.
        
        Método:
        
        print(): Imprime el sonido del animal.
        
        Retorna: el sonido del animal.
        """
        print("El animal hace un sonido.")
    
class Perro(Animal):
    total_perros = 0
    sonido = "guau"
    descripcion = "cuatro patas"
    def __init__(self, nombre, especie):
        """
        Objetivo: Crear un perro con un nombre y una especie y añadirlo a un total de perros
        
        Argumentos:
        
        -self: referencia al objeto actual cuando se llama al método.
        -nombre (str): nombre del perro.
        -especie (int): especie del perro.

        Método:
        
        super().__init__: sobreescribe el método __init__ de animal.

        Perro.total_perros += 1 : aumenta el total de perros en uno.
        
        Retorna: nada.
        """
        super().__init__(nombre, especie)
        Perro.total_perros += 1
        
    def __str__(self):
        """
        Objetivo: devolver el nombre, especie y descripción del perro.
        
        Argumento:
        
        -self: referencia al objeto actual cuando se llama al método.

        Método:
        
        super().__init__: sobreescribe el método __init__ del animal.
        
        Retorna: un string formateado que muestra el nombre, la especie y la descripción del perro.
        """
        return f"El perro se llama {self.nombre}, pertenece a la especie {self.especie} y tiene {self.descripcion}."
        
    def sonido(self):
        """
        Objetivo: imprime el sonido del animal.
        
        Argumento:
        
        -self: referencia al objeto actual cuando se llama al método.
        
        Método:
        
        print(): Imprime el sonido del animal.
        
        Retorna: el sonido del animal.
        """
        print("El perro ladra.")
    
animal_uno = Animal("Garfield","Gato")
print(animal_uno.sonido)
perro_uno = Perro("Toby", "caniche")
perro_dos = Perro("Cobi", "mascota")
perro_tres = Perro("D'Artacán", "mastín")
print(perro_uno)
print(perro_dos)
print(perro_tres)
perro_uno.sonido()
perro_dos.sonido()
perro_tres.sonido()
print("El número de perros registrados es",Perro.total_perros)