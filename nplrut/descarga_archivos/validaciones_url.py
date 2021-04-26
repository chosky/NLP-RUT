def validaciones_url(url, mensaje_salida):
    if validar_respuesta_url(url):
        mensaje_salida["tipo"] = "Correcto"
        mensaje_salida["mensaje"] = "La URL responde."
        return mensaje_salida
    else:
        mensaje_salida["tipo"] = "Error"
        mensaje_salida["mensaje"] = "La URL no responde."
        return mensaje_salida
        

def validar_respuesta_url(url):
    return True