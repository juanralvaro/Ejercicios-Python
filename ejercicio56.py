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
        self.stock -= cantidad
        return self.precio * cantidad
    
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
                return producto.mostrar_informacion()
        return "No se encontró el producto"
    
    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.vender_stock(cantidad)
                    return producto.vender_stock(cantidad)
                else:
                    return "No hay stock suficiente"
                
producto_uno = Producto("Coca-Cola", 1, 200)
producto_dos = Producto("Kilo de carne", 6.95, 55)
producto_tres = Producto("Televisor", 200, 15)

tienda_uno = Tienda

num_productos = int(input("Ingrese el número de productos a agregar: "))
for _ in range(num_productos):
    producto = str(input("Ingrese un producto: "))
    tienda_uno.agregar_producto(producto)

producto_uno.mostrar_informacion()
producto_dos.mostrar_informacion()
producto_tres.mostrar_informacion()

tienda_uno.buscar_producto("Televisor")

tienda_uno.vender_producto("Kilo de carne", 4)
print(f"Coste del producto: {producto_tres.precio * 4}")