# Ejercicio 2.7

def buscar_precio(fruta):
    pFruta = 0
    with open('../Data/precios.csv', 'rt') as file:
        #? Nombre_Fruta - Precio/Cajón
        for line in file:
            row = line.split(',')
            if row[0] == fruta:
                pFruta = float(row[1])
        if pFruta != 0:
            print(f'El precio de un cajón de {fruta} es: {pFruta}')
        else:
            print(f'{fruta} no figura en el listado de precios')
    return pFruta

buscar_precio('Frambuesa')
buscar_precio('Kale')
