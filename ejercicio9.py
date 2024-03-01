""" - 9- Ejercicio Calculadora de descuento (WeekEnd)
Desarrolla un programa en Python que permita calcular el precio final de un producto después de aplicar un descuento.
    1. **Inicio del programa:**
        - Inicia el programa con un mensaje de bienvenida.
    2. **Entrada de datos:**
        - Solicita al usuario ingresar el precio original del producto como un número decimal.
    3. **Entrada de descuento:**
        - Pide al usuario que ingrese el porcentaje de descuento que desea aplicar al producto.
    4. **Cálculo del precio con descuento:**
        - Calcula el precio final después de aplicar el descuento. Utiliza la fórmula: **`Precio Final = Precio Original - (Precio Original * Porcentaje de Descuento / 100)`**
    5. **Mostrar resultados:**
        - Muestra el precio original, el porcentaje de descuento y el precio final después de aplicar el descuento.
        - Utiliza f-strings para formatear los resultados y mostrar el precio final con dos decimales. """

print("Bienvenido a El Corte Escocés.")
precio_original = float(input("\nPor favor, ingrese el precio original del producto: "))
porcentaje_de_descuento = int(input("\nPor favor, ingrese el porcentaje de descuento del producto: "))
precio_final = precio_original - (precio_original * porcentaje_de_descuento / 100)
print(f"\nPrecio original: {precio_original:.0f}" + " €")
print(f"\nPorcentaje de descuento: {porcentaje_de_descuento}%")
print(f"\nPrecio final: {precio_final:.2f}" + " €")
print(f"\n¡Gracias por su visita!")