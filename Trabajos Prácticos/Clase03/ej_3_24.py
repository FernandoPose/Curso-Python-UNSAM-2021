# Ejercicio 3.24

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

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = list()
    for row in lista_arboles:
        if row['nombre_com'] == especie:
            inclinaciones.append(int(row['inclinacio']))
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    tipoMaxIncl = dict()
    conjEspecies = especies(lista_arboles)
    for especie in conjEspecies:
        conjInclinaciones = obtener_inclinaciones(lista_arboles, especie)
        tipoMaxIncl[especie] = max(conjInclinaciones)
    claves  = list(tipoMaxIncl.keys())
    valores = list(tipoMaxIncl.values()) 
    especie = claves[valores.index(max(valores))]
    inclinacion = tipoMaxIncl[especie]
    return (especie, inclinacion)

def especie_promedio_mas_inclinado(lista_arboles):
    tipoPromIncl = dict()
    conjEspecies = especies(lista_arboles)
    for especie in conjEspecies:
        conjInclinaciones = obtener_inclinaciones(lista_arboles, especie)
        tipoPromIncl[especie] = sum(conjInclinaciones) / len(conjInclinaciones)
        
    claves  = list(tipoPromIncl.keys())
    valores = list(tipoPromIncl.values()) 
    
    maximo = valores.index(max(valores))

    return (claves[maximo], valores[maximo])

#! Comienza el programa

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'

nParque_1   = 'GENERAL PAZ'
nParque_2   = 'ANDES, LOS'
nParque_3   = 'CENTENARIO'

infoParque_1    = leer_parque(nArchivo, nParque_1)
infoParque_2    = leer_parque(nArchivo, nParque_2)
infoParque_3    = leer_parque(nArchivo, nParque_3)

(especie_1, promInclinacion_1) = especie_promedio_mas_inclinado(infoParque_1)
(especie_2, promInclinacion_2) = especie_promedio_mas_inclinado(infoParque_2)
(especie_3, promInclinacion_3) = especie_promedio_mas_inclinado(infoParque_3)

print(f'{nParque_1}: Especie: {especie_1} - Prom. Inclinación: {promInclinacion_1}')
print(f'{nParque_2}: Especie: {especie_2} - Prom. Inclinación: {promInclinacion_2}')
print(f'{nParque_3}: Especie: {especie_3} - Prom. Inclinación: {promInclinacion_3}')