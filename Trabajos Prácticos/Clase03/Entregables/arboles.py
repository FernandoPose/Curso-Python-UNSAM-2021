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

#%% Ejercicio 3.18

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
nParque     = 'GENERAL PAZ'

infoParque = leer_parque(nArchivo, nParque)


#%%
# Ejercicio 3.19

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
nParque     = 'GENERAL PAZ'

infoParque      = leer_parque(nArchivo, nParque)
conjEspecies    = especies(infoParque)


#%%
# Ejercicio 3.20

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

#%%
# Ejercicio 3.21

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

#%%
# Ejercicio 3.22

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'
nParque_1   = 'GENERAL PAZ'
nParque_2   = 'ANDES, LOS'
nParque_3   = 'CENTENARIO'

infoParque_1    = leer_parque(nArchivo, nParque_1)
infoParque_2    = leer_parque(nArchivo, nParque_2)
infoParque_3    = leer_parque(nArchivo, nParque_3)

especie         =  'Jacarandá'

conjInclinaciones_1  = obtener_inclinaciones(infoParque_1, especie)
conjInclinaciones_2  = obtener_inclinaciones(infoParque_2, especie)
conjInclinaciones_3  = obtener_inclinaciones(infoParque_3, especie)



#%%
# Ejercicio 3.23

nArchivo    = '../Data/arbolado-en-espacios-verdes.csv'

nParque_1   = 'GENERAL PAZ'
nParque_2   = 'ANDES, LOS'
nParque_3   = 'CENTENARIO'

infoParque_1    = leer_parque(nArchivo, nParque_1)
infoParque_2    = leer_parque(nArchivo, nParque_2)
infoParque_3    = leer_parque(nArchivo, nParque_3)

(especie_1, inclinacion_1) = especimen_mas_inclinado(infoParque_1)
(especie_2, inclinacion_2) = especimen_mas_inclinado(infoParque_2)
(especie_3, inclinacion_3) = especimen_mas_inclinado(infoParque_3)

print(f'{nParque_1}: Especie: {especie_1} - Inclinación: {inclinacion_1}')
print(f'{nParque_2}: Especie: {especie_2} - Inclinación: {inclinacion_2}')
print(f'{nParque_3}: Especie: {especie_3} - Inclinación: {inclinacion_3}')


#%%
# Ejercicio 3.24

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