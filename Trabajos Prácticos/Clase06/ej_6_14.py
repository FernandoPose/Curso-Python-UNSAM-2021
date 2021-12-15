# Ejercicio 6.14

def donde_insertar(lista, x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            return pos
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        pos = izq
    return pos

def main():
    print(f'Test 1: Busco: 3 en [0,2,4,6], debe retornar: 2. La función retorna: {donde_insertar([0,2,4,6], 7)}')
    print(f'Test 2: Busco: 4 en [0,2,4,6], debe retornar: 2. La función retorna: {donde_insertar([0,2,4,6], 4)}')