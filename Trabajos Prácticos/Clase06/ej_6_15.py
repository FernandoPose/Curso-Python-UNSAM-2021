# Ejercicio 6.15

def insertar(lista, x):
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
    if pos == -1:           # si no lo encuentra, devuelvo pos e inserto dato 
        pos = izq
        lista.insert(pos, x)
    return pos

def main():
    lista_1 = [0,2,4,6]
    print(f'Test 1: Busco: 3 en {lista_1}, debe retornar: 2. La función retorna: {insertar(lista_1, 3)}. Lista nueva: {lista_1}')
    lista_2 = [0,2,4,6]
    print(f'Test 2: Busco: 4 en {lista_2}, debe retornar: 2. La función retorna: {insertar(lista_2, 4)}. Lista nueva: {lista_2}')
    

