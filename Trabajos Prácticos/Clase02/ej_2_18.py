# Ejercicio 2.18

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

def generar_informe(pCamion, pAlmacen):
    # Costo del camión, Recaudación del negocio y diferencia.
    # Indicar si hubo ganancia o pérdida
    
    pCamionTotal = 0
    pAlmacenTotal = 0
    
    for Camion in pCamion:
        pCamionTotal =  pCamionTotal + int(Camion['cajones']) * float(Camion['precio'])
        if Camion['nombre'] in pAlmacen:
            pAlmacenTotal = pAlmacenTotal + float(pAlmacen[Camion['nombre']]) * int(Camion['cajones'])
    
    dif = pCamionTotal - pAlmacenTotal
    
    print(f'Costo camion: {pCamionTotal}')
    print(f'Ganancia: {pAlmacenTotal}')
    if dif > 0:
        print(f'El negocio obtuvo una ganancia de: {pAlmacenTotal - pCamionTotal}')
    elif dif == 0:
        print(f'El balance dio 0')
    else:
        print(f'El negocio gano: {pAlmacenTotal - pCamionTotal}')

# Abro archivos
pCamion = leer_camion('../Data/camion.csv')
pAlmacen = leer_precios('../Data/precios.csv')

generar_informe(pCamion, pAlmacen)
    
    
    