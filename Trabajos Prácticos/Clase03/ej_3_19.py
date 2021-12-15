# Ejercicio 3.19

import csv

def leer_parque(nombre_archivo, parque):
    info = []
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                if row[10] == parque:
                    record = dict(zip(headers, row))
                    info.append(record)
            except ValueError:
                pass
        return info

def especies(lista_arboles):
    especies = set()
    for row in lista_arboles:
        especies.add(row['nombre_com'])
    return especies


#! Comienza el programa

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
nParque     = 'GENERAL PAZ'

infoParque      = leer_parque(nArchivo, nParque)
conjEspecies    = especies(infoParque)