# Ejercicio 4.3

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

print('Ejercicio 4.3 - Parte A:')
print(f' Test 1: Valor esperado: 0  - Valor obtenido: {buscar_u_elemento([1,2,3,2,3,4],1)}')
print(f' Test 2: Valor esperado: 3  - Valor obtenido: {buscar_u_elemento([1,2,3,2,3,4],2)}')
print(f' Test 3: Valor esperado: 4  - Valor obtenido: {buscar_u_elemento([1,2,3,2,3,4],3)}')
print(f' Test 4: Valor esperado: -1 - Valor obtenido: {buscar_u_elemento([1,2,3,2,3,4],5)}')

print('Ejercicio 4.3 - Parte B:')
print(f' Test 1: Valor esperado: 1  - Valor obtenido: {buscar_n_elemento([1,2,3,2,3,4],1)}')
print(f' Test 2: Valor esperado: 2  - Valor obtenido: {buscar_n_elemento([1,2,3,2,3,4],2)}')
print(f' Test 3: Valor esperado: 3  - Valor obtenido: {buscar_n_elemento([3,2,3,2,3,4],3)}')
print(f' Test 4: Valor esperado: 0  - Valor obtenido: {buscar_n_elemento([1,2,3,2,3,4],5)}')
