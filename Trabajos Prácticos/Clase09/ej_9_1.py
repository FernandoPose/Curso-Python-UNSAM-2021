# Ejercicio 9.1

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio


a = Lote('Pera', 100, 490.10)
b = Lote('Manzana', 50, 122.34)
c = Lote('Naranja', 75, 91.75)

lotes = [a, b, c]

for c in lotes:
    print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
    
