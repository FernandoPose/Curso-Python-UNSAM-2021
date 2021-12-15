# Ejercicio 7.5

from fileparse import parse_csv

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        cCamion = parse_csv(f, types=[str, int, float])
    return cCamion
    
def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        lPrecios = parse_csv(f, types=[str, float], has_headers = False)
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
        
def main(parametros):
    camion  = parametros[1]
    precios = parametros[2]

    cCamion  = leer_camion(camion)
    lPrecios = leer_precios(precios)
    informe  = hacer_informe(cCamion, lPrecios)
    imprimir_informe(informe)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    main(sys.argv)