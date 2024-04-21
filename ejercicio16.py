""" - 16- Gestión de usuarios (operadores de pertenencia & identidad)
    
    Crea un programa en Python que simule la gestión de usuarios en un sistema. Utiliza variables para representar información sobre dos usuarios diferentes. Luego, utiliza operadores de pertenencia (**`in`**, **`not in`**) y de identidad (**`is`**, **`is not`**) para realizar las siguientes acciones:
    
    1. Verifica si un usuario llamado **`usuario_actual`** está registrado en el sistema.
    2. Comprueba si ambos usuarios comparten la misma dirección de correo electrónico.
    3. Identifica si los objetos que representan a los usuarios son diferentes.
    
    Muestra los resultados utilizando la función **`print()`**.
    
    *Condiciones iniciales*
    
    *# Información del Usuario 1*
    
    *usuario1_nombre = "Alice"
    usuario1_correo = "[alice@email.com](mailto:alice@email.com)"*
    
    *# Información del Usuario 2*
    
    *usuario2_nombre = "Bob"
    usuario2_correo = "[bob@email.com](mailto:bob@email.com)"*
    
    *# Usuario Actual a Verificar*
    
    *usuario_actual = "Alice"*
    
    *Ejemplo de salida*
    
    *# Verificación de Usuarios:*
    
    *Usuario 'Alice' está registrado: True*
    
    *Comprobación de Correo Electrónico:
    Ambos usuarios comparten el mismo correo electrónico: False*
    
    *Identificación de Objetos:
    Los objetos que representan a los usuarios son diferentes: True* """

print("Bienvendo al sistema de gestión de usuarios.")

usuario1_nombre = "Javier"
usuario1_correo = "javier@yahoo.es"

usuario2_nombre = "Marta"
usuario2_correo = "Marta@gmail.com"

usuario_actual = "Javier"

print("Verificación de usuario")

usuario_esta = usuario_actual in (usuario1_nombre, usuario2_nombre)

print(f"¿Está registrado Javier en el sistema? {usuario_esta}")

print("Comprobación de correo electrónico")

mismo_correo = usuario1_correo is usuario2_correo

print(f"¿Ambos usuarios comparten correo electrónico? {mismo_correo}")

print("Identificación de objetos de usuarios")

objetos_diferentes = usuario1_nombre is not usuario2_nombre

print(f"¿Son los objetos de los usuarios diferentes? {objetos_diferentes}")

#Solución

 # Información del usuario 1
usuario1_nombre = "Alice"
usuario1_correo = "alice@email.com"

# Información del usuario 2
usuario2_nombre = "Bob"
usuario2_correo = "bob@email.com"

# Usuario actual a verificar
usuario_actual = "Alice"

#Lista de usuarios
lista_usuarios = [usuario1_nombre, usuario2_nombre]

# Verificación de usuarios
usuario_actual_registrado = usuario_actual in (usuario1_nombre, usuario2_nombre)
print("Usuario '{}' está registrado: {}".format(usuario_actual, usuario_actual_registrado))

# Comprobación de correo electrónico
mismo_correo = usuario1_correo is usuario2_correo
print("\nAmbos usuarios comparten el mismo correo electrónico:", mismo_correo)

# Identificación de objetos
objetos_diferentes = usuario1_nombre is not usuario2_nombre
print("\nLos objetos que representan a los usuarios son diferentes:", objetos_diferentes)