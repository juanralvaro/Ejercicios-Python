""" Desarrolla un programa en Python que simule una calculadora básica. El programa solicitará al usuario que ingrese dos números y luego le permitirá realizar operaciones matemáticas básicas seleccionando un operador. El programa continuará ejecutándose hasta que el usuario decida salir.

1. El programa iniciará un bucle **`while`** para permitir la ejecución continua del programa.
2. Dentro del bucle, el programa solicitará al usuario que ingrese dos números y almacenará estos valores en variables.
3. Luego, el programa solicitará al usuario que seleccione un operador matemático entre suma (+), resta (-), multiplicación (*) o división (/).
4. Dependiendo del operador seleccionado, el programa realizará la operación correspondiente con los dos números ingresados.
5. El resultado de la operación se mostrará al usuario.
6. Después de mostrar el resultado, el programa preguntará al usuario si desea continuar o salir del programa.
7. Si el usuario elige continuar, el programa volverá al paso 2.
8. Si el usuario elige salir, el programa imprimirá un mensaje de despedida y finalizará la ejecución. """

print("Bienvenido a la calculadora de Python.")


# Inicialización del bucle principal
while True:

# Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Solicitar al usuario que seleccione un operador matemático
    operador = input("Ingrese el operador matemático (+, -, *, /): ")
    
    # Realizar la operación correspondiente según el operador seleccionado
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        # Manejar la división por cero
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: No se puede dividir entre cero.")
            continue  # Volver al inicio del bucle
        
    # Mostrar el resultado de la operación
    print("El resultado es:", resultado)
    
    # Preguntar al usuario si desea continuar o salir del programa
    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != 's':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break  # Salir del bucle principal