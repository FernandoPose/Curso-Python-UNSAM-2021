# Ejercicio 5.4

import random

def suma_envido(n,m):
    if n >= 10:
        n = 0
    if m >= 10:
        m = 0
    return 20+n+m

N = 100000 # Número de experimentos

#! Armo la baraja
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos   = ['oro', 'copa', 'espada', 'basto']
naipes  = [(valor,palo) for valor in valores for palo in palos]

envidoAlto = 0

for i in range(N):

    valor   = []
    palo    = []
    nCartas = []
    
    cartas = random.sample(naipes, k = 3)
    for carta in cartas:
        valor.append(carta[0])
        palo.append(carta[1])
    
    lRepetidos = [item for item in set(palo) if palo.count(item) > 1]
    
    if len(lRepetidos) >= 1:
        [nCartas.append(carta) for carta in cartas if carta[1] == lRepetidos[0]]
        nCartas.sort()
        if 31 <= suma_envido(nCartas[0][0], nCartas[1][0]) <= 33:
            envidoAlto += 1          
                   
prob = envidoAlto / N
print(f'{N} Experimentos, de las cuales {envidoAlto} tienen envido > 31')
print(f'Probabilidad de obtener entre 31 y 33 de envido es: {prob:.6f}.')