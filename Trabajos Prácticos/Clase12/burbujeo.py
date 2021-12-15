# Ejercicio 12.2

def ord_burbujeo(lista):
    pasos = 0
    for i in range(len(lista)):
        for j in range(1, len(lista) - i):
            if lista[j-1] > lista[j]:
                lista[j-1], lista[j] = lista[j], lista[j-1]
            pasos = pasos + 1
    return pasos, lista


def main():
    
    lista_1 = [1, 2, -3, 8, 1, 5]
    print(f'Lista: {lista_1} - Ordenada: {ord_burbujeo(lista_1)[1]}')
    lista_2 = [1, 2, 3, 4, 5]
    print(f'Lista: {lista_2} - Ordenada: {ord_burbujeo(lista_2)[1]}')
    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    print(f'Lista: {lista_3} - Ordenada: {ord_burbujeo(lista_3)[1]}')
    lista_4 = [10, 8, 6, 2, -2, -5]
    print(f'Lista: {lista_4} - Ordenada: {ord_burbujeo(lista_4)[1]}')
    lista_5 = [2, 5, 1, 0]
    print(f'Lista: {lista_5} - Ordenada: {ord_burbujeo(lista_5)[1]}')

if __name__ == '__main__':
    main()
