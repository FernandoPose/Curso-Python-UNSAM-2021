# Ejercicio 2.10


import csv
import sys

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


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

#costo = costo_camion(nombre_archivo)
#print('Costo total:', costo)