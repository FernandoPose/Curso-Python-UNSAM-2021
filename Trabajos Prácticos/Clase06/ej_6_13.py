# Ejercicio 6.13

def buscar_u_elemento(lista, e):
    
    pos = -1  
    lista = sorted(lista)
    for i, z in enumerate(lista): 
        if z <= e:
            if z == e:   
                pos = i  
        else:
            break 
    return pos