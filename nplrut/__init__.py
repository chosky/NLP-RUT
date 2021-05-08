# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from flasgger import Swagger
from azure.storage.blob import BlobServiceClient
import os

# Instancia de la aplicación de flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
swagger = Swagger(app)
CORS(app, resources= { r"/*": {"origins": "*"} })

# Llamada a configuraciones privadas
app.config.from_pyfile('config.py')

# Llamado a Azure BlobStorage 
# Help links: 
#   https://franckess.com/post/uploading-files-azure-blob-flask/
#   https://github.com/codesagar/Azure-Blobs 
account = app.config['ACCOUNT_NAME']
key = app.config['ACCOUNT_KEY']
connect_str = app.config['CONNECTION_STRING']
container = app.config['CONTAINER']

cliente_blob_service = BlobServiceClient.from_connection_string(connect_str)

# Configuración de la base de datos Mongo y su conección
#app.config['MONGO_URI'] = ''
#mongo = PyMongo(app)


# Definiciones de rutas de los blueprints
#from nplrut.routes.routes import routes_app
from nplrut.descarga_archivos.descarga_archivos import descarga_archivos_micro_service

# Instancias del Blueprint
#app.register_blueprint(routes_app)
app.register_blueprint(descarga_archivos_micro_service)

#Esto permite hacer pruebas con HTTP (Solo usar en local)
#os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

@app.route('/api')
def index():
    return 'Server on'
    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
    return render_template('index.html')
