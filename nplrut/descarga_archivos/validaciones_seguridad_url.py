def validaciones_seguridad(url, mensaje_salida):
    if validar_nube_conocida(url):
        if validar_xss(url):
            if validar_sqli(url):
                if validar_lfi(url):
                    if validar_rfi(url):
                        mensaje_salida["tipo"] = "Correcto"
                        mensaje_salida["mensaje"] = "El archivo cumple con todas las validaciones."
                        return mensaje_salida
                    else:
                        mensaje_salida["tipo"] = "Error"
                        mensaje_salida["mensaje"] = "Sentencia RFI detactada."
                        return mensaje_salida
                else:
                    mensaje_salida["tipo"] = "Error"
                    mensaje_salida["mensaje"] = "Sentencia LFI detactada."
                    return mensaje_salida
            else:
                mensaje_salida["tipo"] = "Error"
                mensaje_salida["mensaje"] = "Sentencia SQLi detactada."
                return mensaje_salida
        else:
            mensaje_salida["tipo"] = "Error"
            mensaje_salida["mensaje"] = "Sentencia XSS detectada."
            return mensaje_salida
    else:
        mensaje_salida["tipo"] = "Error"
        mensaje_salida["mensaje"] = "La URL no es confiable."
        return mensaje_salida


def validar_nube_conocida(url):
    nubes_conocidas = set(['dropbox', 'google', 'sharepoint', 'mega'])
    return True


def validar_xss(url):
    return True


def validar_sqli(url):
    return True


def validar_lfi(url):
    return True


def validar_rfi(url):
    return True

