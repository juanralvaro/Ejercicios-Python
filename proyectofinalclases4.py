from datetime import date

class Usuario:
    """
        1. Objetivo de la función: define los datos personales de un usuario.
        
        2. Parámetros:
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
    def __init__(self, id_usuario: str, nombre: str, apellido_uno: str, apellido_dos: str, edad: int, direccion: str, localidad: str, provincia: str, telefono: str, email: str) -> None:
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido_uno = apellido_uno
        self.apellido_dos = apellido_dos
        self.edad = edad
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia
        self.telefono = telefono
        self.email = email

class Socio(Usuario):
    socios = []
    def __init__(self, id_usuario: int, fondo_individual: int, avatar: str) -> None:
        """
        1: Objetivo de la función: definir las características de un socio.

        2. Parámetros:
        - id_usuario (int): Identificador único del socio.
        - fondo_individual (int): Fondo individual del socio.
        - avatar (str): Avatar del socio.
        Métodos:
        - Se heredan algunos métodos de la clase Usuario.
        
        3. Retorna: nada.
        """
        super().__init__(id_usuario)
        self.fondo_individual = fondo_individual
        self.avatar = avatar
        self.conexion_app = None
    
    def conectar_app(self, conexion_app: bool) -> None:
        """
        1. Objetivo: Conectar con la app de TechCashClub.

        2. Argumentos:
        - conexion_app (bool): conecta con la app de TechCashClub.
        
        3. Retorna: nada.
        """
        self.conexion_app = conexion_app

    def realizar_puja(self, producto: str, cantidad: int) -> bool:
        """
        1. Objetivo: Método para que el usuario realice una puja por un producto.

        Parámetros:
        - producto (Producto): Producto por el que se desea pujar.
        - cantidad (int): Cantidad de productos a pujar.
        
        Returns:
        - True si la puja fue realizada con éxito, False en caso contrario.
        """
        if Socio.id_usuario == True:
            cantidad_a_pujar = int(input("Introduzca la cantidad a pujar: "))
    
    def realizar_compra(self, producto: 'Producto', cantidad: int) -> bool:
        """
        Método para que el usuario realice una compra de un producto.

        Args:
        - producto (Producto): Producto que se desea comprar.
        - cantidad (int): Cantidad de productos a comprar.
        
        Returns:
        - True si la compra fue realizada con éxito, False en caso contrario.
        """
        for producto in Producto.productos:
            if producto.stock >= cantidad:
                producto.stock -= cantidad
                producto.vender_stock(cantidad)
                return "Se han vendido  "+ str(cantidad) + " unidades de " + producto.nombre + "."
            else:
                return "No hay stock suficiente"

class Administrador(Usuario):
    administradores = []
    def __init__(self, id_usuario: int) -> None:
        """
        1: Objetivo de la función: definir las características de un administrador y abrir una lista de socios.

        2. Parámetros:
        - id_usuario (int): Identificador único del administrador.
        
        Métodos:
        - Se heredan algunos métodos de la clase Usuario.
        
        3. Retorna: nada.
        """
        super().__init__(id_usuario)

    def alta_socio(self, socio: Socio) -> None:
        """
        1: Objetivo de la función: Método para dar de alta un socio en el club.

        2. Parámetros:
        - socio (Socio): Socio al que se va a dar de alta.
        Métodos:
        - Añade al socio a la lista de socios.
        
        3. Retorna: nada.
        """
        self.socios.append(socio)

    def baja_socio(self, socio: Socio) -> None:
        """
        1: Objetivo de la función: Método para dar de baja un socio en el club.

        2. Parámetros:
        - socio (Socio): Socio al que se va a dar de baja.
        Métodos:
        - Elimina al socio de la lista de socios.
        
        3. Retorna: nada.
        """
        self.socios.remove(socio)

    def seleccion_producto(self, producto: 'Producto') -> str:
        """
        1. Objetivo: que el administrador seleccione un producto para ofrecer en el club.

        2. Parámetros:
        - producto (Producto): Producto que se va a seleccionar.
        Métodos:
        - Busca el producto en la lista de productos.
        """
        for producto in Producto.productos:
            if producto.nombre == producto:
                return "Está el producto seleccionado."
        return "El producto que buscaba no está en la lista."

class Producto:
    productos = []
    def __init__(self, id_producto: int, nombre: str, precio: float, caracteristicas: str, imagenes: str, stock: int) -> None:
        """
        1: Objetivo de la función: definir las características de un producto.

        2. Parámetros:
        - id_producto (int): Identificador único del producto.
        - nombre (str): Nombre del producto.
        - precio (int): Precio del producto.
        - características (str): Características del producto.
        - imagenes (str): Imágenes del producto.
        - stock (int): stock del producto.
        
        3. Retorna: nada.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.caracteristicas = caracteristicas
        self.imagenes = imagenes
        self.stock = stock

