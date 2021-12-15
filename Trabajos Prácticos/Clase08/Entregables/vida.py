# Ejercicio 8.1

import datetime

def vida_en_segundos(fecha_nac):
    now = datetime.datetime.now()
    nacimiento = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    sVividos =  now - nacimiento
    return sVividos.total_seconds()

def main():
    fecha_nac = '26/08/1991'
    sVividos = vida_en_segundos(fecha_nac)
    print(f'Segundos vividos: {sVividos}')
    
if __name__ == '__main__':
    main()