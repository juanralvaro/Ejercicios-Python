""" EJERCICIO 5

Crea un programa que simule un gestor de información de un diario. Para ello el programa deberá solicitar al usuario que introduzca la fecha con formato DÍA DE LA SEMANA + día del mes (en número) + mes. Además en una nueva instrucción le pedirá al usuario que introduzca la hora y en una nueva instrucción le pedirá el texto de la entrada que desea almacenar. Al finalizar el programa mostrará al usuario toda la información con el siguiente formato: 

• fecha string en mayúscula 

• hora string

• texto de la entrada del diario en minúscula. """

dia_semana = str(input("Introduzca la fecha en formato DÍA DE LA SEMANA: \n"))
dia_mes = int(input("Introduzca el día del mes en número: \n"))
mes = str(input("Introduzca el mes: \n"))

hora = str(input("Introduzca la hora: \n"))

fecha = (dia_semana.upper(), dia_mes, mes.upper())

entrada = str(input("Introduzca el texto de la entrada: \n"))

print(fecha, hora, entrada.lower())