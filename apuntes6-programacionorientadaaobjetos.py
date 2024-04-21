# --------- PROGRAMACIÓN ORIENTADA A OBJETOS (POO)--------------
"""from --archivo-- import --clase--"""

"""
Surge en los años '70. Utiliza las clases para organizar el código de tal forma que nos permita agrupar conjuntos de variables y funciones para posteriormente utilizarlas.
Un objeto es una entidad que combina datos (llamados atributos) y funciones especifícas de estas clases (llamados métodos)
Para definir clases, utilizaré el CamelCase en caso de el naming de mis clases incluyan dos o más palabras. Además está aceptado y normalizado el uso de mayúsculas para definir las clases. Debemos tener en cuenta que Python es keysensitive, es decir:

class Coche:
class coche:

--> No es lo mismo

"""
""" class Coche:
    def acelerar(self): #El parámetro self es una referencia a la propia instancia de la clase. Es necesario incluirlo como primer parámetro en TODOS los métodos de instancias de una clase de Python
       print("El coche está acelerando")
       
    def frenar(self):
        print("El coche está frenando")
        
        
mi_coche = Coche()

mi_coche.frenar()
 """

""" class Cliente:
    
    def __init__(self, codigo_postal, direccion):
        self.codigo_postal = codigo_postal
        self.direccion = direccion 
    
    def establecer_nombre(self, nombre): #Este método nos permite establecer un nombre de mi cliente. Coge un parámetro 'nombre' y lo asigna al atributo nombre del objeto Cliente
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre
    
    def establecer_edad(self, edad: int):
        self.edad = edad
    
    def obtener_edad(self):
        return self.edad


#Creo una instancia (copia) de mi clase y asigno valores a los atributos de mi instancia      
cliente_uno = Cliente()
cliente_uno.direccion = "Avenida de los Rosales, 357 AtB"

#Creo más instancias de mi clase 
cliente_dos = Cliente()
cliente_tres = Cliente()
#Asigno un valor a la variable nombre_uno
nombre_uno = str(input("Establece un nombre"))
#Asigno un valor a la variable edad_uno
edad_uno = int(input("Dime tu edad"))
#Establezco un valor al atributo nombre de mi clase Cliente
cliente_dos.establecer_nombre("Hachiko")
#Asigno al atributo nombre de mi objeto cliente_uno el valor almacenado en la variable nombre_uno
cliente_uno.establecer_nombre(nombre_uno)
#Asigno al atributo edad de mi objeto cliente_uno el valor 40
cliente_uno.establecer_edad(40)
#Imprimo el nombre de mi cliente_uno utilizando el método obtener_nombre de mi clase Cliente
print("Nombre de mi cliente uno es:", cliente_uno.obtener_nombre())
        
 """

""" 
· Clases: Bloques de construcción que me permiten definir plantillas. Estas plantillas van a definir las propiedades y comportamientos de un objeto. 

· Objeto: Los objetos son instancias de las clases. Cada objeto creado a partir de una clase tiene su propia copia de atributos y de métodos, pudiendo llamar a esos métodos. 

· Atributo: Los atributos son variables asociadas a una clase que representan sus carácterísticas (en el ejemplo de la clase cliente: nombre, edad). Pueden ser datos simples como números o cadenas, o incluso otros objetos como ya veremos.
 
· Métodos: Los métodos son funciones asociadas a una clase que definen su comportamiento. Pueden acceder y modificar los atributos del objeto al que pertenecen. 

"""

#EJERCICIO RÁPIDO
""" Crea una clase TAREA que permita establecer un nombre y una prioridad
 Crear una instancia de la clase tarea.
 Pide al usuario que introduzca el nombre de la tarea y asignáselo a el atributo nombre 
Pide al usuario que introduzca la prioridad de la tarea y asignáselo a el atributo prioridad 
 Muestra la tarea 1 utilizando la función print()
 Crea una tarea 2 siguiendo los mismos pasos que has realizado para crear la tarea 1 """

