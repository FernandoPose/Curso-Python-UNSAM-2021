# Ejercicio 8.5

import os
import sys
import pprint

def buscar_archivos(directorio):
    lArchivos = list()
    for root, _, files in os.walk(directorio):
        for name in files:
            archivo = os.path.join(root, name)
            if archivo[-4:] == '.png':
                lArchivos.append(archivo)
    return lArchivos

def imprimir_lista(lArchivos):
    pprint.pprint(lArchivos)

def main(directorio):
    lArchivos = buscar_archivos(directorio)
    imprimir_lista(lArchivos)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('ERROR: Debe ingresar un nombre del directorio.')