""" - 11- Programa calculadora de edades (WeekEnd)
    
    Crea un programa en Python que solicite al usuario ingresar su año de nacimiento y el año actual. Utiliza esta información para calcular su edad actual y edad futura.
    
    1. Solicita al usuario que introduzca su año de nacimiento.
    2. Solicita al usuario que introduzca el año actual.
    
    Luego, realiza los siguientes cálculos:
    
    - Calcula la edad actual restando el año de nacimiento del año actual.
    - Calcula la edad que tendría en 5 años sumando 5 a la edad actual.
    - Calcula la edad que tendría en 10 años sumando 10 a la edad actual.
    
    Finalmente, utiliza la función **`print()`** para mostrar un mensaje que incluya la información de la siguiente manera:
    
    *¡Bienvenido a la Calculadora de Edades!*
    
    *Introduce tu año de nacimiento: 1990
    Introduce el año actual: 2023*
    
    *Resultados:*
    
    - *Tienes 33 años, ¡Aún te queda muchas cosas buenas por vivir!*
    - *En 5 años tendrás 38 años.*
    - *En 10 años tendrás 43 años.* """

print("¡Bienvenido a la calculadora de edades!")
birth_year = int(input("\nIntroduce tu año de nacimiento: "))
current_year = int(input("\nIntroduce el año actual: "))
current_age = current_year - birth_year
age_in_5_years = current_age + 5
age_in_10_years = current_age + 10
print("\nResultados:")
print("\nActualmente tienes " + str(current_age) + " años.")
print("\nDentro de 5 años tendrás " + str(age_in_5_years) + " años.")
print("\nY dentro de 10 años tendrás " + str(age_in_10_years)+ " años.")
print("\nNo te deprimas, ¡tienes mucho que vivir!")