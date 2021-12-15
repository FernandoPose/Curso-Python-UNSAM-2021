# Ejercicio 11.13

def hojas_ISO(N):
    
    # Hoja A0
    ancho   = 841
    alto    = 1189
    # Validación
    if N>10:
        return -1
    # Ejecución
    if N == 0: # Caso base
        return (ancho, alto)
    else:
        (ancho, alto) = hojas_ISO(N-1)
        if ancho > alto:
            ancho = ancho // 2
        else:
            alto = alto // 2
        return (ancho, alto)

def main():
    for i in range(20):
        hoja = hojas_ISO(i)
        if not(hoja == -1):  
            print(f'Ancho: {hoja[0]} - Largo: {hoja[1]}')
        else:
            print('Tamaño mínimo A10')
            
if __name__ == '__main__':
    main()