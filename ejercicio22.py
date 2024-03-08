""" Vamos a crear un programa en Python que te permita llevar un registro de tus gastos mensuales en diferentes categorías. Utilizaremos un bucle **`for`** para iterar a través de las categorías de gastos y solicitar al usuario que ingrese los importe correspondientes. Al final, el programa calculará y mostrará el total de gastos.

1. Crea una lista llamada **`categorias_gastos`** que contenga las siguientes categorías: "Alimentación", "Transporte", "Entretenimiento", "Servicios" y "Otros".
2. Inicializa una variable llamada **`total_gastos`** en 0 para acumular el total de gastos.
3. Utiliza un bucle **`for`** para iterar a través de las categorías de gastos. Dentro del bucle:
    - Solicita al usuario que ingrese el importe de gasto para cada categoría.
    - Convierte la entrada del usuario a tipo float.
    - Acumula el importe al total de gastos.
4. Muestra un resumen de gastos mensuales por categoría utilizando otro bucle **`for`**.
5. Finalmente, muestra el total de gastos mensuales.

*Ejemplo de salida:*

*Ingrese el importe de gasto para Alimentación: 150.50 pesetas
Ingrese el importe de gasto para Transporte: 60.25 pesetas
Ingrese el importe de gasto para Entretenimiento: 30.00 pesetas
Ingrese el importe de gasto para Servicios: 120.75 pesetas
Ingrese el importe de gasto para Otros: 40.50 pesetas*

*Resumen de Gastos Mensuales:
Alimentación: 150.50 pesetas
Transporte: 60.25 pesetas
Entretenimiento: 30.00 pesetas
Servicios: 120.75 pesetas
Otros: 40.50 pesetas*

*Total de Gastos Mensuales: 402.00 pesetas* """



print("Bienvenido al programa de registro de tus gastos mensuales.")

categorias_gastos = ["Alimentación", "Transporte", "Entretenimiento", "Servicios", "Otros"]

total_gastos = 0

for alimentacion in categorias_gastos:
    alimentacion = float(input(f"\nIngrese el importe de gasto para {categorias_gastos[0]}: "))
    total_gastos += alimentacion
    transporte = float(input(f"\nIngrese el importe de gasto para {categorias_gastos[1]}: "))
    total_gastos += transporte
    entretenimiento = float(input(f"\nIngrese el importe de gasto para {categorias_gastos[2]}: "))
    total_gastos += entretenimiento
    servicios = float(input(f"\nIngrese el importe de gasto para {categorias_gastos[3]}: "))
    total_gastos += servicios
    otros = float(input(f"\nIngrese el importe de gasto para {categorias_gastos[4]}: "))
    total_gastos += otros
    
print("\nÉste es el resumen de gastos mensuales:")

for total_gastos in categorias_gastos:
    print(f"\nAlimentación: {alimentacion} €.")
    print(f"\nTransporte: {transporte} €.")
    print(f"\nEntretenimiento: {entretenimiento} €.")
    print(f"\nServicios: {servicios} €.")
    print(f"\nOtros: {otros} €.")

print(f"\nEl total de los gastos mensuales es: {total_gastos}.") 

""" print("Bienvenido al programa de registro de tus gastos mensuales.")

categorias_gastos = ["Alimentación", "Transporte", "Entretenimiento", "Servicios", "Otros"]
gastos = [0] * len(categorias_gastos)

total_gastos = 0

for i in range(len(categorias_gastos)):
    gastos[i] = float(input(f"Ingrese el importe de gasto para {categorias_gastos[i]}: "))
    total_gastos += gastos[i]

print("\nÉste es el resumen de gastos mensuales:")
for i in range(len(categorias_gastos)):
    print(f"\n{categorias_gastos[i]}: {gastos[i]} €.")

print(f"\nEl total de los gastos mensuales es: {total_gastos} €.") """