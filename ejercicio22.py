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

#1. Crea una lista llamada categorias_gastos que contenga las siguientes categorías: "Alimentación", "Transporte", "Entretenimiento", "Servicios" y "Otros".
categorias_gastos = ["Alimentación", "Transporte", "Entretenimiento", "Servicios", "Otros"]

#Inicializamos un diccionario vacio que vamos a usar para almacenar los gastos en cada categoria
gasto_categoria = {}

#ejemplo_diccionario = {"nombre": "María", "edad": 34}

#Creamos un bucle for para ingresar los gastos en cada categoria
for categoria in categorias_gastos:
  gasto = float(input(f"Ingrese el importe de gasto para {categoria}: "))
  gasto_categoria[categoria] = gasto #En el diccionario gasto_categoria, vamos a almacenar los datos que el usuario añada a la variable gasto, con la categoria como clave
#gasto_categoria = {"Alimentación": gasto, "Transporte": gasto..... }

#4. Muestra un resumen de gastos mensuales por categoría.
print("\nResumen de Gastos Mensuales:")
for categoria, gasto in gasto_categoria.items():
    print(f"{categoria}: {gasto}€") #items se usa para llamar a la clave y valor del diccionario

#5. Finalmente, muestra el total de gastos mensuales.
total_gastos = sum(gasto_categoria.values())
print(f"\nTotal de Gastos Mensuales: {total_gastos:.2f}€") #values sirve para llamar sólo al valor del diccionario; para llamar sólo a la clave habría que usar key