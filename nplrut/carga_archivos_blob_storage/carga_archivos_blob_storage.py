import os
from nplrut import cliente_blob_service, container

def carga_archivos_blob(archivo_rut, nombre_archivo_rut, mensaje_salida):
    archivo_rut.save(nombre_archivo_rut)
    blob_client = cliente_blob_service.get_blob_client(container = container, blob = nombre_archivo_rut)
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
            os.remove(nombre_archivo_rut)
            return mensaje_salida