""" class Tarea:
    
    def establecer_nombre(self,nombre):
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre
        
    def establecer_prioridad(self,prioridad):
        self.prioridad = prioridad
        
    def obtener_prioridad(self):
        return self.prioridad
    
tarea_uno = Tarea()

tarea_uno.establecer_nombre(str(input("Introduzca el nombre de la tarea: ")))
tarea_uno.establecer_prioridad(str(input("Introduzca la proridad de la tarea: ")))

print(f"La tarea uno, {tarea_uno.obtener_nombre()}, tiene prioridad {tarea_uno.obtener_prioridad()}.")

tarea_dos = Tarea()

tarea_dos.establecer_nombre(str(input("Introduzca el nombre de la tarea: ")))
tarea_dos.establecer_prioridad(str(input("Introduzca la prioridad de la tarea: ")))

print(f"La tarea dos, {tarea_dos.obtener_nombre()}, tiene prioridad {tarea_dos.obtener_prioridad()}.")
 """

""" class CocheEjemplo:
    #PRIMER BLOQUE: ATRIBUTOS ESTÁTICOS
    material = "plástico" #Característica/atributo estático
    
    #SEGUNDO BLOQUE: ATRIBUTOS DINÁMICOS
    #Método especial constructor
    def __init__(self, color, puertas, llantas): #Atributos que serán definidos en cada una de las instancias de la clase
        self.color = color
        self.puertas = puertas
        self.llantas = llantas
   
    
    #TERCER BLOQUE: MÉTODOS
    #Método de instancia
    def arrancar(self):
        print(f"El coche {self.color} está arrancando")
    
coche_uno = CocheEjemplo("rojo", "3 puertas", "5 llantas")
coche_dos = CocheEjemplo("amarillo", "5 puertas", "4 llantas")


coche_uno.arrancar() """
""" 
Caracteríscas del coche 1 son:
· Rojo
· 3 puertas
· 5 llantas
· Material plástico
Caracteríscas del coche 2 son:
· Amarillo
· 5 puertas
· 4 llantas
· Material plástico

"""
""" print(coche_dos.material)         """
""" class Persona:
    def __init__(self, nombre:str, edad:int, color_piel:str, profesion:str, estado_civil:str):
        self.nombre = nombre
        self.edad = edad
        self.color_piel = color_piel
        self.profesion = profesion
        self.estado_civil = estado_civil
        
    def hablar(self):
        print(f"{self.nombre} puede hablar.")
        
    def caminar(self):
        print(f"{self.nombre} puede caminar.")
        
    def mirar(self):
        print(f"{self.nombre} puede mirar.")
        
    def nacer(self):
        print(f"{self.nombre} ha nacido.")
        
    def morir(self):
        print(f"{self.nombre} morirá.")
        
sandra = Persona("Sandra",22,"morena","deportista","soltera")
carlos = Persona("Carlos",28,"blanco","abogado","casado")

print(f"{sandra.nombre} tiene {sandra.edad} años, es {sandra.color_piel}, es {sandra.profesion} y es {sandra.estado_civil}.")
sandra.hablar()
sandra.caminar()
sandra.mirar()
sandra.nacer()
sandra.morir()

print(f"\n{carlos.nombre} tiene {carlos.edad} años, es {carlos.color_piel}, es {carlos.profesion} y es {carlos.estado_civil}.")
carlos.hablar()
carlos.caminar()
carlos.mirar()
carlos.nacer()
carlos.morir() """

#EJERCICIO TRABAJADOR RESUELTO CON MÉTODOS DE CLASE
""" class Trabajador:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        
    @classmethod 
    #Este método se asocia con la clase y no con los objetos  
    #Defino una función para que el usuario puedad agregar un nuevo trabajador
    def agregar_trabajador(cls, lista_trabajadores):
        print("Introduce los datos del nuevo trabajador:\n")
        nombre = str(input("Introduce el nombre del nuevo trabajador:\n"))
        edad = int(input("Introduce la edad del nuevo trabajador:\n"))
        salario = int(input("Introduce el salario del nuevo trabajador:\n"))
        trabajador_nuevo = cls(nombre, edad, salario)
        lista_trabajadores.append(trabajador_nuevo)
    
    @classmethod 
    def mostrar_trabajador(cls, lista_trabajadores):
        print("Lista de trabajadores:\n")
        for i, trabajador in enumerate(lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}")
            print()
            

trabajadores = []

while True:
    print("Selecciona una de las siguientes opciones:\n")
    print("1 - Agregar trabajador\n")
    print("2 - Mostrar trabajadores\n")
    print("3 - Salir\n")
    
    opcion = int(input("Escribe el número vinculado a la opción que deseas: \n"))
    
    if opcion == 1:
        Trabajador.agregar_trabajador(trabajadores)
    elif opcion == 2:
        Trabajador.mostrar_trabajador(trabajadores)
    elif opcion == 3:
        break """
    
