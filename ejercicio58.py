""" Crea una clase Usuario en Python que defina los atributos y los métodos que necesita el usuario tipo que deberás crear junto a tus compañeros para el proyecto final. 

Añade un atributo de clase para contabilizar el número de instancias que se creen de la clase usuario, de tal forma que en todo momento podemos saber el número de usuarios creados en nuestro programa. """

class Usuario:
    usuarios = 0
    
    def __init__(self, nombre:str, apellido_uno:str, apellido_dos:str, dni:str, direccion:str, localidad:str, telefono:int, email:str):
        """
        Objetivo: Define los datos del socio a crear. Incrementa el número de usuarios en uno.

        Atributos:
            nombre (str): nombre del socio.
            apellido_uno (str): primer apellido del socio.
            apellido_dos (str): segundo apellido del socio.
            dni (str): DNI del socio.
            direccion (str): residencia del socio.
            localidad (str): localidad de residencia del socio.
            telefono (int): teléfono del socio.
            email (str): correo electrónico del socio.
            
        Retorna:
            Nada.
        """
        self.nombre = nombre
        self.apellido_uno = apellido_uno
        self.apellido_dos = apellido_dos
        self.dni = dni
        self.direccion = direccion
        self.localidad = localidad
        self.telefono = telefono
        self.email = email
        Usuario.usuarios += 1
        
    def __str__(self):
        """
        Objetivo: Muestra la manera en la que se mostrarán los datos al hacer un print de usuario.

        Atributos: el self para hacer referencia al objeto que se está manipulando cuando se llama al método.

        Retorna: La descripción del socio.
        """
        return f"Socio: {self.nombre} {self.apellido_uno} {self.apellido_dos}. DNI: {self.dni}. Domicilio: {self.direccion}. Localidad: {self.localidad}. Teléfono: {self.telefono}. Correo electrónico: {self.email}."
    
socio_uno = Usuario("Juan","Pérez","López","54681887M","C/María de Molina, 1","Madrid",972837291,"juanito@gmail.com")
socio_dos = Usuario("María","López","Yáñez","14788787Z","Passeig de Gràcia, 34","Barcelona",654684487,"maria@hotmail.com")

socios = [socio_uno, socio_dos]

for socio in socios:
    print(socio)
    
print(f"Número de socios: {Usuario.usuarios}.")