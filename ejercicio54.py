""" Crea un programa en Python que permita al usuario registrar la asistencia y calificaciones de un estudiante. Trabaja con métodos de instancia para resolver este ejercicio. 

1. Crea una clase llamada **`Estudiante`** con los siguientes atributos:
    - **`nombre`**: El nombre del estudiante.
    - **`asistencia`**: Un contador que registra la cantidad de días de asistencia.
    - **`calificaciones`**: Una lista que almacena las calificaciones del estudiante.
2. La clase **`Estudiante`** debe tener los siguientes métodos de instancia:
    - **`__init__(self, nombre)`**: Método constructor que inicializa el nombre del estudiante, la asistencia en cero y una lista vacía de calificaciones.
    - **`registrar_asistencia(self)`**: Método que incrementa el contador de asistencia en uno.
    - **`agregar_calificacion(self, calificacion)`**: Método que agrega una calificación a la lista de calificaciones del estudiante.
    - **`promedio_calificaciones(self)`**: Método que calcula y devuelve el promedio de las calificaciones del estudiante.
3. Solicita al usuario los siguientes datos del estudiante:
    - Nombre del estudiante.
    - Cantidad de días de asistencia.
    - Calificaciones del estudiante.
4. Utiliza la clase **`Estudiante`** para crear una instancia con los datos proporcionados por el usuario y realiza las siguientes acciones:
    - Registra la asistencia del estudiante.
    - Agrega las calificaciones del estudiante.
    - Calcula el promedio de calificaciones del estudiante.
5. Muestra los resultados por pantalla, incluyendo el nombre del estudiante, la cantidad de días de asistencia, y el promedio de calificaciones. """

class Estudiante:
    def __init__(self, nombre:str): #Estudiante parte sólo con un parámetro de salida, asistencia y calificaciones se inician vacíos 
        self.nombre = nombre
        self.asistencia = 0
        self.calificaciones = []
        
    def registrar_asistencia(self):  # cada día de asistencia suma uno a la cuenta
        self.asistencia += 1
            
    def agregar_calificacion(self, calificacion): #se añade una calificación a la lista de calificaciones
        self.calificaciones.append(calificacion)
            
    def promedio_calificaciones(self): #se suman las calificaciones y se divide la nota total por el número de calificaciones dadas
        total_calificaciones = sum(self.calificaciones)
        numero_calificaciones = len(self.calificaciones)
        promedio = total_calificaciones / numero_calificaciones
        return promedio
    
    
#SOLUCIÓN ALEJANDRA

# Solicitar al usuario los datos del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
estudiante = Estudiante(nombre_estudiante)

# Registrar asistencia
asistencia = int(input("Ingrese la cantidad de días de asistencia: "))
for _ in range(asistencia):
    estudiante.registrar_asistencia()

# Agregar calificaciones
num_calificaciones = int(input("Ingrese la cantidad de calificaciones a agregar: "))
for _ in range(num_calificaciones):
    calificacion = float(input("Ingrese una calificación: "))
    estudiante.agregar_calificacion(calificacion)

# Calcular promedio de calificaciones
promedio_calificaciones = estudiante.promedio_calificaciones()

# Mostrar resultados
print(f"\nEstudiante {estudiante.nombre}:")
print(f"Asistencia: {estudiante.asistencia} días")
print(f"Promedio de calificaciones: {promedio_calificaciones:.2f}")