# Ejercicio: Planificación de maletas para vacaciones

""" Instrucciones:

Ayuda al usuario a planificar sus maletas para las vacaciones.
Pídele que introduzca la información de los objetos que deben
incluirse en diferentes maletas. Al final, muestra toda la información
de manera ordenada.
 1. Pide al usuario que introduzca la información para cada maleta:
		- accesorios
		- ropa
		- tecnología
		- zapatos & zapatillas.

2. Cuando el usuario terminado de introducir la información, le va a devolver
los resultados en 4 listas diferentes, con toda la información en minúsculas,
y el título de cada lista en mayúsculas:
		· LISTA ACCESORIOS
		· LISTA ROPA
		· LISTA TECNOLOGÍA
		· LISTA ZAPATOS & ZAPATILLAS"""

print("Bienvenido al planificador de vacaciones HappyDays.")
lista_accesorios = input("\nIntroduce los accesorios que quieras llevar:\n")
lista_ropa = input("\nIntroduce las prendas de ropa que quieras llevar:\n")
lista_tecnologia = input("\nIntroduce los aparatos tecnológicos que quieras llevar:\n")
lista_zapatos_y_zapatillas = input("\nIntroduce los zapatos y zapatillas que quieras llevar:\n")
print(f"¡Perfecto! Esto es lo que llevas." + "\n" + "\n" + "lista accesorios:".upper(), lista_accesorios.lower() + "\n" + "\n" + "lista ropa:".upper(), lista_ropa.lower() + "\n" + "\n" + "lista tecnologia:".upper(), lista_tecnologia.lower() + "\n" + "\n" + "lista zapatos & zapatillas:".upper(), lista_zapatos_y_zapatillas.lower() + "\n" + "¡Gracias por confiar en nosotros!")

""" # Ejercicio de Planificación de Maletas para Vacaciones

# Solicitar al usuario que introduzca la información de las maletas
maleta_ropa = input("Introduce los objetos para la maleta de ropa: ")
maleta_accesorios = input("Introduce los objetos para la maleta de accesorios: ")
maleta_calzado = input("Introduce los objetos para la maleta de calzado: ")
maleta_tecnologia = input("Introduce los objetos para la maleta de tecnología: ")
maleta_aseo = input("Introduce los objetos para la maleta de aseo: ")

# Imprimir un mensaje de confirmación
print("\n¡Maletas planificadas con éxito!")

# Mostrar al usuario la información ordenada y en minúsculas
print("\nResumen de Maletas:".upper())
print(f"Maleta de ropa:".upper(), maleta_ropa.lower())
print(f"MALETA DE ACCESORIOS: {maleta_accesorios.lower()}")
print(f"MALETA DE CALZADO: {maleta_calzado.lower()}")
print(f"MALETA DE TECNOLOGÍA: {maleta_tecnologia.lower()}")
print(f"MALETA DE ASEO: {maleta_aseo.lower()}") """