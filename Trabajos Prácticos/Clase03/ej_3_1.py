# Ejercicio 3.1

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