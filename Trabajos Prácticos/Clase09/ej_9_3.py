# Ejercicio 9.3

import fileparse

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cajones):
        self.cajones -= cajones


with open('../Data/camion.csv') as lineas:
    camion_dict = fileparse.parse_csv(lineas, 
                                      select = ['nombre', 'cajones', 'precio'],
                                      types =  [str, int, float])
    
camion = [ Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dict]
print(f'Precio total: {sum([c.costo() for c in camion])}')

