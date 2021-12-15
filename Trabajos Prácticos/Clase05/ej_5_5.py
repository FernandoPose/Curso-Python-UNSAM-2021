# Ejercicio 5.5

import random
import math

N = 100000
cPuntos = 0

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

for cont in range(N):
    x, y = generar_punto()
    if (x**2 + y**2) < 1:
        cPuntos += 1

aprox = 4 * (cPuntos / N)
print(f'El valor de pi es: {math.pi:0.10f}. El resultado aproximado es: {aprox:0.10f}')