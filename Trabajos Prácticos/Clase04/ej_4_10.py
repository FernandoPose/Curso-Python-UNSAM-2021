# Ejercicio 4.10

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
pAlmacen    = leer_precios('../Data/precios.csv')

nombre_cajones_lista    = [ (s['nombre'], s['cajones']) for s in pCamion ]

nombres = { s['nombre'] for s in pCamion }
stock   = {nombre:0 for nombre in nombres}
for s in pCamion:
    stock[s['nombre']] += s['cajones']

camion_precios = {nombre: pAlmacen[nombre] for nombre in nombres}    



