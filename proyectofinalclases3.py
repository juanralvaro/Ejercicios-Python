from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://beldic:<CLAVE>@techcashclub.akflm9s.mongodb.net/club"

mongo = PyMongo(app)

@app.route('/')
def index():
    try:
        # Intenta obtener un documento de la colección 'usuarios'
        socio = mongo.db.socios.find_one({'nombre': 'Juan'})
        if socio:
            return f'Hola, {socio["nombre"]}'
        else:
            return 'Usuario no encontrado'
    except Exception as e:
        return f'Error de conexión: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
    
    