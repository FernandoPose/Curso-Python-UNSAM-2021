# Ejercicio 5.13

import numpy as np
import random

figus_total = 670

def crear_album(figus_total):    
    fTotal = np.zeros(figus_total, dtype=int)
    return fTotal

def album_incompleto(A):
    return (0 in A)

def comprar_figu(figus_total):
    figurita = random.randint(1, figus_total)
    return figurita

def cuantas_figus(figus_total):
    nAlbum  = crear_album(figus_total)
    while album_incompleto(nAlbum):
        nFigurita = comprar_figu(figus_total)
        nAlbum[nFigurita - 1] += 1
    return nAlbum.sum()





