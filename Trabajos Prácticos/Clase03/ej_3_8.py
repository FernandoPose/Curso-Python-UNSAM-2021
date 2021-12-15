# Ejercicio 3.8

import csv

def costo_camion(nombre_archivo):
    cTotal = 0
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(file)
        for nFila, row in enumerate(rows, start = 1):
            try:
                cTotal = cTotal + int(row[1]) * float(row[2])
            except ValueError:
                print(f'Fila {nFila}: No puede interpretar: {row}') 
        return cTotal

costo = costo_camion('../Data/missing.csv')

print(f'Costo total: {costo}')
