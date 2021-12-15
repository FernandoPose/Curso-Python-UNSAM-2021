
import fileparse
from lote import Lote
import formato_tabla
from camion import Camion

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as lines:
        camion_dicts = fileparse.parse_csv(lines, 
                            select=['nombre','cajones','precio'],
                            types=[str, int, float])
    
    cCamion = [ Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(cCamion)
    
def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        lPrecios = fileparse.parse_csv(f, types=[str, float], has_headers = False)
    return lPrecios

def hacer_informe(pCamion, pAlmacen):
    pAlmacen = dict(pAlmacen)
    informe = list()
    for Camion in pCamion:
        registro    = ()
        registro    = (Camion.nombre, int(Camion.cajones), float(Camion.precio))
        cambio      = pAlmacen[Camion.nombre] - Camion.precio
        registro    = registro + (round(cambio,2),)
        informe.append(registro)
    return informe

def imprimir_informe(data_informe, formateador):
    ''' Imprime el informe '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
        
def informe_camion(archivo_camion, archivo_precios, fmt ='txt'):   
    # Leo los archivos con datos 
    cCamion  = leer_camion(archivo_camion)
    lPrecios = leer_precios(archivo_precios)
    # Creo los datos para hacer el informe
    informe  = hacer_informe(cCamion, lPrecios)
    # Imprimo el informe en el formato elegido por argumento
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)  
    
def main(args):
    if len(args) != 4:
        raise SystemExit(f'Uso adecuado: {args[0]} archivo_camion archivo_precios formato')
    informe_camion(args[1], args[2], args[3])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
