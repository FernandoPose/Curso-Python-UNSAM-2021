# Ejercicio 8.1

import datetime

def seg_vividos(fNacimiento):
    now = datetime.datetime.now()
    nacimiento = datetime.datetime.strptime(fNacimiento, '%d/%m/%Y')
    sVividos =  now - nacimiento
    return sVividos.total_seconds()

def main():
    fNacimiento = '26/08/1991'
    sVividos = seg_vividos(fNacimiento)
    print(f'Segundos vividos: {sVividos}')
    
if __name__ == '__main__':
    main()