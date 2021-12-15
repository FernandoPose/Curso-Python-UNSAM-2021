

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')

        #raise RuntimeError('¡Qué moco!') 
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
        
print(f'Ingresaste {n}.')

