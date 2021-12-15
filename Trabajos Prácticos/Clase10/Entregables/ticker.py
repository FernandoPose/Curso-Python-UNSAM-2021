# ticker.py

from vigilante import vigilar
import informe_final
import formato_tabla
import sys
import csv

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, str, str])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
        
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def ticker(camion_file, log_file, fmt):
    
    camion = informe_final.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    #filas = filtrar_datos(filas, camion)
    filas = (fila for fila in filas if fila['nombre'] in camion)

    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    
    while True:
        for fila in filas:
            formateador.fila(fila.values())

def main(archivo_camion, archivo_log, fmt):
    ticker(archivo_camion, archivo_log, fmt)
        
if __name__ == '__main__':
    try: 
        if len(sys.argv) == 3: 
            archivo_camion = sys.argv[1]
            archivo_log = sys.argv[2]
            fmt = sys.argv[3]
        else:
            archivo_camion = '../Data/camion.csv'
            archivo_log = '../Data/mercadolog.csv'
            fmt = 'txt'
    except FileNotFoundError:
        print(f'No existen los archivos en el ordenador')
    main(archivo_camion, archivo_log, fmt)
    


