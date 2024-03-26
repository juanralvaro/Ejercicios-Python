""" Escribe un programa en Python que solicite al usuario ingresar el precio de un producto y su descuento. El programa debe calcular el precio final después del descuento y mostrar el resultado. Utiliza un operador ternario para manejar el caso en el que el descuento sea mayor que el precio del producto, en cuyo caso se mostrará un mensaje indicando que el descuento no es válido.

1. Solicita al usuario que ingrese el precio del producto y su descuento en porcentaje.
2. Utiliza un operador ternario para calcular el precio final después del descuento.
3. Si el descuento es mayor que el precio del producto, muestra un mensaje indicando que el descuento no es válido.
4. Si el descuento es válido, muestra el precio final después del descuento. """

# Solicitar al usuario que ingrese el precio del producto y su descuento
precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el descuento (%): "))

# Calcular el precio final después del descuento usando un operador ternario
precio_final = precio - (precio * descuento / 100) if descuento <= 100 else "Descuento inválido"

# Mostrar el resultado
print("El precio final después del descuento es:", precio_final)

""" #SOLUCIÓN JUSTO + NACHO

print("\n+++++ Calculadora de descuentos +++++\n")
precio = float(input("Introduzca el precio del producto: "))
descuento = float(input("Introduzca el porcentaje de descuento: "))
precio_final = precio - precio * descuento / 100; print("El precio final es: ", precio_final ) if descuento <= 100 else print("descuento no válido") """