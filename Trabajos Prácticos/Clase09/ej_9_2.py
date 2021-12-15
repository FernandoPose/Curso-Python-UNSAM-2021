# Ejercicio 9.2

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cajones):
        self.cajones -= cajones


s = Lote('Pera', 100, 490.10)

print(f' Precio inicial del camion: {s.costo()}')
print(f' Cantidad de cajones: {s.cajones}')
s.vender(25)
print(f'Cantidad de cajones luego de la venta: {s.cajones}')
print(f'Nuevo costo: {s.costo()}')
