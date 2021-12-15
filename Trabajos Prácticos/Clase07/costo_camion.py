import csv

def costo_camion(nombre_archivo):
    nFila = 1
    cTotal = 0
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(file)
        for row in rows:
            try:
                cTotal = cTotal + int(row[1]) * float(row[2])
                nFila = nFila + 1
            except ValueError:
                print(f'Falta de dato en fila {nFila + 1}')
                nFila = nFila + 1    
        return cTotal

def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    camion  = parametros[1]
    costo = costo_camion(camion)
    print(f'Costo total: {costo}')

if __name__ == '__main__':
    import sys
    main(sys.argv)
    

