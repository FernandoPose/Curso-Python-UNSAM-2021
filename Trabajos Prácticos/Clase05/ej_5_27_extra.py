# Ejercicio 5.27 extra

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
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
        arboleda = [ { head:value  for head,value in zip(headers, row)} for row in rows]
        return arboleda

def medidas_de_especies(especies, arboleda):
    dicEspecies = { especie:[ (float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleda if arbol['nombre_com'] == especie ] for especie in especies }
    return dicEspecies
    
def histograma_Especie_Jacaranda():
    nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
    arboleada   = leer_arboles(nArchivo)
    especie = 'Jacarandá'
    altos = [ float(arbol['altura_tot']) for arbol in arboleada if arbol['nombre_com'] == especie ]
    plt.hist(altos, bins = 50)
    plt.xlabel('Altura [m]')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de alturas')
    plt.show()

def scatterplot_hD_Jacaranda():
    nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
    arboleada   = leer_arboles(nArchivo)
    especie = 'Jacarandá'
    hD  = np.array([ (float(arbol['altura_tot']), float(arbol['diametro']))  for arbol in arboleada if arbol['nombre_com'] == especie ])
    d = hD[:, 0]
    h = hD[:, 1]
    colors = np.random.rand(len(d))
    plt.scatter(d, h, s=10, c=colors, alpha=0.5)
    plt.xlabel('diametro (cm)')
    plt.ylabel('alto (m)')
    plt.title('Relación diámetro-alto para Jacarandás')
    plt.show()
   
def scatterplot_hD_especies():

    nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda    = leer_arboles(nArchivo)
    especies    = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    colores     = ['blue', 'red', 'green']
    dicEspecies = medidas_de_especies(especies, arboleda)

    plt.figure()
    
    for cont, especie in enumerate(especies):
        medidas = np.array(dicEspecies[especies[cont]])
        d = medidas[:, 0]    
        h = medidas[:, 1]
        plt.scatter(d, h, s=10, c=colores[cont], alpha=0.5, label = especies[cont] )
        plt.xlabel('diametro (cm)')
        plt.ylabel('alto (m)')
        plt.title(f'Relación diámetro-alto')
        plt.xlim(0,70)
        plt.ylim(0,300)
    
    plt.legend()
    plt.show()
