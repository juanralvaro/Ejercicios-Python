""" 1. Crea una tupla llamada **`compras_enero`** que contenga los precios de productos comprados durante el mes de enero.
2. Implementa la funcionalidad para calcular el total gastado en compras durante un mes.
3. Implementa la funcionalidad para encontrar el precio del producto más caro en una lista de precios.
4. Crea una tupla llamada **`compras_febrero`** con precios de productos comprados en febrero.
5. Utiliza el método **`count`** para contar cuántas veces se compró un producto específico en febrero.
6. Utiliza la función **`max`** para encontrar el precio más alto entre las dos tuplas.
7. Utiliza la función **`sum`** para calcular el gasto total en ambos meses.
8. Utiliza la función **`sorted`** para obtener una tupla ordenada de precios en ambos meses.
9. Imprime los resultados de las operaciones anteriores y verifica que las funcionalidades y métodos están trabajando correctamente. """

#Bienvenida
print("Bienvenido al recopilador de precios de sus productos de enero.")

#1. Crear tupla con las compras de enero
compras_enero = (12.95, 3, 6.95, 12, 25.93, 13, 16.23)

#2. Saber lo gastado durante todo el mes
lista_compras_enero = list(compras_enero)
gasto_mes_enero = sum(lista_compras_enero)

#3. Saber la compra más cara del mes
lista_ordenada = sorted(lista_compras_enero) #Se ordena para que la última sea la más cara, y esa última se muestra en el print.

#4. Crear tupla con las compras de febrero
compras_febrero = (10, 12, 6.23, 12.95, 23.23, 12, 41)

#5. Contar las veces que se compró cierto producto en febrero
producto_buscado = compras_febrero.count(12)

#6. Encontrar el precio más alto entre los dos meses
compras_enero_febrero = compras_enero + compras_febrero
precio_mas_alto = max(compras_enero_febrero)

#7. Encontrar el total comprado entre ambos meses.
total_comprado = sum(compras_enero_febrero)

#8. Tupla ordenada de precios en ambos meses.
precios_ordenados_enero = tuple(sorted(compras_enero))
precios_ordenados_febrero = tuple(sorted(compras_febrero))

#9. Imprimir resultados
print("Compras de enero:",compras_enero)
print(f"El gasto en enero fue {gasto_mes_enero} €.")
print(f"La compra más cara en enero fue: {lista_ordenada[5]} €.")
print("Compras de febrero:",compras_febrero)
print(f"En enero se ha comprado el producto de 12 € {producto_buscado} veces.")
print(f"El producto comprado con el precio más alto entre enero y febrero costó {precio_mas_alto} €.")
print(f"El total de dinero gastado en compras entre enero y febrero fue {total_comprado} €.")
print("Precios de enero ordenados:",precios_ordenados_enero)
print("Precios de febrero ordenados:",precios_ordenados_febrero)

#Despedida
print("Gracias por usar el recopilador de precios. ¡Hasta la próxima!")