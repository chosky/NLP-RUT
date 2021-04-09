# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from flasgger import Swagger
import os

# Instancia de la aplicación de flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
swagger = Swagger(app)
CORS(app, resources= { r"/*": {"origins": "*"} })

# COnfiguración de la base de datos Mongo y su conección
#app.config['MONGO_URI'] = ''
#mongo = PyMongo(app)


# Definiciones de rutas de los blueprints
#from nplrut.routes.routes import routes_app

# Instancias del Blueprint
#app.register_blueprint(routes_app)

#Esto permite hacer pruebas con HTTP (Solo usar en local)
#os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

@app.route('/api')
def index():
    return 'Server on'
    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
    return render_template('index.html')
