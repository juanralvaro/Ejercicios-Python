""" Crea un programa en Python que simule la actualización de la puntuación de un juego. Inicializa una variable llamada **`puntuacion`** con un valor inicial de 100. Luego, utiliza **operadores de asignación** para realizar las siguientes acciones:

1. Incrementa la puntuación en 10 unidades: Ha adquirido una vida extra
2. Reduce la puntuación en 5 unidades: Ha sido alcanzado por un enemigo
3. Multiplica la puntuación por 2: Ha recibido un bonus extra
4. Divide la puntuación por 4: Ha repartido el botín entre el equipo
5. Calcula el módulo de la puntuación entre 3: Ha perdido la parte del botín no repartida de forma equitativa entre los miembros del equipo.

Muestra la puntuación después de cada operación utilizando la función **`print()`**.

*Ejemplo de salida:*

*Puntuación Inicial: 100
Puntuación después de incrementar: 110
Puntuación después de reducir: 105
Puntuación después de multiplicar por 2: 210
Puntuación después de dividir por 4: 52.5
Puntuación después de calcular el módulo: 1.5* """

puntuacion = 100
print(f"Comienzas el juego con: {puntuacion} puntos.")
puntuacion += 10
print(f"\n¡Felicidades! Tienes una vida extra y pasas a tener {puntuacion} puntos.")
puntuacion -= 5
print(f"\n¡Oh, no! Te ha alcanzado un enemigo y te quedas con {puntuacion} puntos.")
puntuacion *= 2
print(f"\n¡Magnífico! Tienes un bonus extra y pasas a tener {puntuacion} puntos.")
puntuacion /= 4
print(f"\nEres generoso. Has repartido el botín con tus compañeros, conformándote con {puntuacion} puntos.")
puntuacion %= 3
print(f"\n¡Vaya! Te has quedado sin {puntuacion} puntos tras no poder ser repartible con tus compañeros.")

dinero = 100
print(f"Tienes {dinero} euros.")
dinero += 10
print(f"\nTienes {dinero} euros.")
dinero -= 5
print(f"\nTe quedan {dinero} euros.")
dinero *= 2
print(f"\nPasas a tener {dinero} euros.")
dinero /= 4
print(f"\nHas repartido tus {dinero} euros a tus amigos.")
dinero %= 3
print(f"\nLo único que no pudiste repartir fueron {dinero} euros.")