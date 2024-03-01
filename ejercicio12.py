""" - 12- Calculadora de propinas (WeekEnd)
    
    Desarrolla un programa en Python que permita calcular la propina a dejar en un restaurante. El ejercicio se centrará en practicar operaciones aritméticas básicas, la entrada de datos desde el teclado, la conversión de datos mediante casting, y la presentación de resultados utilizando f-strings.
    
    1. **Inicio del programa:**
        - Inicia el programa con un mensaje de bienvenida.
    2. **Entrada de datos:**
        - Solicita al usuario que ingrese el monto total de la factura del restaurante como un número decimal.
    3. **Entrada de porcentaje de propina:**
        - Pide al usuario que ingrese el porcentaje de propina que desea dejar.
    4. **Cálculo de la propina:**
        - Calcula la propina a partir del monto total y el porcentaje ingresado. Utiliza la fórmula: **`Propina = Monto Total * (Porcentaje de Propina / 100)`**
    5. **Mostrar resultados:**
        - Muestra el monto total de la factura, el porcentaje de propina y el monto total a pagar incluyendo la propina.
        - Utiliza f-strings para formatear los resultados y mostrar montos con dos decimales. """

print("Bienvenido al restaurante La Casilla.")
monto_total = float(input("Por favor, introduzca el monto total: "))
porcentaje_de_propina = int(input("Por favor, introduzca el porcentaje de propina a dar: "))
propina = monto_total * (porcentaje_de_propina / 100)
monto_total_final = monto_total + propina
print(f"\nMonto total: {monto_total:.0f}" + " €.")
print(f"\nPorcentaje de propina: {porcentaje_de_propina}"+ "%.")
print(f"\nMonto total final: {monto_total_final:.2f}" + " €.")
print(f"\n¡Gracias por venir! ¡Le esperamos!")