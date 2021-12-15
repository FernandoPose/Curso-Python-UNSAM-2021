# Ejercicio 11.11

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e: 
            return True
        if e in lista[:medio]:
            return bbinaria_rec(lista[:medio], e)
        else:
            return bbinaria_rec(lista[medio:], e)
    return res


def main():
    lista = [1, 2, 4, 5, 7, 8, 9, 11, 12, 14, 15, 17, 20]
    print(bbinaria_rec(lista, 9))
    print(bbinaria_rec(lista, 10))
    print(bbinaria_rec(lista, 1))
    print(bbinaria_rec(lista, 20))

if __name__ == '__main__':
    main()