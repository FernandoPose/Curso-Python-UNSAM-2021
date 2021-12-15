# Ejercicio 12.8

import random
import numpy as np
import timeit as tt
import matplotlib.pyplot as plt 


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1
    return lista


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return lista


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v


def ord_burbujeo(lista):
    for i in range(len(lista)):
        for j in range(1, len(lista) - i):
            if lista[j-1] > lista[j]:
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return lista


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado


def generar_lista(N):
    lim_inf = 1
    lim_sup = 1000
    lista = list()
    for _ in range(1, N):
        lista.append(random.randint(lim_inf, lim_sup))
    return lista


def graficar_resultados(lenList, tiempos_insercion, tiempos_seleccion, tiempos_burbujeo, tiempos_mergeSort):
    
    plt.plot(lenList, tiempos_insercion, color='b', label = 'Inserción')
    plt.plot(lenList, tiempos_seleccion, color='g', label = 'Selección')
    plt.plot(lenList, tiempos_burbujeo, linestyle='--', color='r', label = 'Burbujeo')
    plt.plot(lenList, tiempos_mergeSort, color='m', label = 'Merge Sort')
    
    plt.xlabel('Largo lista')
    plt.ylabel('Tiempo de procesamiento')
    plt.title('Comparación de algoritmos - Complejidad')
    plt.legend()
    plt.show()

def experimento_timeit(listas, K):
    
    K = 256
    i = 1
    
    global lista

    tiempos_insercion = np.zeros(K)
    tiempos_seleccion = np.zeros(K)
    tiempos_burbujeo  = np.zeros(K)
    tiempos_mergeSort = np.zeros(K)

    for lista in listas:
        
        tiempos_insercion[i] = tt.timeit('ord_insercion(lista.copy())', number=(K-1), globals = globals()) 
        tiempos_seleccion[i] = tt.timeit('ord_seleccion(lista.copy())', number=(K-1), globals = globals()) 
        tiempos_burbujeo[i]  = tt.timeit('ord_burbujeo(lista.copy())', number=(K-1), globals = globals()) 
        tiempos_mergeSort[i] = tt.timeit('merge_sort(lista.copy())', number=(K-1), globals = globals()) 

        i += 1
    '''
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_burbujeo  = np.array(tiempos_burbujeo)
    tiempos_mergeSort = np.array(tiempos_mergeSort)
    '''
     
    return tiempos_insercion, tiempos_seleccion, tiempos_burbujeo, tiempos_mergeSort


def main():
    
    K = 256
        
    lenList = np.arange(1, K + 1, step=1)
    listas = list()
    
    for i in range(1, K):
        lista = []
        lista = generar_lista(lenList[i])
        listas.append(lista)
    
    (tiempos_insercion, tiempos_seleccion, tiempos_burbujeo, tiempos_mergeSort) = experimento_timeit(listas, K)
    
    graficar_resultados(lenList, tiempos_insercion, tiempos_seleccion, tiempos_burbujeo, tiempos_mergeSort)
    
    
if __name__ == '__main__':
    main()


