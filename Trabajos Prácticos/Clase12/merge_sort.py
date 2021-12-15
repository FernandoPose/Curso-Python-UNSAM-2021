import random

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
       
    if len(lista) < 2:
        lista_nueva = lista
        pasos = 0 
    else:
        pasos = 0 
        medio = len(lista) // 2
        pasos_izq, izq = merge_sort(lista[:medio])
        pasos_der, der = merge_sort(lista[medio:])
        pasos_merge, lista_nueva = merge(izq, der)
        pasos = pasos_izq + pasos_der + pasos_merge
    return pasos,lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones = 0 
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        
        comparaciones = comparaciones + 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return comparaciones, resultado