# Ejercicio 11.3

def digitos(n):
    cDigitos = 1
    if n < 10:
        return (1)
    else:
        n = n / 10
        cDigitos = cDigitos + digitos(n)
        return(cDigitos)


cDigitos = digitos(123456789)
print(f'El número tiene: {cDigitos} digitos.')