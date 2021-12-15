#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo semántico y estaba ubicado la línea 14.
#    Lo corregí cambiando el else por elif i==n para que recorra la palabra entera
#    antes de decir si la palabra contiene o no "a"
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        elif i==n:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')



#%%
# Ejercicio 3.2

#   Ejercicio 3.2. Función tiene_a(), nuevamente tiene errores de sintaxis.
#   Comentario: Se detectaron los siguientes errores:
#       1) Faltan 2 puntos en la declaración de la función.
#       2) Faltan 2 puntos en el while.
#       3) Falta un = en la comparación del if y los 2 puntos.
#       4) Esta mal escrito el retorno en caso de que no contenga a (falso por false)

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3

#   Ejercicio 3.3.  Función tiene_uno(), nuevamente tiene errores de tipo de dato
#   Comentario: Se detectaron los siguientes errores:
#       1) No puede calcularse len() de un número entero. Cambio expresión a str.

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


#%%
# Ejercicio 3.4

#   Ejercicio 3.4.  Función suma(), nuevamente tiene errores de alcance
#   Comentario: Se detectaron los siguientes errores:
#       1) La función no retorna el valor de la suma 'c'


def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


#%%
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

