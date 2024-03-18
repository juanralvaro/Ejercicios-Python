#Busca el fallo

# Mensaje de bienvenida

print("\n\n\nBienvenido al programa de planeación de tu viaje.\n\n")

#Pedimos al usuario que introduzca su nombre

nombre=input('\nDíganos como se llama:\n\n') #fallito de escritura en la cadena

#Pedimos al usuario que introduzca sus apellidos

apellidos=input('\nDíganos sus apellidos:\n\n')

#Mostramos al usuario sus datos

print("\n\nHola", nombre.upper(), apellidos.upper(), "encantados de que use nuestra aplicación.\n\n")

# Creación de la variable "pais" lista

paises = []

# Agregamos los paises al final de la lista de forma simultánea

paises.extend(["AUSTRALIA", "EEUU", "INDIA", "NUEVA ZELANDA"])

paises.append("REINO UNIDO")

num= [0, 1, 2, 3, 4]

numero_paises=[1, 2, 3, 4, 5]

pais=["Estados Unidos", "Nueva Zelanda", "India", "Australia", "Reino Unido"]

#Pregunta de conocimiento al usuario sobre nuestro programa

conocimiento = input("\n\n¿Cuánto sabes de nuestro programa?\n\n") #no print sin variables

usuario = input(f"¿A que país quieres ir?\n\n")

check_pais = usuario in pais

print("\n\n¿El pais que has elegido está en nuestra calculadora?\n\nY la respuesta es:\n\n", check_pais)

print("\n\nSi la respuesta es True\n\nConoce nuestra aplicación. ¡Enhorabuena!\n\n\nEn cambio si la respuesta es False.\n\nLe recomendamos que pase mas tiempo trasteando, cacharreando con nuestra calculadora.\n\n\n")

#Le mostramos al usuario los destinos con los que trabajamos actualmente

print("\n\n\n\n Los paises con los que trabajamos actualmentes son:\n\n")

for i in num:

  print("-","[",numero_paises[i],"]",paises[i])

#Le mostramos al usuario de cuantos paises se compone nuestro catálogo actualmente

print("\n\n¡Actualmente contamos con",len(paises),"paises en nuestro catálogo! ¡Esperamos pronto poder ofrecerle más destinos! \n\n")

#Creamos esta nueva lista para poder operar con ella y con otro formato

list_paises = ["AUSTRALIA","EEUU", "INDIA","NUEVA ZELANDA","REINO UNIDO"]

#Le pedimos al usuario/cliente que introduzca el número del país a visitar, lo guardamos en una variable llamada "pais_eleg"

pais_eleg = int(input("Elige al país que quieres viajar del 1 al 5:\n\n"))

# Verificamos si el valor ingresado es valido, entre 1 y 5, y se lo asignamos a la variable 'index_pais'

index_pais = int(pais_eleg-1)

#Le mostramos al usuario/cliente el país que ha elegido y le pedimos el presupuesto que tiene previsto para el viaje

print("\nYa sabemos que estás interesado en viajar al país de", list_paises[index_pais], ". Ahora dinos de que presupuesto dispones o disponéis (para alimentación, alojamiento, para transporte,ocio)\n\n") #Faltaban tildes

#Pedimos al usuario que ingrese los disitntos presupuestos que disponen para gastar

presupuesto_alimentacion = float(input("\nPresupuesto en euros para gastar en alimentación:\n\n"))

presupuesto_alojamiento = float(input("\n\nPresupuesto en euros para gastar en alojamiento:\n"))

presupuesto_transporte = float(input("\n\nPresupuesto en euros para gastar en transporte:\n"))

presupuesto_ocio = float(input("\n\nPresupuesto en euros para gastar en ocio:\n"))

# Presupuesto total o acumulado

presupuesto = presupuesto_alimentacion + presupuesto_alojamiento + presupuesto_transporte + presupuesto_ocio #presupuesto_transporte estaba repetido

#Creamos la variable lista de los tipos de cambios

tipos = [1.65,1.09,90.44,1.77,0.85]

#Creamos una variable lista de los tipos de moneda de nuestra calculadora

monedas = ["Dolares australianos", "Dolares", "Rupias", "Dolares neozelandeses", "Libras Esterlinas"]

#Cálculo del tipo de cambio

cambio_money = int(presupuesto * tipos[index_pais])

#Declaramos el precio del pan en cada uno de los paises

panes = ["2.50 a 3 AUD","2,75 dólares","41,28 Rupias","3,35 NZ","£1.50"]

panes1= [2.50,2.75,41.28,3.35,1.50]

#Número de panes que puedes comprar

numero_de_panes = int(cambio_money / panes1[index_pais])

#Le mostramos al cliente un mensaje con el país que ha elegido, el tipo de cambio en el destino y el precio del pan en cada uno de los paises

print(f"\nCon el presupuesto {presupuesto:.2f} € que destinas al viaje tienes al cambio del país al que quieres viajar, {list_paises[index_pais]}, un cambio de {cambio_money} {monedas[index_pais]}.\n\nQue sepas que la barra de pan como anécdota tiene un precio de {panes[index_pais]}.\n\nLo que equivale a que puedes comprar {numero_de_panes} panes con tu presupuesto\n")

#Para que el cliente compare el poder adqusitivo de su destion con respecto al resto

#Calulamos el numero de panes que podemos comprar en cada pais

numero_panes_australianos = f"{int(cambio_money/panes1[0])} panes australianos"

numero_panes_estadounidenses = f"{int(cambio_money/panes1[1])} panes estadounidenses"

numero_panes_indios = f"{int(cambio_money/panes1[2])} panes indios"

numero_de_panes_neozelandeses = f"{int(cambio_money/panes1[3])} panes neozelandese"

numero_de_panes_ingleses = f"{int(cambio_money/panes1[4])} panes ingleses"

#Creamos la lista de el numero de panes que podemos comprar al tipo de cambio y el presupuesto destinado al viaje

list_panes = []

list_panes.extend([numero_panes_australianos ,numero_panes_estadounidenses,numero_panes_indios,numero_de_panes_neozelandeses,numero_de_panes_ingleses])

#Mostramos al usuario un listado con el numero de panes que puede comprar con el presupuesto destinado al viaje y el tipo de cambio

print("\n\nUsted puede corroborar cuántos panes puede comprar con el presupuesto total, el tipo de cambio y el precio del pan en cada destino. Así podrás ver cuál es el poder adquisitivo en cada país por el tipo de cambio y precio del pan:\n\n")

for i in num:

  print("\n-", list_panes[i])

print("\n\n\n¡Deseamos que la aplicación le haya sido de utilidad!\n\n¡Esperamos que vuelva a usar nuestra calculadora, e incluir más destinos en nuestro catálogo y opciones en nuestra aplicación!\n\n\n")


