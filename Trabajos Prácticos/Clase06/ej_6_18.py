# Ejercicio 6.18

def incrementar(g):
    s = g.copy()
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    secuencia = []            
    secuencia.append([0] * n)
    while ( 0 in secuencia[-1]):
        aux = incrementar(secuencia[-1])
        secuencia.append(aux)
    return secuencia

def main():
    print(listar_secuencias(5))



