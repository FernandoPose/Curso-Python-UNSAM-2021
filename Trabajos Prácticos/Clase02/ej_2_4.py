# Ejercicio 2.4

import gzip

with gzip.open('../Data/camion.csv.gz', 'rt') as file:
    #? Nombre_Fruta - Precio/Cajón
    for line in file:
        print(line, end = '')