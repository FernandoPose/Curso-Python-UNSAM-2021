# Ejercicio 12.5

import random
import numpy as np
import matplotlib.pyplot as plt 

import merge_sort as ms
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

def graficar_resultados(lenList, pasos_insercion, pasos_seleccion, pasos_burbujeo, pasos_mergeSort):
    
    plt.plot(lenList, pasos_insercion, color='b', label = 'Inserción')
    plt.plot(lenList, pasos_seleccion, color='g', label = 'Selección')
    plt.plot(lenList, pasos_burbujeo, linestyle='--', color='r', label = 'Burbujeo')
    plt.plot(lenList, pasos_mergeSort, color='m', label = 'Merge Sort')
    
    plt.xlabel('Largo lista')
    plt.ylabel('Número de comparaciones')
    plt.title('Comparación de algoritmos - Complejidad')
    plt.legend()
    plt.show()

def main():
    
    K = 256
    
    lenList = np.arange(1, K + 1, step=1)
    
    pasos_insercion = np.zeros(K)
    pasos_seleccion = np.zeros(K)
    pasos_burbujeo  = np.zeros(K)
    pasos_mergeSort = np.zeros(K)
    
    for i in range(K):
        lista = generar_lista(lenList[i])
        pasos_insercion[i], _ = ord_insercion(lista.copy())
        pasos_seleccion[i], _ = ord_seleccion(lista.copy())
        pasos_burbujeo[i],  _ = ord_burbujeo(lista.copy())
        pasos_mergeSort[i], _ = ms.merge_sort(lista.copy())
    
    graficar_resultados(lenList, pasos_insercion, pasos_seleccion, pasos_burbujeo, pasos_mergeSort)
    
    
if __name__ == '__main__':
    main()