# Ejercicio 3.5

#   Ejercicio 3.4.  Función suma(), nuevamente tiene errores de alcance
#   Comentario: Se detectaron los siguientes errores:
#       1) Al avanzar en el bucle for y cambiar el valor de registro, se cambia en la lista también dado
#          que el valor de registro esta agregado a la lista camión y no es una copia lo que se agrega en la lista.
#          El error se soluciona: creando un nuevo diccionario al comienzo del ciclo.


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

