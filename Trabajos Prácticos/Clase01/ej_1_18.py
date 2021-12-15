# Ejercicio 1.18

vCadena = 'Geringoso'
nCadena = ' '

for c in vCadena:
    
    if c == 'a':
        nCadena = nCadena + c + 'p' + c
    elif c == 'e':
        nCadena = nCadena + c + 'p' + c
    elif c == 'i':
        nCadena = nCadena + c + 'p' + c
    elif c == 'o':
        nCadena = nCadena + c + 'p' + c
    elif c == 'u':
        nCadena = nCadena + c + 'p' + c
    else:
        nCadena = nCadena + c
    
print('Nueva cadena:', nCadena)