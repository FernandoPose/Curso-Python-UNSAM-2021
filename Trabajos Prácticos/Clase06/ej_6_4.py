# Ejercicio 6.4

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

def hacer_informe(pCamion, pAlmacen):
    informe = list()
    for Camion in pCamion:
        registro    = ()
        registro    = (Camion['nombre'], int(Camion['cajones']), float(Camion['precio']))
        cambio      = pAlmacen[Camion['nombre']] - Camion['precio']
        registro    = registro + (round(cambio,2),)
        informe.append(registro)
    return informe

def imprimir_informe(informe):
    ''' Imprime el informe '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

pCamion     = leer_camion('../Data/camion.csv')
pAlmacen    = leer_precios('../Data/precios.csv')
informe     = hacer_informe(pCamion, pAlmacen)

imprimir_informe(informe)

