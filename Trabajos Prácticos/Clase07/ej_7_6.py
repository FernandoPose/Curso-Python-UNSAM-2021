# Ejercicio 7.6

def sumar_enteros_1(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''   
    sum = 0 
    if (hasta > desde):
        for i in range(desde,hasta):
            sum +=i
        sum += hasta
    return sum


    
def sumar_enteros_2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    sum = 0 
    if (hasta > desde):
        pass
    return sum

