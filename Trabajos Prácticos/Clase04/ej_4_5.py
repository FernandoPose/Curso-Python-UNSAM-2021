# Ejercicio 4.5

def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida = [e] + invertida
    return invertida

print(f' Test 1: Valor esperado: {[5, 4, 3, 2, 1]}  - Valor obtenido: {invertir_lista([1, 2, 3, 4, 5])}')
aux = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(f" Test 1: Valor esperado: ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']  - Valor obtenido: {invertir_lista(aux)}")


