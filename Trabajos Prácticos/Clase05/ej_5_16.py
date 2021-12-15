# Ejercicio 5.16

import numpy as np
import random

figus_total = 670
cAlbum = np.arange(1, figus_total + 1)
paquete = random.choices(cAlbum, k = 5)

print(f'El paquete contiene las figuritas: {paquete[0]}, {paquete[1]}, {paquete[2]}, {paquete[3]} y {paquete[4]}')
