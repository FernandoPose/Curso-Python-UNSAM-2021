# Ejercicio 3.21

from collections import Counter
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

def contar_ejemplares(lista_arboles):
    contEjemplares = Counter()
    for row in lista_arboles:
        
        contEjemplares[row['nombre_com']] += 1
    return contEjemplares

def obtener_alturas(lista_arboles, especie):
    alturas = list()
    for row in lista_arboles:
        if row['nombre_com'] == especie:
            alturas.append(float(row['altura_tot']))
    return alturas
    
    
#! Comienza el programa

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
nParque_1   = 'GENERAL PAZ'
nParque_2   = 'ANDES, LOS'
nParque_3   = 'CENTENARIO'

infoParque_1    = leer_parque(nArchivo, nParque_1)
infoParque_2    = leer_parque(nArchivo, nParque_2)
infoParque_3    = leer_parque(nArchivo, nParque_3)

especie         =  'Jacarandá'

conjAlturas_1  = obtener_alturas(infoParque_1, especie)
conjAlturas_2  = obtener_alturas(infoParque_2, especie)
conjAlturas_3  = obtener_alturas(infoParque_3, especie)

aux = 'Media'
aMax = 'max'
aProm = 'prom'

print(f' {aux:<20s} {nParque_1:<20s} {nParque_2:<20s} {nParque_3:<20s}')
print(f'--------------------------------------------------------------------------')
print(f'{aMax:<20s}  {max(conjAlturas_1):<20.2f} {max(conjAlturas_2):<20.2f} {max(conjAlturas_3):<20.2f} ')
print(f'{aProm:<21s} {(sum(conjAlturas_1)/len(conjAlturas_1)):<20.2f} {(sum(conjAlturas_2)/len(conjAlturas_2)):<21.2f} {(sum(conjAlturas_3)/len(conjAlturas_3)):<21.2f} ')

