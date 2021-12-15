# Ejercicio 4.6

def propagar(cFosforos): 
    for i, estado in enumerate(cFosforos):
        if estado == 1 and i < len(cFosforos)-1 and cFosforos[i + 1] == 0:
                cFosforos[i + 1] = 1    
    
    cFosforos = invertir_lista(cFosforos)
    
    for i, estado in enumerate(cFosforos):
        if estado == 1 and i < len(cFosforos)-1 and cFosforos[i + 1] == 0:
                cFosforos[i + 1] = 1 
    
    cFosforos = invertir_lista(cFosforos)
    
    return cFosforos

def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida = [e] + invertida
    return invertida


