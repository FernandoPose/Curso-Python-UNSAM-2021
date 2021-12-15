# Ejercicio 4.9

import csv

def leer_camion(nombre_archivo):
    ''' Precios pagados al productor de frutas'''
    cCamion = []
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(file)
        for nombre, cajones, precio in rows:
            lote = {'nombre':nombre, 'cajones':int(cajones), 'precio':float(precio)}
            cCamion.append(lote)
        return cCamion

def leer_precios(nombre_archivo):
    ''' Precios de venta en almacén'''
    lPrecios = {}
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        try:
            for nombre, precio in rows:
                lPrecios[nombre] = float(precio)
        except ValueError:
            pass  
    return lPrecios

#? Comienza el programa
pCamion     = leer_camion('../Data/camion.csv')

mas100      = [ s for s in pCamion if s['cajones'] > 100 ]
myn         = [ s for s in pCamion if s['nombre'] in {'Mandarina', 'Naranja'} ]
costo10k    = [ s for s in pCamion if s['cajones'] * s['precio'] > 10000]
