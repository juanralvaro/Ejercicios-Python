#PREGUNTA 1
#Una función se puede declarar en cualquier lugar del código

#PREGUNTA 2 - Opción correcta
def suma(a: int, b: int) -> int:
    resultado = a + b
    return resultado

#PREGUNTA 2 - Opción incorrecta pero posible
def suma_b(a: int, b: int) -> int:
    resultado = a + b
    print(f"La sumatoria es: {resultado}") #La sumatoria es: 5
    
#PREGUNTA 3 - Opción correcta
def resta(a: int, b: int) -> int:
    resultado = a - b
    return resultado

#PREGUNTA 4 - Opción correcta
def Suma(a: int, b: int) -> int:
    a + b #Si una función no tiene un resultado que devolver, me va a devolver un None

#PREGUNTA 4 - Opción incorrecta pero posible
def suma(a: int, b: int) -> int:
    resultado = a + b
    return resultado
    
#PREGUNTA 4 - Opción incorrecta pero posible
def Suma_b(a: int, b: int) -> int:
    resultado = a + b
    return resultado

#PREGUNTA 4 - Opción incorrecta pero posible
def Suma_c(a: int, b: int) -> int:
    resultado = a + b
    print(f"La sumatoria es: {resultado}") #La sumatoria es: 5
    
#PREGUNTA 5
#Python tiene tipado dinámico pues no es necesario declarar el tipo de datos de una determinada variable

#PREGUNTA 6 - Opción correcta
usuario = "Juan"

def saluda():
    saludo = f"Hola, {usuario}"
    return saludo
    
#PREGUNTA 6 - Opción incorrecta pero posible
def saluda_b():
    saludo = "Hola"
    return saludo
    
#PREGUNTA 7 - Opción correcta
def doble(a: int) -> int:
    resultado_uno = 2 * a
    return resultado_uno

#PREGUNTA 8
#En Python, las listas pueden tener diferentes tipos de datos simultáneamente

#PREGUNTA 9 - Opción correcta
def suma_sin_return(a: int, b: int) -> int:
    a + b
    
#PREGUNTA 10 - Opción correcta

""" numero_uno = int(input("Introduce el primer número: "))
numero_dos = int(input("Introduce el primer número: "))

def resta2(b=numero_uno, a=numero_dos):
    resultado = b - a
    print(resultado) """
    
#PREGUNTA 11
#En Python, una función puede tener varios parámetros

#PREGUNTA 12
#En Python, los DocStrings sirven para documentar funciones

#PREGUNTA 13
#En Python, las Function Annotations son metadatos que agregamos en la entrada y salida de una reunión

#PREGUNTA 14
#En Python, una función puede retornar múltiples valores utilizando la sentencia return

#PREGUNTA 15 - Opción correcta
def es_par(a: int) -> int:
    if a % 2 == 0:
        return True
    else:
        return False

#print(es_par(7))
    
#PREGUNTA 15 - Opción incorrecta pero posible
def es_par2(a: int) -> int:
    if a % 2 == 0:
        print(f"El número es par: True")
    else:
        print(f"El número es par: False")
        
#es_par2(7)
    
#PREGUNTA 15 - Opción incorrecta pero posible
def es_par3(a: int) -> int:
    if a % 2 == 0:
        print(f"El número es par: True")

#print(es_par3(7))

#PREGUNTA 16 - Opción correcta
def dividir(a: int, b: int) -> int:
    if b == 0:
        return "Error: no se puede dividir por cero"
    else:
        resultado = a / b
        print(resultado)
        
#PREGUNTA 16 - Opción incorrecta pero posible
def dividir(a: int, b: int) -> int:
    if b == 0:
        print("Error: no se puede dividir por cero")
    else:
        resultado = a / b
        print(resultado)

#PREGUNTA 17
#En Python, la función return devuelve un valor al punto donde fue llamada la función

#PREGUNTA 18
#En Python, las funciones pueden admitir argumentos

#PREGUNTA 19 - Opción correcta

def sumar_ingresos(*valores):
    resultado = sum(valores)
    print(resultado)
    
#sumar_ingresos(1500, 1500, 1500) retornaría 4500

#PREGUNTA 20
def calcular_total(*numeros) -> int:
    resultado = sum(numeros)
    return resultado
    
print(calcular_total(10,20,30,40,50,60,70))