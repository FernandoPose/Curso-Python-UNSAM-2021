# Ejercicio 7.8

def valor_absoluto(n):
    ''' Calcula el valor absoluto de n.
    Pre: n debe ser un número.
    Pos: Devuelve n con signo positivo.
    '''   
    
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):
    ''' Calcula la suma de todos los números pares que se encuentran en el 
        la lista l.
        Pre: l debe ser una lista de números enteros.
        Pos: Devuelve la suma de números pares
    '''  
    
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

# Invariante de ciclo: variable res: Contiene el valor de la suma de elementos de la parte de la lista que ya fue analizada.

def veces(a, b):
    ''' Suma b veces el número a
        Pre: a y b deben ser números.
        Pos: Devuelve un número.
    ''' 
    
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

# Invariante de ciclo: variable res. Arranca en 0 y contiene la suma de la n veces entre 0 y b del número a

def collatz(n):
    ''' Conjetura de Collatz: dado un número n ingresado como parámetro, la función
        calcula el número de elementos en la sucesión hasta llegar a 1 incluido.
        Pre: n debe ser un número entero positivo.
        Pos: Devuelve un número entero positivo obtenido a partir de la cantidad de repeticiones
             necesarias para alcanzar el 1.
    ''' 

    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

# Invariante de ciclo: variable res: Contiene un valor que resulta de la suma entre 0 y el número de pasos que lleva el algoritmo
# recoriendo hasta llegar a 1.