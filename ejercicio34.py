""" 1. **Inicialización del inventario:**
    - Crea una lista llamada **`inventario`** que contendrá tuplas representando los productos en stock. Cada tupla contendrá el nombre del producto, su precio y la cantidad disponible en la tienda.
    - Agrega al menos 5 productos al inventario.
2. **Operaciones del inventario:**
    - Agrega un nuevo producto al inventario especificando su nombre, precio y cantidad.
    - Actualiza la cantidad disponible de un producto existente en el inventario.
    - Elimina un producto del inventario.
    - Busca un producto en el inventario y muestra su información si está disponible.
3. **Operaciones adicionales:**
    - Ordena el inventario alfabéticamente por nombre de producto.
    - Cuenta cuántos productos tienes en el inventario.
    - Encuentra la posición de un producto específico en el inventario.
4. **Mostrar resultados:**
    - Después de cada operación, muestra el inventario actualizado con todos los productos y su información.
    - Al final, muestra el inventario completo una última vez antes de finalizar el programa.
    - Puedes dar formato de salida a la muestra de inventario para que simule una tabla utilizando caracteres especiales. """

#Bienvenida
print("Bienvenido al inventario.")

#1. Creación inventario
inventario = [("Aceite de girasol", 1.40, 14), ("Leche desnatada", 0.85, 42), ("Coca-Cola", 0.90, 50), ("Barra pan tradicional", 0.85, 15), ("Kilo carne cerdo", 7, 10)]

#2. Operaciones inventario
inventario.append(("Sardinas en aceite", 0.85, 15))
print("Inventario ampliado",inventario)
inventario[0] = ("Aceite de girasol", 1.40, 10)
print("Inventario modificado",inventario)
inventario.remove(("Barra pan tradicional", 0.85, 15))
print("Inventario reducido",inventario)
informacion_leche = inventario[1]
print("La leche disponible es:",informacion_leche)

#3. Operaciones adicionales
inventario.sort()
print("Inventario ordenado:",inventario)
print(f"Hay {len(inventario)} productos en el inventario.")
posicion_coca_cola = inventario.index(('Coca-Cola', 0.9, 50))
print(f"La Coca-Cola está en la {posicion_coca_cola+1}ª posición de la lista.")

#4. Inventario completo y estético
print("Inventario final",inventario)

print("############################################")
print("# Ven a GADIS, el precio no es un problema #")
print("#       NUESTRO INVENTARIO DE HOY ES:      #")
print(f"#     ",inventario[0],"     #")
print(f"#         ",inventario[1],"         #")
print(f"#      ",inventario[2],"       #")
print(f"#     ",inventario[3],"      #")
print(f"#    ",inventario[4],"    #")
print("#            GADIS. EN CONFIANZA           #")
print("############################################")