#Definir la clase Socio:

class Usuario:
    def __init__(self, id: str, nombre: str, apellido_uno: str, apellido_dos: str, edad: int, direccion: str, localidad: str, provincia: str, telefono: str, email: str, aprobacion_privacidad: bool) -> None:
        """
        1. Objetivo de la función: define los datos personales de un socio.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        - id (str): es la id del socio.
        - nombre (str): es el nombre o nombres del socio.
        - apellido_uno (str): es el primer apellido del socio.
        - apellido_dos (str): es el segundo apellido del socio.
        - edad (int): es la edad del socio.
        - direccion (str): es la dirección donde vive el socio.
        - localidad (str): es la localidad donde vive el socio.
        - provincia (str): es la provincia donde vive el socio.
        - telefono (str): es el teléfono del socio.
        - email (str): es el correo electrónico del socio.
        - aprobacion_privacidad (bool): permite o no la privacidad.
        
        3. Retorna: no retorna nada.

    """
        self.id = id
        self.nombre = nombre
        self.apellido_uno = apellido_uno
        self.apellido_dos = apellido_dos
        self.edad = edad
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia
        self.telefono = telefono
        self.email = email
        self.aprobacion_privacidad = aprobacion_privacidad

    def __str__(self) -> str:
        """
        1. Objetivo: devolver los nombres de un socio formateados.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        
        3. Retorna:
        Un texto con los datos personales del socio estilizados.
        
        """
        return f"ID: {self.id}\nNombre: {self.nombre}\nApellido 1: {self.apellido_uno}\nApellido 2: {self.apellido_dos}\nEdad: {self.edad}\nDirección: {self.direccion}\nLocalidad: {self.localidad}\nProvincia: {self.provincia}\nTeléfono: {self.telefono}\nCorreo electrónico: {self.email}"


#Definir la clase Administrador:

class Administrador(Usuario):
    administradores = []
    
#Definir la clase Socio:

class Socio(Usuario):
    socios = []

#Definir la clase ClubSocios:


class ClubSocios:
    def __init__(self) -> None:
        """
        1. Objetivo: inicializar una lista de socios.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        
        3. Retorna: no retorna nada.
        
        """
        self.socios = []

    def crear_socio(self, id: int, nombre: str, apellido_uno: str, apellido_dos: str, edad: int, direccion: str, localidad: str, provincia: str, telefono: int, email: str) -> None:
        """
        1. Objetivo de la función: crear los datos personales de un socio.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        - id (str): es la id del socio.
        - nombre (str): es el nombre o nombres del socio.
        - apellido_uno (str): es el primer apellido del socio.
        - apellido_dos (str): es el segundo apellido del socio.
        - edad (int): es la edad del socio.
        - direccion (str): es la dirección donde vive el socio.
        - localidad (str): es la localidad donde vive el socio.
        - provincia (str): es la provincia donde vive el socio.
        - telefono (str): es el teléfono del socio.
        - email (str): es el correo electrónico del socio.
    
        Atributos:
        
        socio: define una instancia socio con los datos personales del mismo.
        
        Métodos:
        
    
        self.socios.append(socio): añade al socio a la lista de socios
        
        3. Retorna: no retorna nada.

    """
        socio = Socio(id, nombre, apellido_uno, apellido_dos, edad, direccion, localidad, provincia, telefono, email)
        self.socios.append(socio)

    def mostrar_socios(self) -> str:
        """
        1. Objetivo: mostrar una lista de socios.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        
        3. Retorna: imprime la lista de los socios añadidos.
        
        """
        for socio in self.socios:
            print(socio)

    def actualizar_socio(self, id: int, nombre: str, apellido_uno: str, apellido_dos: str, edad: int, direccion: str, localidad: str, provincia: str, telefono: int, email: str) -> bool:
        """
        1. Objetivo de la función: actualizar los datos personales de un socio.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        - id (str): es la id del socio.
        - nombre (str): es el nombre o nombres del socio.
        - apellido_uno (str): es el primer apellido del socio.
        - apellido_dos (str): es el segundo apellido del socio.
        - edad (int): es la edad del socio.
        - direccion (str): es la dirección donde vive el socio.
        - localidad (str): es la localidad donde vive el socio.
        - provincia (str): es la provincia donde vive el socio.
        - telefono (str): es el teléfono del socio.
        - email (str): es el correo electrónico del socio.
        
        Métodos:
        
        Para cada socio a modificar datos, se comprueba si el id coincide con el id del socio.
        Si coincide, se actualizan los datos.
        
        3. Retorna: un True si la operación se ha realizado con éxito o un false si no.

        """
        for socio in self.socios:
            if socio.id == id:
                socio.nombre = nombre
                socio.apellido_uno = apellido_uno
                socio.apellido_dos = apellido_dos
                socio.edad = edad
                socio.direccion = direccion
                socio.localidad = localidad
                socio.provincia = provincia
                socio.telefono = telefono
                socio.email = email    
            return True
        return False

    def eliminar_socio(self, id: int) -> bool: 
        """
        1. Objetivo: eliminar un socio de la lista de socios.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        - id(int): identificador del socio.

        Métodos:
        
        Para cada socio a eliminar, se comprueba si el id coincide con el id del socio.
        Si coincide, se eliminan los datos.
        
        3. Retorna: un True si la operación se ha realizado con éxito o un false si no.
        """
        for socio in self.socios:
            if socio.id == id:
                self.socios.remove(socio)
                return True
        return False

    def buscar_socio(self, id: int) -> str:
        """
        1. Objetivo: busca un socio en la lista de socios.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        - id(int): identificador del socio.

        Métodos:
        
        Para cada socio a buscar, se comprueba si el id coincide con el id del socio.
        Si coincide, se retorna al socio
        
        3. Retorna: el socio buscado si la operación se ha realizado con éxito o nada si no.
        """
        for socio in self.socios:
            if socio.id == id:
                return socio
        return None
    
#Ejemplo de uso:
club = ClubSocios()

# Crear socios
club.crear_socio(1, "Juan", "Pérez", "García", 30, "C/María de Molina, 1", "Madrid", "Madrid", 688487814, "juancho@gmail.com")
club.crear_socio(2, "María", "López", "Pérez", 25, "Passeig de Gràcia, 31", "Barcelona", "Barcelona", 658788124, "marieta@yahoo.es")
club.crear_socio(3, "Pedro", "González", "Latorre", 40, "Praza do Obradoiro, 11", "Santiago de Compostela", "A Coruña", 682346119, "pedrinho@hotmail.com")

# Mostrar socios
print("Lista de socios:")
club.mostrar_socios()

# Actualizar socio
if club.actualizar_socio(2, "Marcel", "Garcia", "Ardèvol", 27, "Av. Lluís Companys, 32", "Barcelona", "Barcelona", 934688872, "mgborras@yahoo.es"):
    print("\nSocio actualizado:")
    print(club.buscar_socio(2))
else:
    print("\nNo se encontró el socio para actualizar")

# Eliminar socio
if club.eliminar_socio(1):
    print("\nSocio eliminado")
else:
    print("\nNo se encontró el socio para eliminar")

# Mostrar socios actualizados
print("\nLista de socios actualizada:")
club.mostrar_socios()