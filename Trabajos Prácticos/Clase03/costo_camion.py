# costo_camion.py

import csv

def costo_camion(nombre_archivo):
    cTotal = 0
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for nFila, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                nCajones = int(record['cajones'])
                precio   = float(record['precio'])
                cTotal += nCajones * precio
            except ValueError:
                print(f'Fila {nFila}: No puede interpretar: {row}') 
        return cTotal

costo = costo_camion('/Users/fpose/Documents/Doctorado/Cursos/Curso-Python-TP/Data/fecha_camion.csv')

print(f'Costo total: {costo}')