""" - Reto de programación II
    
    **Objetivo:**
    El objetivo de este ejercicio es que cada grupo de estudiantes plantee un programa de Python que incluya fallos de sintaxis, de concepto y de estilo. Los demás grupos deberán resolver los desafíos planteados por los otros grupos.
    
    **Instrucciones:**
    
    1. **Creación de programas:**
        - Cada grupo debe crear un programa en Python que contenga al menos 10 fallos de sintaxis, de concepto o de estilo.
        - El programa debe utilizar la sintaxis y los conceptos vistos hasta el momento en el curso.
    2. **Resolución de desafíos:**
        - Los demás grupos deberán intentar resolver los desafíos planteados por los otros grupos.
        - Se recomienda trabajar en equipo para identificar y corregir los fallos en los programas de los otros grupos.
        - El grupo que logre corregir todos los fallos correctamente en el menor tiempo posible será el ganador.
    3. **Reflexión:**
        - Al finalizar el ejercicio, se realizará una corrección sobre los errores cometidos, las soluciones encontradas y los conceptos aprendidos, la cual se reflejará como siempre en comentarios en la propia corrección del ejercicio.
    
    **Notas:**
    
    - Se puede utilizar cualquier tema o contexto para los programas, siempre y cuando se respeten los requisitos del ejercicio.
    - Se recomienda que los programas sean lo suficientemente desafiantes para que los otros grupos tengan que esforzarse en resolver los problemas planteados. """


"""
 EJERCICIO RETO DE PROGRAMACIÓN II - ¡ENCUENTRA LOS FALLOS! (Revisado)
 AUTORES: Manuel,Juan,Rafael y Jordi. 
 Enunciado: 
 Diseñar un avanzado algoritmo o programa en Python que acepte el registro de
 un propietario de una comunidad de vecinos y muestre por pantalla los datos. 


 """

# Recogida de datos para un propietario usando un diccionario
Propietario = {
    "nombre": str(input("Introduce el nombre del propietario: ")),
    'piso':   int(input("Introduce el piso: ")),
    "puerta": str(input("Introduce la puerta: ")),
    "moroso": bool(input("¿Es moroso? (True/False): ")),
    "garaje": bool(input("¿Tiene garaje? (True/False): "))
}



# Mostrando los datos recogidos
for clave, valor in Propietario.items():
    print(f"{clave.capitalize()}: {valor}")