# Ejercicio 4.12

import csv

nFile = '../Data/camion.csv'

types = [str, int, float]

file    = open(nFile)
rows    = csv.reader(file)
headers = next(rows)
row     = next(rows)

#print(row)

#converted = []
#for func, val in zip(types, row):
#    converted.append(func(val))
#
#print(converted[1] * converted[2])

converted = [ func(val) for func, val in zip(types, row) ]
print(converted[1] * converted[2])

