# Ejercicio 12.4

import random
import numpy as np

from ord_insercion import ord_insercion
from ord_seleccion import ord_seleccion
from burbujeo import ord_burbujeo

def generar_lista(N):
    lim_inf = 1
    lim_sup = 1000
    lista = list()
    for _ in range(N):
        lista.append(random.randint(lim_inf, lim_sup))
    return lista


def main():
    
    N = 10
    K = 100
    
    pasos_insercion = np.zeros(K)
    pasos_seleccion = np.zeros(K)
    pasos_burbujeo  = np.zeros(K)
    
    for i in range(K):
        lista = generar_lista(N)
        pasos_insercion[i], _ = ord_insercion(lista.copy())
        pasos_seleccion[i], _ = ord_seleccion(lista.copy())
        pasos_burbujeo[i], _  = ord_burbujeo(lista.copy())
    
    print(f'Con algoritmo de insercion se necesitaron: {pasos_insercion.mean()} comparaciones.')
    print(f'Con algoritmo de selección se necesitaron: {pasos_seleccion.mean()} comparaciones.')
    print(f'Con algoritmo de burbujeo  se necesitaron: {pasos_burbujeo.mean()} comparaciones.')
    
if __name__ == '__main__':
    main()