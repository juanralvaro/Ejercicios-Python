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
lista_accesorios = str(input("Introduce los accesorios que quieras llevar:\n"))
lista_ropa = str(input("Introduce las prendas de ropa que quieras llevar:\n"))
lista_tecnologia = str(input("Introduce los aparatos tecnológicos que quieras llevar:\n"))
lista_zapatos_y_zapatillas = str(input("Introduce los zapatos y zapatillas que quieras llevar:\n"))
print(f"¡Perfecto! Esto es lo que llevas." + "\n" + "\n" + "lista accesorios:".upper(), lista_accesorios.lower() + "\n" + "\n" + "lista ropa:".upper(), lista_ropa.lower() + "\n" + "\n" + "lista tecnologia:".upper(), lista_tecnologia.lower() + "\n" + "\n" + "lista zapatos & zapatillas:".upper(), lista_zapatos_y_zapatillas.lower() + "\n" + "\n" + "¡Gracias por confiar en nosotros!")

""" Solución:

print("Bienvenido a tu gestor de maletas para las vacaciones") #la función print( ) se utiliza para mostrar la salida de información

ropa = str(input("¿Qué ropa vas a llevar en tu maleta?\n"))
aseo = str(input("¿Qué útiles de aseo vas a llevar en tu maleta?\n"))
accesorios = str(input("¿Qué accesorios vas a llevar en tu maleta?\n"))
tecnologia = str(input("¿Qué dispositivos vas a llevar en tu maleta?\n"))
zapatos = str(input("¿Qué zapatos vas a llevar en tu maleta?\n")) #Es muy importante tener en todo momento el control sobre los tipos de datos

print("\nResumen de mis maletas:".upper())
print("Maleta de ropa:".upper(), ropa.lower()) 
print("\nMaleta de aseo:\n".upper(), aseo.lower()) 
print("\nMaleta de accesorio:\n".upper(), accesorios.lower()) 
print("\nMaleta de tecnologia:\n".upper(), tecnologia.lower()) 
print("\nMaleta de zapatos:\n".upper(), zapatos.lower()) 

print("\nSegundo método en una línea\n")

print("\nResumen de mis maletas:\n".upper(), "\nMaleta de ropa:\n".upper(), ropa.lower(), "\n\nMaleta de aseo:\n".upper(), aseo.lower(),"\n\nMaleta de accesorio:\n".upper(), accesorios.lower(), "\n\nMaleta de tecnologia:\n".upper(), tecnologia.lower(), "\n\nMaleta de zapatos:\n".upper(), zapatos.lower())

Cuando nosotros utilizamos la coma para separar las variables dentro de un print, Python automáticamente agrega un espacio entre las variables. Además con la coma, Python va a poder imprimir diferentes tipos de datos sin necesidad de realizar una CONVERSIÓN.   --> En el caso de trabajar con el operador suma no se manejarán automáticamente los espacios ni las conversiones de tipo. Lo utilizaremos cuando necesitemos un control más explícito de nuestras operaciones"""