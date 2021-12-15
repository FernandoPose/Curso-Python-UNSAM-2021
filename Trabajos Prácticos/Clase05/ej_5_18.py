# Ejercicio 5.18

import numpy as np
import random


def crear_album(figus_total):    
    fTotal = np.zeros(figus_total, dtype=int)
    return fTotal

def album_incompleto(A):
    return (0 in A)

def comprar_paquete(figus_total, figus_paquete):
    cAlbum = np.arange(1, figus_total + 1)
    paquete = random.choices(cAlbum, k = figus_paquete)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    nPaquetes = 0 
    nAlbum = crear_album(figus_total)
    while album_incompleto(nAlbum):
        Paquete = comprar_paquete(figus_total, figus_paquete)
        nPaquetes += 1
        for figurita in Paquete:
            nAlbum[figurita - 1] += 1
    return nAlbum.sum()