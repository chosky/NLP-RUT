from flask import jsonify
from flask import request
from flask import Blueprint
import json

from nlp.descarga_archivos.validaciones_archivo import validaciones_archivo
from nlp.descarga_archivos.validaciones_seguridad_url import validaciones_seguridad
from nlp.descarga_archivos.validaciones_url import validaciones_url

descarga_archivos_micro_service = Blueprint("descarga_archivos_micro_service", __name__)

descarga_archivos_micro_service.route('/api/descarga_archivos', methods=['POST'])
def descarga_archivos():
    archivos_rut = request.files['archivos_rut']

    for archivo_rut in archivos_rut:
        print(archivo_rut.filename)

    return jsonify(True)


descarga_archivos_micro_service.route('/api/descarga_archivos_url', methods=['POST'])
def descarga_archivos_url():
    url_archivos = request.json['url_archivos']
    return jsonify(True)
