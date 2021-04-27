# -*- coding: utf-8 -*-

from flask import jsonify
from flask import request
from flask import Blueprint
from werkzeug.utils import secure_filename
import json, os

from nplrut.descarga_archivos.validaciones_archivo import validaciones_archivo
from nplrut.descarga_archivos.validaciones_seguridad_url import validaciones_seguridad
from nplrut.descarga_archivos.validaciones_url import validaciones_url
from nplrut.carga_archivos_blob_storage.carga_archivos_blob_storage import carga_archivos_blob

descarga_archivos_micro_service = Blueprint("descarga_archivos_micro_service", __name__)

descarga_archivos_micro_service.route('/api/descarga_archivos', methods=['POST'])
def descarga_archivos():
    archivos_rut = request.files['archivos_rut']
    mensaje_salida = {
        "tipo": "",
        "mensaje": ""
    }
    if len(archivos_rut) != 0: 
        for archivo_rut in archivos_rut:
            nombre_archivo_rut = secure_filename(archivo_rut.filename)
            mensaje_salida = validaciones_archivo(archivo_rut, mensaje_salida)
            if mensaje_salida["tipo"] == "Correcto":
                print(mensaje_salida["mensaje"])
                mensaje_salida = carga_archivos_blob(archivo_rut, nombre_archivo_rut, mensaje_salida)
                return jsonify(mensaje_salida)
            else:
                return jsonify(mensaje_salida)
    else:
        mensaje_salida["tipo"] = "Error"
        mensaje_salida["mensaje"] = "No se recivio ningún archivo"
        return jsonify(mensaje_salida)


descarga_archivos_micro_service.route('/api/descarga_archivos_url', methods=['POST'])
def descarga_archivos_url():
    url_archivos = request.json['url_archivos']
    mensaje_salida = {
        "tipo": "",
        "mensaje": ""
    }
    return jsonify(True)
