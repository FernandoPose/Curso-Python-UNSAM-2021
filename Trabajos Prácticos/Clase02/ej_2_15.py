# Ejercicio 2.15

import csv

def leer_camion(nombre_archivo):
    cCamion = []
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(file)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            cCamion.append(lote)
        return cCamion

cCamion = leer_camion('../Data/camion.csv')

print(cCamion)
