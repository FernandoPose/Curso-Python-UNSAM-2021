# Ejercicio 6.1

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):    
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m

#%% 
propagar([0,0,0,0,1]) #! Propaga 4 veces
propagar([0,0,1,0,0]) #! Propaga 2 veces
propagar([1,0,0,0,0]) #! Propaga 1 vez

#! 1: No causa error debido a que en la condición del if se tienen las condiciones
#!  : i<n-1 y i>0 con el enumerate que evitan caer fuera de los elementos de la lista.

#! 2: No genera la misma cantidad de repeticiones debido a que al encontrar un 1, hacia adelante
#!    el for de la función propagar_al_vecino() continua encenciendo hasta alcanzar la última posición.
#!    pero para atrás solo propaga a un único elemento pasado (enumerate va para adelante)

#! 3: a: n-1 veces puede repetirse. Dado que si todos son 0 solo se repite 1 vez.
#!    b: 
#!    c: 
