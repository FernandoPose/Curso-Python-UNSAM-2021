# Ejercicio 5.17

import numpy as np
import random

def comprar_paquete(figus_total, figus_paquete):
    cAlbum = np.arange(1, figus_total + 1)
    paquete = random.choices(cAlbum, k = figus_paquete)
    return paquete

figus_total = 670
figus_paquete = 5

paquete = comprar_paquete(figus_total, figus_paquete)

print(f'El paquete contiene las figuritas: {paquete[0]}, {paquete[1]}, {paquete[2]}, {paquete[3]} y {paquete[4]}')

