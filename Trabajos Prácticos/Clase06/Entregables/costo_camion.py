# Ejercicio 6.12

import informe_funciones

def costo_camion(nombre_archivo):
    cTotal = 0
    cCamion = informe_funciones.leer_camion(nombre_archivo)
    for camion in cCamion:
        cTotal += camion['cajones'] * camion['precio']
    return cTotal

