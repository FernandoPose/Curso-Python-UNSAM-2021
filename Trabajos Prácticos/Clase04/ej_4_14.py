# Ejercicio 4.14

import csv

nFile   = '../Data/dowstocks.csv'

file    = open(nFile)
rows    = csv.reader(file)
headers = next(rows)
row     = next(rows)

types = [str, float, str, str, float, float, float, float, int]

converted = [ func(val) for func, val in zip(types, row)]
record    = dict(zip(headers, converted))
print(record)

# Bonus: ¿Cómo modificarías este ejemplo para transformar la fecha (date) en una tupla como (6, 11, 2007)?