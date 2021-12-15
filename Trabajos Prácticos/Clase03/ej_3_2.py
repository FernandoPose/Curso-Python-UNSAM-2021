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