# Ejercicio 4.16 y 4.17

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

def leer_arboles(nombre_archivo):
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        arboleada = [ { head:value  for head,value in zip(headers, row)} for row in rows]
        return arboleada


#! Comienza el programa

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
arboleada   = leer_arboles(nArchivo)

especie     = 'Jacarand??'

H   = [ float(arbol['altura_tot']) for arbol in arboleada if arbol['nombre_com'] == especie ]
hD  = [ (float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleada if arbol['nombre_com'] == especie ]

