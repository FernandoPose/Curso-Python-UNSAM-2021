
import csv

def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, 
    determinando el parámetro select, que debe ser una lista de 
    nombres de las columnas a considerar.
    '''
    
    if (select != None) & (has_headers == False):
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    filas = csv.reader(lines)

    # Lee los encabezados del archivo    
    if has_headers:
        encabezados = next(filas)

    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios
    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    registros = []
        
    for nFila, fila in enumerate(filas, start=1):
        try:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
                
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
                
            if has_headers:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
            else:
                registro = []
                for columna in fila:
                    registro.append(columna)
                registro = tuple(registro)
                
            registros.append(registro)
        except ValueError as e:
            if silence_errors == False:
                print(f'Fila {nFila}: No puede convertir {fila}')
                print(f'Fila {nFila}: Motivo: {e}')
                
    return registros