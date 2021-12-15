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