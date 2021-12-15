# Ejercicio 2.16

import csv

def leer_camion(nombre_archivo):
    cCamion = []
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(file)
        for nombre, cajones, precio in rows:
            lote = {'nombre':nombre, 'cajones':int(cajones), 'precio':float(precio)}
            cCamion.append(lote)
        return cCamion

cCamion = leer_camion('../Data/camion.csv')

print(cCamion)