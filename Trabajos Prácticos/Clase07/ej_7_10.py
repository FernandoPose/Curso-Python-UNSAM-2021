# Ejercicio 7.10

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

caminatas   = []
cMaximos    = []

plt.figure()
plt.subplot(2,2,(1,2))
for i in range(12):
    pasos = randomwalk(N)
    caminatas.append(pasos)
    cMaximos.append(max(abs(pasos)))
    plt.plot(pasos)

camMaxima = caminatas[cMaximos.index(max(cMaximos))]
camMinima = caminatas[cMaximos.index(min(cMaximos))]

plt.title('12 Caminatas al azar')
plt.ylim([-600,600])
plt.xticks([])
plt.yticks([-500, 0, 500])

plt.subplot(2,2,3)
plt.plot(camMaxima)
plt.ylim([-600,600])
plt.xticks([])
plt.yticks([-500, 0, 500])
plt.title('La caminata que más se aleja')

plt.subplot(2,2,4)
plt.plot(camMinima)
plt.ylim([-600,600])
plt.xticks([])
plt.yticks([])
plt.title('La caminata que menos se aleja')

plt.show()