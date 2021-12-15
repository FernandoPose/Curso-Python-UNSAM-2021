# Ejercicio 5.2

from collections import Counter
import random


def tirar(tirada):
    cDados = 5 - len(tirada)
    for i in range(cDados):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    if len(set(tirada)) == 1:
        return True
    else:
        return False
    

N = 100000
#N = 1000000

cGenerala   = 0

for pruebas in range(N):
    dados = []
    for n in range(3):
        dados = tirar(dados)
        if es_generala(dados):
            cGenerala += 1
            break
        else:
            if len(set(dados)) != 1:
                aux = []
                [aux.append(Counter(list(dados)).most_common()[0][0]) for i in range(Counter(list(dados)).most_common()[0][1])]
                dados = aux
                
                
prob = cGenerala / N
print(f'Tiré {N} veces, de las cuales {cGenerala} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')