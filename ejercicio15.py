""" Calculadora de impuestos para autónomos
    
    Desarrolla un programa en Python que ayude a un autónomo a calcular los impuestos que deberá pagar en un trimestre. 
    
    1. **Inicio del Programa:**
        - Inicia el programa con un mensaje de bienvenida para el autónomo.
    2. **Entrada de Datos:**
        - Solicita al autónomo ingresar los siguientes datos:
            - Ingresos totales del trimestre como un número decimal.
            - Gastos deducibles del trimestre como un número decimal.
            - Otros gastos no deducibles del trimestre como un número decimal.
    3. **Cálculo de la Base Imponible:**
        - Calcula la base imponible restando los gastos deducibles y otros gastos no deducibles a los ingresos totales.
    4. **Cálculo del Impuesto a Pagar:**
        - Calcula el impuesto a pagar como el 10% de la base imponible.
    5. **Mostrar Resultados:**
        - Muestra los siguientes resultados:
            - Ingresos totales.
            - Gastos deducibles.
            - Otros gastos no deducibles.
            - Base imponible.
            - Impuesto a pagar.
    6. **Consideraciones Adicionales:**
        - Utiliza f-strings para formatear los resultados y mostrar montos con dos decimales.
        - No es necesario utilizar la estructura de control **`if`** en este ejercicio. """

print("Bienvenido a la computadora de impuestos para autónomos.")

ingresos_totales = float(input("\nIntroduzca sus ingresos totales en euros: "))
gastos_deducibles = float(input("\nIntroduzca sus gastos deducibles en euros: "))
otros_gastos_no_deducibles = float(input("\nIntroduzca otros gastos no deducibles en euros: "))

base_imponible = ingresos_totales - gastos_deducibles - otros_gastos_no_deducibles

impuesto_a_pagar = base_imponible / 10

print(f"\nSus ingresos totales son {ingresos_totales:.2f} €.")
print(f"\nSus gastos deducibles son {gastos_deducibles:.2f} €.")
print(f"\nSus gastos no deducibles son {otros_gastos_no_deducibles:.2f} €.")
print(f"\nSu base imponible es {base_imponible:.2f} €.")
print(f"\nSu impuesto a pagar es {impuesto_a_pagar:.2f} €.")

print(f"----------------------------------------------------")
print(f"|                                                  |")
print(f"|              CALCULADORA DE IMPUESTOS            |")
print(f"|                                                  |")
print(f"|              Autónomo: José Ruiz Díaz            |")
print(f"|                                                  |")
print(f"|                    {ingresos_totales:.2f}                       |")
print(f"|                                                  |")
print(f"|                    {gastos_deducibles:.2f}                        |")
print(f"|                                                  |")
print(f"|                    {otros_gastos_no_deducibles:.2f}                         |")
print(f"|                                                  |")
print(f"|                    {base_imponible:.2f}                       |")
print(f"|                                                  |")
print(f"|                    {impuesto_a_pagar:.2f}                        |")
print(f"|                                                  |")
print(f"----------------------------------------------------")

#Optimizado para ingresos totales de 4 cifras enteras, gastos deducibles de 3 cifras enteras, otros gastos no deducibles de 2 cifras enteras, base imponible de 4 cifras enteras e impuesto a pagar de 3 cifras enteras.