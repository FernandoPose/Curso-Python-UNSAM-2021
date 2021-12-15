import informe_final

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cajones):
        self.cajones -= cajones
        
def main():
    camion = informe_final.leer_camion('../Data/camion.csv')
    print(camion)

if __name__ == "__main__":
    main()





