# Ejercicio 9.11

#! Para que funcione, le agrego a la línea 26 un .copy. 
#! Esto es debido a que contenido=[] asigna siempre la misma dirección si no se envia una lista
#! lo que hace que todo quede apuntado a la misma dirección de memoria.
#! Además, si no se pasa una lista, se rompe por el copy por lo que se debe verificar si corresponde o no a una lista.

class Canguro:
    
    def __init__(self, nombre, contenido = []):
        self.nombre = nombre
        self.contenido_marsupio = contenido
    
    def meter_en_marsupio(self, item):
        self.contenido_marsupio.append(item)
        
    def __str__(self):
        return f'Canguro(Nombre: {self.nombre}, Contenido: {self.contenido_marsupio})'


class Canguro_Malo:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = []
        if not isinstance(contenido, list):
            self.contenido_marsupio.append(contenido)
        else:
            self.contenido_marsupio = contenido.copy()

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


def canguro_bueno():
    # Creo los objetos: madre_canguro y cangurito
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    # Le agrego algunos items a madre_canguro
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    # Imprimo madre_canguro
    print(madre_canguro)

def canguro_malo():
    # Creo los objetos: madre_canguro y cangurito
    madre_canguro = Canguro_Malo('Madre')
    cangurito = Canguro_Malo('gurito')
    # Le agrego algunos items a madre_canguro
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    # Imprimo madre_canguro
    print(cangurito)

def main():
    #canguro_bueno()
    canguro_malo()

if __name__ == "__main__":
    main()


