# Ejercicio 2.17

import csv

def leer_precios(nombre_archivo):
    lPrecios = {}
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        try:
            for nombre, precio in rows:
                lPrecios[nombre] = float(precio)
        except ValueError:
            pass  
    return lPrecios

lPrecios = leer_precios('../Data/precios.csv')
print(lPrecios)