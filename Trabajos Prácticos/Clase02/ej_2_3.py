# Ejercicio 2.3

pNaranja = 0

with open('../Data/precios.csv', 'rt') as file:
    #? Nombre_Fruta - Precio/Cajón
    for line in file:
        row = line.split(',')
        if row[0] == 'Naranja':
            pNaranja = float(row[1])
    
    print(f'El precio de la naranja es: {pNaranja}')