""" 1. Crea una clase llamada **`Producto`** con los siguientes atributos:
    - **`nombre`**: El nombre del producto.
    - **`precio`**: El precio del producto.
    - **`stock`**: La cantidad de unidades disponibles en el stock del producto.
2. La clase **`Producto`** debe tener los siguientes métodos:
    - **`__init__(self, nombre, precio, stock)`**: Método constructor que inicializa los atributos **`nombre`**, **`precio`** y **`stock`**.
    - **`mostrar_informacion(self)`**: Método que imprime la información del producto, mostrando su nombre, precio y stock.
    - **`agregar_stock(self, cantidad)`**: Método que permite aumentar el stock del producto en la cantidad especificada.
    - **`vender(self, cantidad)`**: Método que permite vender una cantidad específica del producto. Actualiza el stock y devuelve el monto total de la venta.
3. Desarrolla una clase llamada **`Tienda`** con los siguientes atributos:
    - **`productos`**: Una lista que almacena los productos disponibles en la tienda.
4. La clase **`Tienda`** debe tener los siguientes métodos:
    - **`__init__(self)`**: Método constructor que inicializa el atributo **`productos`** como una lista vacía.
    - **`agregar_producto(self, producto)`**: Método que permite agregar un producto a la lista de productos disponibles en la tienda.
    - **`mostrar_productos(self)`**: Método que muestra la información de todos los productos disponibles en la tienda.
    - **`buscar_producto(self, nombre)`**: Método que busca un producto por su nombre y devuelve su información.
    - **`vender_producto(self, nombre, cantidad)`**: Método que permite vender una cantidad específica de un producto. Actualiza el stock del producto y devuelve el monto total de la venta.
5. Desarrolla un programa principal que permita al usuario:
    - Crear instancias de la clase **`Producto`**.
    - Agregar productos a la tienda.
    - Mostrar la información de todos los productos disponibles en la tienda.
    - Buscar un producto por su nombre y mostrar su información.
    - Vender una cantidad específica de un producto y mostrar el monto total de la venta. """

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def mostrar_informacion(self):
        return f"Información del producto: {self.nombre}, {self.precio} €, {self.stock} artículos disponibles"
    
    def agregar_stock(self, cantidad):
        self.stock += cantidad
        
    def vender_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return self.precio * cantidad
        else:
            return "No hay stock suficiente"
    
class Tienda:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.mostrar_informacion())
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return "No se encontró el producto"
    
    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    cantidad_vendida = producto.vender_stock(cantidad)
                    monto = cantidad_vendida * precio
                    return monto
                else:
                    return "No hay stock suficiente"

#Creación de la tienda
tienda = Tienda()

#Menú de opciones
print("Bienvenido a la tienda.")
print("Seleccione una opción:")
print("1. Introducir un producto y agregarlo a la tienda")
print("2. Mostrar productos disponibles")
print("3. Buscar un producto y mostrar su información")
print("4. Vender un producto y mostrar el monto de la venta")
print("5. Salir")

while True:
    opcion = input("Ingrese el número de la opción seleccionada: ")
    if opcion == '1':
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        stock = input("Ingrese el stock del producto: ")
        nuevo_producto = Producto(nombre, precio, stock)
        tienda.agregar_producto(nuevo_producto)
    elif opcion == '2':
        tienda.mostrar_productos()
    elif opcion == '3':
        producto_buscado = str(input("Ingrese el producto a buscar: "))
        producto_encontrado = tienda.buscar_producto(producto_buscado)
        if producto_encontrado:
            producto_encontrado.mostrar_informacion(f"{producto.nombre}, {producto.precio}, {producto.stock}")
        else:
            print("El producto no existe")
    elif opcion == '4':
        print("Venta de producto:")
        producto = str(input("Ingrese el nombre del producto que desea comprar: "))
        producto.stock = int(input("Ingrese el stock del producto que desea comprar: "))
        tienda.vender_producto(Producto)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")