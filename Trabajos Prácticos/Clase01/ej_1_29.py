# Ejercicio 1.29


frase = 'Todos somos programadores'
#frase = 'Los hermanos sean unidos porque ésa es la ley primera'
#frase = '¿cómo transmitir a los otros el infinito Aleph?'
#frase = 'Todos, tu también'
lista = []

palabras = frase.split()
for palabra in palabras:
    if palabra[-2:].find('o') != -1:
        nPalabra = palabra[:-2] + palabra[-2:].replace('o','e')
        lista.append(nPalabra)
    else:
        lista.append(palabra)
        
frase_t = ' '.join(lista)
print(frase_t)

