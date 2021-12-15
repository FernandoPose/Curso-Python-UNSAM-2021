# Ejercicio 3.16

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

# Abro archivos
pCamion = leer_camion('../Data/camion.csv')
pAlmacen = leer_precios('../Data/precios.csv')

informe = hacer_informe(pCamion, pAlmacen)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
cadena  = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
sep     = f'---------- ---------- ---------- ----------'
print(cadena)
print(sep)

#* Forma 1: Usando %
#for r in informe:
#    print('%10s %10d %10.2f %10.2f' % r)
    
#* Forma 2: Usando f-strings
for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {f'${precio:0.2f}':>10s} {cambio:>10.2f}")   
