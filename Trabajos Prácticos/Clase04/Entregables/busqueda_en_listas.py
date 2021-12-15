# Ejercicio 4.3 y 4.4

def buscar_u_elemento(lista, e):
    pos = -1  
    for i, z in enumerate(lista): 
        if z == e:   
            pos = i   
    return pos

def buscar_n_elemento(lista, e):
    cant = 0
    for i, z in enumerate(lista): 
        if z == e:   
            cant += 1   
    return cant

def maximo(lista):
    m = lista[0]
    for e in lista: 
        if e > m:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    for e in lista: 
        if e < m:
            m = e
    return m
