# Ejercicio 5.3

import random

N           = 100000 # Número de experimentos
cPersonas   = 30     # Cantidad de personas c/u experimento
cRepetidos  = 0

dias        = list(range(365))

for i in range(N):
    dGenerados = random.choices(dias, k = cPersonas)
    lRepetidos = [item for item in set(dGenerados) if dGenerados.count(item) > 1]
    if len(lRepetidos) >= 1:
        cRepetidos += 1

prob = cRepetidos / N
print(f'{N} Experimentos, de las cuales {cRepetidos} cumplen el mismo día')
print(f'Podemos estimar la probabilidad de que dos personas cumplen el mismo dia: {prob:.6f}.')