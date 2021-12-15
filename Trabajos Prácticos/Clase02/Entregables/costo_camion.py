import csv

def costo_camion(nombre_archivo):
    nFila = 1
    cTotal = 0
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(file)
        for row in rows:
            try:
                cTotal = cTotal + int(row[1]) * float(row[2])
                nFila = nFila + 1
            except ValueError:
                print(f'Falta de dato en fila {nFila + 1}')
                nFila = nFila + 1    
        return cTotal

costo = costo_camion('../Data/camion.csv')

print(f'Costo total: {costo}')