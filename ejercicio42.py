#Busca el fallo (Easter edition)

salario_anual = float(input("Ingresa tu salario anual: "))

if salario_anual <= 10000: #Faltan los dos puntos
    impuesto = salario_anual * 0.05
    impuesto = salario_anual * 0.10 #Falta un elif (ej. elif salario anual <= 25000), si no lo segundo anularía a lo primero
elif salario_anual <= 50000: #Falta la indentación
    impuesto = salario_anual * 0.15
else:
    impuesto = salario_anual * 0.20

print(f"Tu salario anual es de ${salario_anual}")
print(f"El impuesto correspondiente es del {(impuesto / salario_anual) * 100:.0f}%, lo que equivale a ${impuesto:.2f}\n")

print("Impuestos para diferentes rangos de ingresos:")
for i in range(0, 200001, 10000):
    if i <= 10000:
        impuesto_rango = i * 0.05
    elif i <= 50000:
        impuesto_rango = i * 0.10
    elif i <= 100000:
        impuesto_rango = i * 0.15
    else:
        impuesto_rango = i * 0.20
    print(f"Salario anual de ${i} - ${i + 10000}: ${impuesto_rango:.2f}") #Cero fallos

#Parte2

# Este programa determina si un estudiante ha aprobado o no un examen

puntaje = float(input("Ingrese el puntaje del estudiante: "))

# Comprueba si el puntaje es mayor o igual a 60 para aprobar
estado = "Aprobado" if puntaje >= 60 else "Reprobado"

print(f"El estudiante está {estado}")

# Verifica si el estudiante obtuvo una calificación adicional y le da un bono si es así
bono = True
mensaje_bono = "Felicidades, has ganado un bono!" if bono else "Lo siento, no ganaste un bono."

print(mensaje_bono)

# Calcula el promedio de calificaciones para determinar si el estudiante pasa al siguiente nivel
calificaciones = [puntaje, 80, 90, 85]
promedio = sum(calificaciones) / len(calificaciones)
pasa_nivel = "Pasa al siguiente nivel" if promedio >= 80 else "No pasa al siguiente nivel"

print(f"El promedio de calificaciones es {promedio}. {pasa_nivel}") #No hay error