""" - 14 - Ejercicio evalúa las condiciones
    
    Crea un programa en Python que simule la evaluación de condiciones utilizando **operadores lógicos + operadores de comparación**. Utiliza variables para representar las siguientes situaciones:
    
    1. Un estudiante ha aprobado si su puntuación es mayor o igual a 60.
    2. Un usuario tiene acceso si es un administrador o tiene una suscripción premium.
    3. Un número es positivo si es mayor que 0 y menor que 100.
    4. Un equipo gana si ha anotado más de 3 goles y no ha recibido ningún gol en contra.
    
    Utiliza operadores lógicos (**`and`**, **`or`**, **`not`**) para evaluar estas condiciones y muestra el resultado de cada situación utilizando la función **`print()`**.
    
    *Ejemplo de salida:*
    
    *Puntuación del estudiante: 75
    El estudiante ha aprobado: True*
    
    *Usuario es administrador: True
    Usuario tiene suscripción premium: False
    El usuario tiene acceso: True*
    
    *Número a evaluar: 45
    El número es positivo: True*
    
    *Goles a favor: 4
    Goles en contra: 0
    El equipo ha ganado: True* """

1.
nota_estudiante = int(input("Introduzca su nota: "))
aprobado_estudiante = nota_estudiante >= 60
print(f"\nEl estudiante ha aprobado: {aprobado_estudiante}.\n")

2.
acceso_usuario = str(input("¿Es usuario o administrador premium?: "))
accede = acceso_usuario == "usuario" or acceso_usuario == "administrador_premium"
print(f"\n¿Usted puede acceder?: {accede}.\n")

3.
numero = int(input("Introduzca un número: "))
numero_positivo = numero > 0 and numero < 100
print(f"\n¿El número es positivo?: {numero_positivo}.\n")

4.
goles_a_favor = int(input("Introduzca sus goles a favor: "))
goles_en_contra = int(input("Introduzca sus goles en contra: "))
victoria = goles_a_favor >= 3 and goles_en_contra == 0
print(f"\n¿Su equipo ha ganado el partido?: {victoria}.")

"""SOLUCIÓN

# Situación 1: Evaluación de aprobación del estudiante
puntuacion_estudiante = 75
aprobado = puntuacion_estudiante >= 60
print(f"Puntuación del estudiante: {puntuacion_estudiante}\nEl estudiante ha aprobado: {aprobado}\n")

# Situación 2: Evaluación de acceso del usuario
es_administrador = True
tiene_suscripcion_premium = False
acceso_usuario = es_administrador or tiene_suscripcion_premium
print(f"Usuario es administrador: {es_administrador}\nUsuario tiene suscripción premium: {tiene_suscripcion_premium}\nEl usuario tiene acceso: {acceso_usuario}\n")

# Situación 3: Evaluación de número positivo
numero_evaluar = 45
es_positivo = 0 < numero_evaluar < 100
print(f"Número a evaluar: {numero_evaluar}\nEl número es positivo: {es_positivo}\n")

# Situación 4: Evaluación de victoria del equipo
goles_a_favor = 4
goles_en_contra = 0
equipo_gana = goles_a_favor > 3 and goles_en_contra == 0
print(f"Goles a favor: {goles_a_favor}\nGoles en contra: {goles_en_contra}\nEl equipo ha ganado: {equipo_gana}\n") """