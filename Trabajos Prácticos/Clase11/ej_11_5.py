# Ejercicio 11.5

def posiciones_de(a, b):
    idx = []
    if len(a) < len(b):
        return idx

    if a[-len(b):] == b:
        idx.append(a.index(b, -len(b)))
        idx = idx + posiciones_de(a[:-1], b)
        return idx
    else:
        return posiciones_de(a[:-1], b)

print(posiciones_de('Un tete a tete con Tete', 'te'))