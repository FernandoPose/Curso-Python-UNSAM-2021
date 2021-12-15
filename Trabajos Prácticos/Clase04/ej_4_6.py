# Ejercicio 4.6

def propagar(cFosforos): 
    for i, estado in enumerate(cFosforos):
        if estado == 1 and i < len(cFosforos)-1 and cFosforos[i + 1] == 0:
                cFosforos[i + 1] = 1       
    return cFosforos

def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida = [e] + invertida
    return invertida


cFosforos = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
nFosforos = [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]

cFosforos = propagar(cFosforos)
cFosforos = propagar(invertir_lista(cFosforos))
print(f' Test 1: Valor esperado: {nFosforos}  - Valor obtenido: {invertir_lista(cFosforos)}')

cFosforos = [ 0, 0, 0, 1, 0, 0]
nFosforos = [ 1, 1, 1, 1, 1, 1]

cFosforos = propagar(cFosforos)
cFosforos = propagar(invertir_lista(cFosforos))
print(f' Test 2: Valor esperado: {nFosforos}  - Valor obtenido: {invertir_lista(cFosforos)}')