#EJERCICIO TRABAJADOR RESUELTO CON MÉTODOS DE INSTANCIA
"""
class TrabajadorDos:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def agregar_trabajador(self, lista_trabajadores):
        print("Introduce los datos del nuevo trabajador:\n")
        nombre = str(input("Introduce el nombre del nuevo trabajador:\n"))
        edad = int(input("Introduce la edad del nuevo trabajador:\n"))
        salario = int(input("Introduce el salario del nuevo trabajador:\n"))
        trabajador_nuevo = TrabajadorDos(nombre, edad, salario)
        lista_trabajadores.append(trabajador_nuevo)
        print("Trabajador agregado corectamente")
     
    def mostrar_trabajador(self, lista_trabajadores):
        print("Lista de trabajadores:\n")
        for i, trabajador in enumerate(lista_trabajadores, start=1):
            print(f"Trabajador {i}:")
            print(f"Nombre: {trabajador.nombre}")
            print(f"Edad: {trabajador.edad}")
            print(f"Salario: {trabajador.salario}")
            print()

trabajadores = []

#Necesito crear una instancia de mi clase para poder trabajar con sus métodos, ya que son métodos de instancia y no son métodos de clase
empresa = TrabajadorDos("", 0, 0)

while True:
    print("Selecciona una de las siguientes opciones:\n")
    print("1 - Agregar trabajador\n")
    print("2 - Mostrar trabajadores\n")
    print("3 - Salir\n")
    
    opcion = int(input("Escribe el número vinculado a la opción que deseas: \n"))
    
    if opcion == 1:
        empresa.agregar_trabajador(trabajadores)
    elif opcion == 2:
        empresa.mostrar_trabajador(trabajadores)
    elif opcion == 3:
        break
    

----- MÉTODO DE CLASE -----
--> Actúa sobre la propia clase, en vez de actuar sonbre las instancia
--> Pueden ser llamados directamente desde la clase sin necesidad de crear una instancia.
--> Se definen utilizando el decorador @classmethod y automáticamente va a tomar como primer parámetro 'cls'
--> Pueden ser llamados directamente desde la clase, sin necesidad de crear una instancia 

class MiClase:
    @classmethod
    def mi_metodo_de_clase(cls, parámetro1, parametro2....)
    --> Utilizo cls para acceder a la clase.
    --> Realizar operaciones vinculadas con la clase.
    
----- MÉTODO DE INSTANCIA -----
--> Actúa siempre sobre las instancias individuales de una clase
--> Son utilizados para realizar operaciones específicas para cada instancia de la clase
--> Se definen dentro de la clase sin utilizar ningún decorador y automáticamente utiliza como primer parámetro 'self'. 
--> Podré acceder a los atributos de la instancia utilizando 'self'
"""
#EJEMPLO MÉTODO DE INSTANCIA
""" class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}, y tengo {self.edad} años"
    
persona_uno = Persona("Juan", 30)
persona_dos = Persona("Pepe", 24)

print(persona_uno.saludar())
print(persona_dos.saludar())

#EJEMPLO MÉTODO DE CLASE
class Loteria:
    coste_boleto_euros = 6
    
    def __init__(self, boletos):
        self.boletos = boletos
        
    @classmethod
    def definir_nuevo_coste_boleto_euros(cls, nuevo_valor):
        cls.coste_boleto_euros = nuevo_valor
    
    @classmethod
    def calcular_coste_boletos(cls, boletos):
        return cls.coste_boleto_euros * boletos

#Llamar al método de clase para definir pi sin necesidad de crear previamente una instancia
nuevo_valor = int(input("Introduce un nuevo coste del boleto en euros: "))
Loteria.definir_nuevo_coste_boleto_euros(nuevo_valor)
#Llamar al método de clase para calcular el área del círculo sin necesidad de crear previamente una instancia
print(Loteria.calcular_coste_boletos(12)) """

