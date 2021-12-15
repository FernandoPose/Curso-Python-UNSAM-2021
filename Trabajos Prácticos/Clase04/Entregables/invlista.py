# Ejercicio 4.5

def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida = [e] + invertida
    return invertida