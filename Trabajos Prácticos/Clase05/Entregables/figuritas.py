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

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total     = 670
n_repeticiones  = 100

nVeces = [cuantas_figus(figus_total) for repeticion in range(n_repeticiones)]
print(f'Deben comprarse {np.mean(nVeces):<0.2f} en promedio para completar el álbum')
