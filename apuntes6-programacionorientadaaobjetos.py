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
class Trabajador:
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
        break
    
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
class Persona:
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
print(Loteria.calcular_coste_boletos(12))