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