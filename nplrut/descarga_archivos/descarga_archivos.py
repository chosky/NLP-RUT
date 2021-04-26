# -*- coding: utf-8 -*-

from flask import jsonify
from flask import request
from flask import Blueprint
from werkzeug.utils import secure_filename
import json, os

from nplrut import blob_service, container
from nplrut.descarga_archivos.validaciones_archivo import validaciones_archivo
from nplrut.descarga_archivos.validaciones_seguridad_url import validaciones_seguridad
from nplrut.descarga_archivos.validaciones_url import validaciones_url

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


def carga_archivos_blob(archivo_rut, nombre_archivo_rut, mensaje_salida):
    archivo_rut.save(nombre_archivo_rut)
    blob_client = blob_service_client.get_blob_client(container = container, blob = nombre_archivo_rut)
    with open(nombre_archivo_rut, "rb") as data:
        try:
            print("Cargando archivo: " + nombre_archivo_rut + " al almacenamiento")
            blob_client.upload_blob(data, overwrite=True)
            mensaje_salida["tipo"] = "Correcto"
            mensaje_salida["mensaje"] = "Archivo guardado con éxito"
        except Exception as ex:
            mensaje_salida["tipo"] = "Error"
            mensaje_salida["mensaje"] = ex
        finally:
            os.remove(filename)
            return mensaje_salida