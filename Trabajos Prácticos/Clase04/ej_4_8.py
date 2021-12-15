# Ejercicio 4.8

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

costo = sum([s['cajones'] * s['precio'] for s in pCamion])
print(f'El costo total del camion es: {costo}')

valor = sum([s['cajones'] * pAlmacen[s['nombre']] for s in pCamion])
print(f'Valor en mercado: {valor}')


