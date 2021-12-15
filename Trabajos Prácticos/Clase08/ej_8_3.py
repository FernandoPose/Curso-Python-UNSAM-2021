# Ejercicio 8.3

import datetime

inicio      = '26-09-2020'
duracion    = 200

inicio = datetime.datetime.strptime(inicio, '%d-%m-%Y') 
duracion = datetime.timedelta(days=duracion)
fin = inicio + duracion
print(f'Comienzo de licencia: {inicio}. Fin de la licencia: {fin}')
