# Ejercicio 2.14


def obtener_geringoso(vCadena):
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
    return nCadena

def diccionario_geringoso(pLista):
    diccionario = dict()
    for p in pLista:
        pConvertida = obtener_geringoso(p)
        diccionario[p] = pConvertida
    return diccionario


pEvaluacion = ['banana', 'manzana', 'mandarina']
pResultado = diccionario_geringoso(pEvaluacion)
for k, v in pResultado.items():
        print(k, '=', v)



