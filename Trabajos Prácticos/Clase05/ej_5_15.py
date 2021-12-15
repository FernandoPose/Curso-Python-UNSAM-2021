# Ejercicio 5.15

import numpy as np
import random

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


figus_total     = 670
n_repeticiones  = 100

nVeces = [cuantas_figus(figus_total) for repeticion in range(n_repeticiones)]
print(f'Deben comprarse {np.mean(nVeces):<0.2f} en promedio para completar el álbum')
