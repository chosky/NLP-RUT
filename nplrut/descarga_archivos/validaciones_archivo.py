# -*- coding: utf-8 -*-

def validaciones_archivo(archivo_rut, mensaje_salida):
    nombre_archivo_rut = archivo_rut.filename
    if validar_extension(nombre_archivo_rut):
        if validar_archivo_con_contraseña(archivo_rut):
            if validar_tamano_archivo(archivo_rut):
                if validar_numero_paginas(archivo_rut):
                    if validar_resolucion_archivo(archivo_rut):
                        mensaje_salida["tipo"] = "Correcto"
                        mensaje_salida["mensaje"] = "El archivo cumple con todas las validaciones."
                        return mensaje_salida
                    else:
                        mensaje_salida["tipo"] = "Error"
                        mensaje_salida["mensaje"] = "Mala resolución en el archivo."
                        return mensaje_salida
                else:
                    mensaje_salida["tipo"] = "Error"
                    mensaje_salida["mensaje"] = "Número de páginas excedido."
                    return mensaje_salida
            else:
                mensaje_salida["tipo"] = "Error"
                mensaje_salida["mensaje"] = "Tamaño del archivo excedido."
                return mensaje_salida
        else:
            mensaje_salida["tipo"] = "Error"
            mensaje_salida["mensaje"] = "Archivo con contraseña."
            return mensaje_salida
    else:
        mensaje_salida["tipo"] = "Error"
        mensaje_salida["mensaje"] = "Archivo con extensión invalida."
        return mensaje_salida


def validar_extension(nombre_archivo_rut):
    extensiones_permitidas = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])
    extension_archivo = nombre_archivo_rut.rsplit('.', 1)
    if extension_archivo in extensiones_permitidas:
        return True
    else:
        return False


def validar_archivo_con_contraseña(archivo_rut):
    return True


def validar_tamano_archivo(archivo_rut):
    tamano_maximo = 20 * 1024 * 1024    # 20 Mb limit
    return True


def validar_numero_paginas(archivo_rut):
    return True


def validar_resolucion_archivo(archivo_rut):
    return True
