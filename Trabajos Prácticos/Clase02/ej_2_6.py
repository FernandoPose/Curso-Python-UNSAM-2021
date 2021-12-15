# Ejercicio 2.6

from typing import runtime_checkable


def costo_camion(nombre_archivo):
    
    cTotal = 0
    with open(nombre_archivo, 'rt') as file:
        headers = next(file)
        for line in file:
            row = line.split(',')
            cTotal = cTotal + int(row[1]) * float(row[2])
        return cTotal

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)


