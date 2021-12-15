# Ejercicio 3.20

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



#! Comienza el programa

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
nParque_1   = 'GENERAL PAZ'
nParque_2   = 'ANDES, LOS'
nParque_3   = 'CENTENARIO'

infoParque_1    = leer_parque(nArchivo, nParque_1)
infoParque_2    = leer_parque(nArchivo, nParque_2)
infoParque_3    = leer_parque(nArchivo, nParque_3)

contEjemplares_1  = contar_ejemplares(infoParque_1)
contEjemplares_2  = contar_ejemplares(infoParque_2)
contEjemplares_3  = contar_ejemplares(infoParque_3)

mCommon_1 = contEjemplares_1.most_common(5)
mCommon_2 = contEjemplares_2.most_common(5)
mCommon_3 = contEjemplares_3.most_common(5)

#? IMPRIME SIEMPRE LOS MISMOS VALORES. ALGO ESTA MAL.
print(f'{nParque_1:<35s} {nParque_2:<35s} {nParque_3:<35s}')
print(f'----------------------------------------------------------------------------------')

for i in range(5):
    print(f"{f'{mCommon_1[i][0]}: {mCommon_1[i][1]}':<35s} {f'{mCommon_2[i][0]}: {mCommon_2[i][1]}':<35s} {f'{mCommon_3[i][0]}: {mCommon_3[i][1]}':<35s}")

#print(f"  {f'${precio:0.2f}':>10s} ")   
