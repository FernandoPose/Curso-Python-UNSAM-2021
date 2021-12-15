# Ejercicio 2.2

cTotal = 0

with open('../Data/camion.csv', 'rt') as file:
    #? Nombre_Fruta - Cant_Cajones - Precio/Cajón
    headers = next(file)
    for line in file:
        row = line.split(',')
        cTotal = cTotal + int(row[1]) * float(row[2])
    
    print(f'Costo total: {cTotal}')
    
    