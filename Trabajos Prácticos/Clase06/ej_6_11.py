# Ejercicio 6.11

from fileparse import parse_csv

def leer_camion(nombre_archivo):
    cCamion = parse_csv(nombre_archivo, types=[str, int, float])
    return cCamion
    
def leer_precios(nombre_archivo):
    lPrecios = parse_csv(nombre_archivo, types=[str, float], has_headers = False)
    return lPrecios

def hacer_informe(pCamion, pAlmacen):
    pAlmacen = dict(pAlmacen)
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
