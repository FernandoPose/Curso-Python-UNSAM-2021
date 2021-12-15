# Ejercicio 4.1

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

#! El error esta en:  invertida.append (lista.pop(i))
#! En ese momento, a 'invertida' se le esta asignando un valor
#! Que estoy sacando de la lista, modificando así, la lista.
