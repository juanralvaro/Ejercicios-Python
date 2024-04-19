class Usuario:
    def __init__(self, id: str, nombre: str, apellido_uno: str, apellido_dos: str, edad: int, direccion: str, localidad: str, provincia: str, telefono: str, email: str) -> None:
        """
        1. Objetivo de la función: define los datos personales de un usuario.
        
        2. Parámetros:
        - self: permite acceder a los métodos y atributos de la propia clase.
        - id (str): es la id del usuario.
        - nombre (str): es el nombre o nombres del usuario.
        - apellido_uno (str): es el primer apellido del usuario.
        - apellido_dos (str): es el segundo apellido del usuario.
        - edad (int): es la edad del usuario.
        - direccion (str): es la dirección donde vive el usuario.
        - localidad (str): es la localidad donde vive el usuario.
        - provincia (str): es la provincia donde vive el usuario.
        - telefono (str): es el teléfono del usuario.
        - email (str): es el correo electrónico del usuario.
        
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

    
    def realizar_puja(self, producto, cantidad):
        """
        Método para que el usuario realice una puja por un producto.

        Args:
        - producto: Producto por el que se desea pujar.
        - cantidad: Cantidad de productos a pujar.
        """
        pass
    
    def realizar_compra(self, producto, cantidad):
        """
        Método para que el usuario realice una compra de un producto.

        Args:
        - producto: Producto que se desea comprar.
        - cantidad: Cantidad de productos a comprar.
        """
        pass
    
    def alta_socio(self, socio):
        """
        Método para que el administrador dé de alta un socio.

        Args:
        - socio: Socio que se va a dar de alta.
        """
        pass
    
    def baja_socio(self, socio):
        """
        Método para que el administrador dé de baja un socio.

        Args:
        - socio: Socio que se va a dar de baja.
        """
        pass
    
    def seleccion_producto(self, producto):
        """
        Método para que el administrador seleccione un producto.

        Args:
        - producto: Producto que se va a seleccionar.
        """
        pass

class Socio(Usuario):
    def __init__(self, identificador, fondo_individual, avatar):
        """
        Constructor de la clase Socio.

        Args:
        - identificador: Identificador único del socio.
        - fondo_individual: Fondo individual del socio.
        - avatar: Avatar del socio.
        """
        super().__init__(identificador)
        self.fondo_individual = fondo_individual
        self.avatar = avatar
        self.conexion_app = None
    
    def conectar_app(self, app):
        """
        Método para que el socio se conecte a la aplicación.

        Args:
        - app: Aplicación a la que se va a conectar el socio.
        """
        self.conexion_app = app

class Administrador(Usuario):
    def __init__(self, identificador):
        """
        Constructor de la clase Administrador.

        Args:
        - identificador: Identificador único del administrador.
        """
        super().__init__(identificador)


class Producto:
    def __init__(self, identificador, nombre, precio, caracteristicas, imagenes, stock):
        """
        Constructor de la clase Producto.

        Args:
        - identificador: Identificador único del producto.
        - nombre: Nombre del producto.
        - precio: Precio del producto.
        - caracteristicas: Características técnicas del producto.
        - imagenes: Lista de imágenes del producto.
        - stock: Cantidad disponible en stock del producto.
        """
        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio
        self.caracteristicas = caracteristicas
        self.imagenes = imagenes
        self.stock = stock

class VentanaTemporal:
    def __init__(self, identificador, fecha_inicio, fecha_fin):
        """
        Constructor de la clase VentanaTemporal.

        Args:
        - identificador: Identificador único de la ventana temporal.
        - fecha_inicio: Fecha de inicio de la ventana temporal.
        - fecha_fin: Fecha de fin de la ventana temporal.
        """
        self.identificador = identificador
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Transaccion:
    def __init__(self, identificador, pago, descuento_oferta, confirmacion_aceptado, fecha_entrega):
        """
        Constructor de la clase Transaccion.

        Args:
        - identificador: Identificador único de la transacción.
        - pago: Método de pago utilizado en la transacción.
        - descuento_oferta: Descuento u oferta aplicada a la transacción.
        - confirmacion_aceptado: Confirmación de si la transacción fue aceptada o no.
        - fecha_entrega: Fecha de entrega de la transacción.
        """
        self.identificador = identificador
        self.pago = pago
        self.descuento_oferta = descuento_oferta
        self.confirmacion_aceptado = confirmacion_aceptado
        self.fecha_entrega = fecha_entrega

class Puja:
    def __init__(self, fecha_inicio, fecha_fin):
        """
        Constructor de la clase Puja.

        Args:
        - fecha_inicio: Fecha de inicio de la puja.
        - fecha_fin: Fecha de finalización de la puja.
        """
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Administrador(Usuario):
    def __init__(self, identificador):
        """
        Constructor de la clase Administrador.

        Args:
        - identificador: Identificador único del administrador.
        """
        super().__init__(identificador)
    
    def alta_socio(self, socio):
        """
        Método para dar de alta un socio en el club.

        Args:
        - socio: Socio que se va a dar de alta.
        """
        self.socios.append(socio)
    
    def baja_socio(self, socio):
        """
        Método para dar de baja un socio en el club.

        Args:
        - socio: Socio que se va a dar de baja.
        """
        self.socios.remove(socio)
    
    def seleccion_producto(self, producto):
        """
        Método para que el administrador seleccione un producto para ofrecer en el club.

        Args:
        - producto: Producto que se va a seleccionar.
        """
        pass

class Fabricante:
    def __init__(self, empresa, direccion, producto, oferta_especial):
        """
        Constructor de la clase Fabricante.

        Args:
        - empresa: Nombre de la empresa del fabricante.
        - direccion: Dirección del fabricante.
        - producto: Producto fabricado por el fabricante.
        - oferta_especial: Oferta especial proporcionada por el fabricante.
        """
        self.empresa = empresa
        self.direccion = direccion
        self.producto = producto
        self.oferta_especial = oferta_especial

class Contabilidad:
    def __init__(self, fondo_individual, fondo_comun, comision):
        """
        Constructor de la clase Contabilidad.

        Args:
        - fondo_individual: Fondo individual del club de socios.
        - fondo_comun: Fondo común del club de socios.
        - comision: Comisión aplicada a las transacciones.
        """
        self.fondo_individual = fondo_individual
        self.fondo_comun = fondo_comun
        self.comision = comision
