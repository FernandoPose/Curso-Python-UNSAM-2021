# Ejercicio 5.9

from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import random


temperaturas = np.load('../Data/Temperaturas.npy')

plt.hist(temperaturas,bins=15)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.