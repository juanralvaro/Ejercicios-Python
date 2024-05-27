import pymongo

# Conexión a la base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["proyecto_final"]

# Definición de las colecciones
socios_collection = database["socios"]
productos_collection = database["productos"]
ventanas_temporales_collection = database["ventanas_temporales"]
transacciones_collection = database["transacciones"]
pujas_collection = database["pujas"]
administradores_collection = database["administradores"]
fabricantes_collection = database["fabricantes"]
contabilidad_collection = database["contabilidad"]

# Definición de documentos de ejemplo para cada colección
socio = {
    "_id": 1,
    "realizar_puja_o_compra": True,
    "fondo_individual": 1000,
    "avatar": "avatar.jpg",
    "conexion_app": True
}
socios_collection.insert_one(socio)

producto = {
    "_id": 1,
    "objeto_de_puja": "Teléfono móvil",
    "caracteristicas_tecnicas": {"marca": "Samsung", "modelo": "Galaxy S20", "color": "Negro"},
    "imagenes": ["imagen1.jpg", "imagen2.jpg"],
    "stock": 50
}
productos_collection.insert_one(producto)

ventana_temporal = {
    "_id": 1,
    "fecha_inicio": "2024-04-01",
    "fecha_cierre": "2024-04-30"
}
ventanas_temporales_collection.insert_one(ventana_temporal)

transaccion = {
    "_id": 1,
    "pago": 500,
    "descuento_o_oferta": None,
    "confirmacion_aceptado": True,
    "fecha_entrega": "2024-04-15"
}
transacciones_collection.insert_one(transaccion)

puja = {
    "_id": 1,
    "fecha_inicio": "2024-04-01",
    "fecha_fin": "2024-04-15"
}
pujas_collection.insert_one(puja)

administrador = {
    "_id": 1,
    "alta_baja_socios": True,
    "seleccion_productos": True
}
administradores_collection.insert_one(administrador)

fabricante = {
    "_id": 1,
    "datos_fabricante": {"empresa": "Samsung", "direccion": "Seúl, Corea del Sur"},
    "producto": "Teléfono móvil",
    "oferta_especial_transaccion": True
}
fabricantes_collection.insert_one(fabricante)

contabilidad = {
    "_id": 1,
    "fondo_individual": 1000,
    "fondo_comun": 5000,
    "comision": 0.05
}
contabilidad_collection.insert_one(contabilidad)

print("Base de datos creada con éxito.")