class VentanaTemporal:
    def __init__(self, id_ventana_temporal: int, fecha_inicio: date, fecha_fin: date) -> None:
        """
        1: Objetivo de la función: abrir una ventana temporal.

        2. Parámetros:
        - id_ventana_temporal (int): Identificador único del producto.
        - fecha_inicio (date): Inicio de la ventana temporal.
        - fecha_fin (date): Final de la ventana temporal.
        
        3. Retorna: nada.
        """
        self.id_ventana_temporal = id_ventana_temporal
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Transaccion:
    def __init__(self, id_transaccion: int, metodo_pago: int, descuento_oferta: float, confirmacion_aceptada: bool, fecha_entrega: date) -> None:
        """
        1: Objetivo: detalla una transacción.

        2. Parámetros
        - id_transaccion (int) : Identificador único de la transacción.
        - metodo_pago (int): Método de pago utilizado en la transacción.
        - descuento_oferta (float): Descuento u oferta aplicada a la transacción.
        - confirmacion_aceptada (bool): Confirmación de si la transacción fue aceptada o no.
        - fecha_entrega (date): Fecha de entrega de la transacción.
        
        3. Retorna: nada.
        """
        self.id_transaccion = id_transaccion
        self.metodo_pago = metodo_pago
        self.descuento_oferta = descuento_oferta
        self.confirmacion_aceptada = confirmacion_aceptada
        self.fecha_entrega = fecha_entrega

class Puja:
    def __init__(self, fecha_inicio: date, fecha_fin: date) -> None:
        """
        1: Objetivo: detalla una puja.

        2. Parámetros:
        - fecha_inicio (date): Fecha de inicio de la puja.
        - fecha_fin (date): Fecha de finalización de la puja.
        
        3. Retorna: nada.
        """
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Fabricante:
    def __init__(self, empresa: str, direccion: str, producto: Producto, oferta_especial: float) -> None:
        """
        1: Objetivo de la función: definir las características de un fabricante.

        2. Parámetros:
        - empresa (str): Nombre del fabricante.
        - direccion_empresa (str): Dirección de la empresa.
        - producto (Producto): Producto fabricado.
        - oferta_especial (float): Descuento por oferta especial
        - stock (int): stock del producto.
        
        3. Retorna: nada.
        """
        self.empresa = empresa
        self.direccion = direccion
        self.producto = producto
        self.oferta_especial = oferta_especial

class Contabilidad:
    def __init__(self, fondo_individual: int, fondo_comun: int, comision: float) -> None:
        """
        1: Objetivo de la función: almacena la contabilidad de una empresa.

        2. Parámetros:
        - fondo_individual (int): Fondo a aportar por los socios.
        - fondo_comun (int): Fondo acumulado
        - comision (float): Porcentaje de comisión.
        
        3. Retorna: nada.
        """
        self.fondo_individual = fondo_individual
        self.fondo_comun = fondo_comun
        self.comision = comision