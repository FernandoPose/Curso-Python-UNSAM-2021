# Ejercicio 4.4

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

print('Ejercicio 4.4 - Parte A:')
print(f' Test 1: Valor esperado: {max([1,2,7,2,3,4])}  - Valor obtenido: {maximo([1,2,7,2,3,4])}')
print(f' Test 2: Valor esperado: {max([1,2,3,4])}  - Valor obtenido: {maximo([1,2,3,4])}')
print(f' Test 3: Valor esperado: {max([-5,4])}  - Valor obtenido: {maximo([-5,4])}')
print(f' Test 4: Valor esperado: {max([-5,-4])} - Valor obtenido: {maximo([-5,-4])}')

print('Ejercicio 4.4 - Parte B:')
print(f' Test 1: Valor esperado: {min([1,2,7,2,3,4])}  - Valor obtenido: {minimo([1,2,7,2,3,4])}')
print(f' Test 2: Valor esperado: {min([1,2,3,4])}  - Valor obtenido: {minimo([1,2,3,4])}')
print(f' Test 3: Valor esperado: {min([-5,4])}  - Valor obtenido: {minimo([-5,4])}')
print(f' Test 4: Valor esperado: {min([-5,-4])}  - Valor obtenido: {minimo([-5,-4])}')
