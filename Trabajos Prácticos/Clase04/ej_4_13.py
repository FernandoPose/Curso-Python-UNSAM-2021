# Ejercicio 4.13

import csv

nFile = '../Data/camion.csv'

types = [str, int, float]

file    = open(nFile)
rows    = csv.reader(file)
headers = next(rows)
row     = next(rows)

# converted   = [ func(val) for func, val in zip(types, row) ]
# dictionary  = dict(zip(headers, converted)) 

dictionary = { name:func(val) for name, func, val in zip(headers, types, row) }

print(dictionary)

