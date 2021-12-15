# Ejercicio 11.4

def potencia(n, b):         # b^x = n?
    if n == b or n == 1:
        return True
    if n > b:
        if n % b == 0:
            return potencia(n//b, b)
        else:
            return False
    
    if n < b:
        if b % n == 0:
            return potencia(n, b//n)
        else:
            return False
        

print(f'El número 8 es potencia de 2? {potencia(8, 2)}')
print(f'El número 64 es potencia de 4? {potencia(64, 4)}')
print(f'El número 70 es potencia de 10? {potencia(70, 10)}')
print(f'El número 1 es potencia de 2? {potencia(1, 2)}')
