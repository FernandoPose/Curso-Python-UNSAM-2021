# Ejercicio 5.6

from pprint import pprint
import random

N           = 99
mu          = 0 
sigma       = 0.2
medicion    = 37.5

resultados = []

for i in range(N):
    resultados.append(medicion + random.normalvariate(mu, sigma))

pprint(resultados)

print(f'Valor máximo: {max(resultados):.2f}')
print(f'Valor mínimo: {min(resultados):.2f}')
print(f'Promedio: {(sum(resultados)/len(resultados)):.2f}')

resultados.sort()
print(f'Mediana: {resultados[round(len(resultados)/2)]:.2f}')