# CONTINUAMOS CON EL EJEMPLO BIBLIOTECA

""" class Libro:
    #Este atributo de clase hace referencia a todas las instancias que se creen de esta misma clase. Este valor es común para todas las instancias. 
    cantidad_libros_en_biblioteca = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        #Cada vez que cree una instancia de la clase Linro, quiero que la cantidad de libros en biblioteca se incremente en 1
        Libro.cantidad_libros_en_biblioteca += 1
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de paginas: {self.paginas}\n") """

""" #Creamos dos objetos de la clase Libro      
libro_uno = Libro("El Alquimista", "Paulo Coehlo", 149)
libro_dos = Libro("Juan Salvador Gaviota", "Nader El Yacoubi", 239)

#Modifico el valor de un atributo en una instancia específica
libro_uno.titulo = "Nuevo valor para el título del libro 1"

#Mostrar la información de las instancias que he creado
print("Información libro 1:\n")
libro_uno.mostrar_info()

print("Información libro 2:\n")
libro_dos.mostrar_info()

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")

#Creo un nuevo objeto de la clase Libro
libro_tres = Libro("Python essentials", "Guido Van Rossum", 698)

#Mostrar la cantidad actual de libros en mi biblioteca
print(f"La cantidad actual de libros es: {Libro.cantidad_libros_en_biblioteca}")"""

""" class Coche:
    #Atributo de clase
    cantidad_coches = 0
    
    def __init__(self, marca, modelo):
        #Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        #Incrementar la cantidad de coches cada vez que se cree una instancia
        Coche.cantidad_coches += 1
    
    def __str__(self): #Me sirve para formatear la representación de los objetos
        return f"Nuevo coche de la marca {self.marca} - {self.modelo}"
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, modelo: {self.modelo}")
        
coche_david = Coche("Ferrari", "python")
coche_justo = Coche("LandRover", "freelander")

concesionario = [coche_david, coche_justo]

print(f"La cantidad de coches que existen es: {Coche.cantidad_coches} ")

for _ in concesionario:
    print(_)

coche_david.mostrar_info()
coche_justo.mostrar_info()
class Usuario:
    usuarios = 0
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        Usuario.usuarios += 1

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}. Edad: {self.edad}."
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")

usuario_uno = Usuario("Juan","Pérez",40)
usuario_dos = Usuario("María","Gómez",30)
usuario_tres = Usuario("Pedro","Pérez",20)
        
lista_usuarios = [usuario_uno,usuario_dos,usuario_tres]

for usuario in lista_usuarios:
    print(usuario) """
    
# POO - HERENCIA ****************************************
""" 
· Podemos crear nuevas clases a partir de clases ya existentes. 
· Nos permite que una clase (subclase o clase derivada) herede tanto atributos como métodos de otra clase (superclase o clase base)
· La herencia facilita la reutilización del código y la creación de jerarquías de clases --> Tratamos de promover en todo caso un diseño modular y extensible

"""
#Defino una clase --> SUPERCLASE O CLASE BASE
class Animal:
    tipo = "Mamífero"
    bigotes = "largos y sensibles"
    #Métodos
    pass

#Defino una clase --> SUBCLASE O CLASE DERIVADA
class Perro(Animal):
    #hereda tipo = "Mamífero"
    bigotes = "" #Puedo sobreescribir un atributo heredado de la clase base.
    sonido = "ladrar"
    pass

class Chihuahua(Perro):
    #hereda tipo = "Mamífero"
    #hereda sonido = "ladrar"
    #hereda bigotes = ""
    pass

class Gato(Animal):
    #hereda tipo = "Mamífero"
    #hereda bigotes = "largos y sensibles"
    sonido = "maullar"
    pass

#EJEMPLO 1 de CLASES HEREDADAS

#Definimos una CLASE BASE Vehículo que contenga atributos de instancia y métodos de instancia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_informacion(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo}")

#Definimos una CLASE DERIVADA Coche, que herede los atributos de instancia de la clase base y además añada nuevos atributos. 
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo) #Llamamos al constructor de la clase base para inicializar los atributos de la propia clase. La función super() me permite acceder a los métodos (de clase y de instancia) de la clase padre desde una de sus clases hijas. 
        self.color = color
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Color: {self.color}")
        
