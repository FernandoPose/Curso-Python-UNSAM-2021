# Ejercicio 9.12

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    
class TorreDeControl():
    
    def __init__(self):
        self.arribo = Cola()
        self.partida = Cola()
    
    def nuevo_arribo(self, codigo):
        self.arribo.encolar(codigo)
    
    def nueva_partida(self, codigo):
        self.partida.encolar(codigo)
    
    def ver_estado(self):
        if not self.arribo.esta_vacia():
            print(f'Vuelos esperando para aterrizar: {",".join(self.arribo.items)}')
        if not self.partida.esta_vacia():
            print(f'Vuelos esperando para despegar: {",".join(self.partida.items)}')
    
    def asignar_pista(self):
        if ( len(self.arribo.items) + len(self.partida.items) ) == 0:
            print('No hay vuelos en espera.')
        elif len(self.arribo.items) > 0:
            print(f'El vuelo {self.arribo.desencolar()} aterrizó con éxito.')
        elif len(self.partida.items) > 0:
            print(f'El vuelo {self.partida.desencolar()} despegó con éxito.')
            

def main():
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
             
if __name__ == '__main__':
    main()
    

        
    
    
    




