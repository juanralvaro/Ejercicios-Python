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




while True:
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    print("Operaciones disponibles:")
    print("\n1: Suma.")
    print("\n2: Resta:")
    print("\n3: Multiplicación.")
    print("\n4: División.")
    operacion = int(input("\nSeleccione una operación: "))
    if operacion == 1:
        resultado = num1 + num2
        print(resultado)
    elif operacion == 2:
        resultado = num1 - num2
        print(resultado)
    elif operacion == 3:
        resultado = num1 * num2
        print(resultado)
    elif operacion == 4:
        if num2 !=0 :
            resultado = num1 / num2
            print(resultado)
        else:
            print("No se puede dividir por cero.")
    else:
        print("Número erróneo. Introduzca el correcto:")
    continuar = str(input("¿Desea continuar? (S/N): ")) == "S" #Inicializo una variable booleana para que el usuario diga si seguir o no, si es S (True) sigue, si no (False) hará break
    if not continuar:
        break
print("Gracias por usar la calculadora de Python.")