coche_uno = Coche("Land Rover","Freelander","Gris")
#Coche.mostrar_informacion(coche_uno)

#ATRIBUTO ESPECIAL __BASE__: Proporciona una referencia de la clase de la cual es derivada. Es decir, me dice quien es su clase padre. En el caso de que no tenga una clase padre, nos remite a un valor object (la base de todas las clases en Python)

""" print(Chihuahua.__base__)
print(Perro.__base__)
print(Animal.__base__) """


#ATRIBUTO ESPECIAL __SUBCLASSES__(): Obtengo una lista de todas las clases derivadas de una clase base.
""" print(Animal.__subclasses__())
print(Perro.__subclasses__()) """

""" print(f"La clase base de Chihuahua es: {Chihuahua.__base__}")
print(f"La clase base de Perro es: {Perro.__base__}")
print(f"La clase base de Animal es: {Animal.__base__}") """



#ATRIBUTO ESPECIAL __MRO__: Method Resolution Order (Orden de Resolución de Métodos). Devuelve una tupla que nos muestra el orden en el que las clases se van a buscar en mi jerarquía de clases a la hora de resolver atributos y métodos en una instancia. 

""" print(Chihuahua.__mro__)
print("*" * 100)
print(Perro.__mro__)
print("*" * 100)
print(Animal.__mro__)
print("*" * 100) """

#EJEMPLO

class A:
    nivel_a = 1
    def __init__(self):
        return self.nivel_a
class B(A):
    nivel_b = 2
    def __init__(self):
        return self.nivel_b
class C(B):
    nivel_c = 3
    def __init__(self):
        return self.nivel_c

class D(C):
    nivel_d = 4
    def __init__(self):
        return self.nivel_d

#Ejemplo de uso de __mro__:

""" print(D.__mro__)
print("*" * 106)
print(C.__mro__)
print("*" * 84)
print(B.__mro__)
print("*" * 62)
print(A.__mro__)
print("*" * 40) """

class Doc:
    """
    sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    pass

#print(Doc.__doc__)

"""OTROS ATRIBUTOS ESPECIALES COMUNES"""

#Atributo __doc__: Este atributo va a devolver toda la documentación asociada con una clase.
class Documentacion:
    """
    Nombre de la clase: Documentacion
        Descripción:
        Esta clase se ha definido para documentar y explicar el uso del atributo especial __doc__
    """
    pass

#print(Documentacion.__doc__)

#Atributo __dict__: Este atributo nos devuelve un diccionario que contiene los atributos de la instancia de la clase, incluídos los métodos. CLAVE (nombres de los atributos) - VALOR (valores de los atributos)

""" print(Perro.__dict__) #Nos muestra un diccionario que contiene los atributos de la instancia de la clases dada, en este caso, Perro.

print("Este documento recoge la clase Animal, y las clases derivadas de la class Animal.\nINDICE\n \n- Class Animal" , Animal.__mro__ , "\n  Atributos que contiene:", Animal.__dict__, "\n\n   - Class Perro", Perro.__mro__ , "\n\n        -Class Chihuahua" , Chihuahua.__mro__ ,  "\n Atributos que contiene:", Chihuahua.__dict__, "\n\n  - Class Gato" , Gato.__mro__ , "\n Atributos que contiene:", Gato.__dict__) """

""" A partir del ejemplo de las clases A, B, C y D vas a mostrar la documentación de estas clases, la jerarquía de clases de las que derivan y además los atrubitos de instancia y los métodos de la clase"""

print("\nDOCUMENTO 'GLOBAL':\n\nEste documento recoge por un lado la clase A, y por otro sus clases derivadas: B, C y D.\n\nÍNDICE: \n \n - Clase A", A.__mro__ , "\n   Atributos que contiene:\n  ", A.__dict__, "\n\n     - Clase B", B.__mro__, "\n       Atributos que contiene:\n      ",B.__dict__, "\n\n         - Clase C", C.__mro__, "\n           Atributos que contiene:\n          ", C.__dict__,"\n\n             - Clase D: ", D.__mro__, "\n               Atributos que contiene:\n              ", D.__dict__,"\n") 