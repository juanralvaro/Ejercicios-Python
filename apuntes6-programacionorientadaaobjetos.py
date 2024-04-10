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
· Atributo: 

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

