# Ejercicio 5.12

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


