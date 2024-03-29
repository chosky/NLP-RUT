import os
from nplrut import cliente_blob_service, container
from nplrut.form_recognizer.analisis_documento import analizar_documento

def carga_archivos_blob(nombre_archivo_rut, mensaje_salida):
    blob_client = cliente_blob_service.get_blob_client(container = container, blob = nombre_archivo_rut)
    with open(nombre_archivo_rut, "rb") as data:
        try:
            print("Cargando archivo: " + nombre_archivo_rut + " al almacenamiento")
            blob_client.upload_blob(data, overwrite=True)
            data = analizar_documento(nombre_archivo_rut, nombre_archivo_rut, nombre_archivo_rut.rsplit('.', 1)[1])
            mensaje_salida["tipo"] = "Correcto"
            mensaje_salida["mensaje"] = "Archivo guardado con éxito"
            mensaje_salida["data"] = data
        except Exception as ex:
            mensaje_salida["tipo"] = "Error"
            mensaje_salida["mensaje"] = str(ex)
        finally:
            return mensaje_salida