# -*- coding: utf-8 -*-

from flask import jsonify
from flask import request
from flask import Blueprint
from werkzeug.utils import secure_filename
import json, os, requests

from nplrut.descarga_archivos.validaciones_archivo import validaciones_archivo
from nplrut.descarga_archivos.validaciones_seguridad_url import validaciones_seguridad
from nplrut.descarga_archivos.validaciones_url import validaciones_url
from nplrut.carga_archivos_blob_storage.carga_archivos_blob_storage import carga_archivos_blob

descarga_archivos_micro_service = Blueprint("descarga_archivos_micro_service", __name__)

@descarga_archivos_micro_service.route('/api/descarga_archivos', methods=['POST'])
def descarga_archivos():
    archivo_rut = request.files['archivos_rut']
    mensaje_salida = {
        "tipo": "",
        "mensaje": ""
    }
    nombre_archivo_rut = secure_filename(archivo_rut.filename)
    if nombre_archivo_rut != "":
        mensaje_salida = validaciones_archivo(nombre_archivo_rut, mensaje_salida)
        if mensaje_salida["tipo"] == "Correcto":
            print(mensaje_salida["mensaje"])
            mensaje_salida = carga_archivos_blob(nombre_archivo_rut, mensaje_salida)
            return jsonify(mensaje_salida)
        else:
            return jsonify(mensaje_salida)
    else:
        mensaje_salida["tipo"] = "Error"
        mensaje_salida["mensaje"] = "No se recivio ningún archivo"
        return jsonify(mensaje_salida)


@descarga_archivos_micro_service.route('/api/descarga_archivos_url', methods=['POST'])
def descarga_archivos_url():
    url_archivos = request.json['url_archivos']
    mensaje_salida = {
        "tipo": "",
        "mensaje": ""
    }
    mensaje_salida = validaciones_url(url_archivos, mensaje_salida)
    if mensaje_salida["tipo"] == "Correcto":
        mensaje_salida = validaciones_seguridad(url_archivos, mensaje_salida)
        if mensaje_salida["tipo"] == "Correcto":
            if url_con_archivo(url_archivos):
                nombre_archivo_rut = obtener_nombre_archivo_url(url_archivos)
                print("Descargando el archivo: " + nombre_archivo_rut)
                mensaje_salida = descargar_archivo(url_archivos, mensaje_salida, nombre_archivo_rut)
            else:
                print("Descargando archivos de la url: " + url_archivos)
                mensaje_salida = descarga_archivos_nube(url_archivos, mensaje_salida)
            return jsonify(mensaje_salida)
        else:
            return jsonify(mensaje_salida)
    else:
        return jsonify(mensaje_salida)


def url_con_archivo(url):
    # validar que en la URL esté el archivo
    nombre_archivo_rut = obtener_nombre_archivo_url(url)
    if nombre_archivo_rut != "":
        return True
    else: 
        return False


def obtener_nombre_archivo_url(url):
    nombre_archivo_rut = ""
    final_url = url.rsplit('/', 1)[1]
    try:
        if final_url.rsplit('.', 1)[1] != "": # tiene una extension
            nombre_archivo_rut = final_url
        else:
            print("La URL no posee el archivo o está mal nombrado")
    except Exception as ex:
        print("La URL no posee el archivo, error: " + str(ex))
    finally:
        return nombre_archivo_rut
        

# Esto solo sirve para URL con el archivo, hay que hacer este método diferente para cada tipo de nube :(
def descargar_archivo(url, mensaje_salida, nombre_archivo_rut):
    print("Descargando archivo")
    archivo_a_descargar = requests.get(url)
    with open(nombre_archivo_rut, "wb") as archivo_rut:
        archivo_rut.write(archivo_a_descargar.content)
        mensaje_salida = validaciones_archivo(nombre_archivo_rut, mensaje_salida)
        if mensaje_salida["tipo"] == "Correcto":
            print(mensaje_salida["mensaje"])
            mensaje_salida = carga_archivos_blob(nombre_archivo_rut, mensaje_salida)

    os.remove(nombre_archivo_rut)
    return mensaje_salida

# Al igual que el anterior este es dependiente de la nube :(
def descarga_archivos_nube(url, mensaje_salida):
    print("Descargando archivos")
    #mensaje_salida = carga_archivos_blob(archivo_rut, nombre_archivo_rut, mensaje_salida)
    return mensaje_salida

