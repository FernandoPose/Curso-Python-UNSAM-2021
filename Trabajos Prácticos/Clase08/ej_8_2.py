# Ejercicio 8.2

import datetime

def proxPrimavera(fPrimavera):
    now = datetime.datetime.now()
    fPrimavera = datetime.datetime.strptime(fPrimavera, '%d/%m/%Y')    
    pPrimavera =  now - fPrimavera
    return abs(pPrimavera)

if __name__ == '__main__':
    fPrimavera = '21/09/2021'
    pPrimavera = proxPrimavera(fPrimavera)
    print(f'Faltan: {pPrimavera.days} días para la primavera')