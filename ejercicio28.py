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

comunidad_de_vecinos = {
    "Piso": '',
    "Nombre": '',
    "Apellidos": '',
    "Pago": '',
    "Garaje": '',
    "Ninos": ''
}

comunidad_de_vecinos["Piso"] = str(input("Introduzca el nombre del piso: "))
comunidad_de_vecinos["Nombre"] = str(input("Introduzca el nombre del propietario: "))
comunidad_de_vecinos["Apellidos"] = str(input("Introduzca los apellidos del propietario: "))
comunidad_de_vecinos["Pago"] = bool(input("¿Ha pagado la comunidad del mes? Diga True o False: "))
comunidad_de_vecinos["Garaje"] = bool(input("¿Tiene plaza de garaje? Diga True o False: "))
comunidad_de_vecinos["Ninos"] = int(input("¿Tiene niños?: "))

print(comunidad_de_vecinos)

for piso in comunidad_de_vecinos:
    print(f"{comunidad_de_vecinos.get("Piso")}")

""" for vecino in comunidad_de_vecinos:
    print(f"{comunidad_de_vecinos.get("Nombre", "Apellidos")}")

for vecino in comunidad_de_vecinos:
    print(f"{comunidad_de_vecinos.get("Pago")}")

for garaje in comunidad_de_vecinos:
    print(f"{comunidad_de_vecinos.get("Garaje", "Apellidos")}") """