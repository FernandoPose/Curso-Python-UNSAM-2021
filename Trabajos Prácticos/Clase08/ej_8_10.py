# Ejercicio 8.10

import pandas as pd
import matplotlib.pyplot as plt
import sys


def main(archivo):
   
    # Cargo el dataframe en memoria
    df = pd.read_csv(archivo, index_col=['Time'], parse_dates=True)

    # Obtengo un fragmento del dataframe
    dh = df['12-25-2014':].copy()
    
    # Arreglo las series para hacerlas coincidentes
    delta_t = -1 # tiempo que tarda la marea entre ambos puertos
    delta_h = 20 # diferencia de los ceros de escala entre ambos puertos
    pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
    plt.show()
    
    
if __name__ == '__main__':
    
    try: 
        if len(sys.argv) == 2: 
            archivo = sys.argv[1]
        else:
            archivo = '../Data/OBS_SHN_SF-BA.csv'
    
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv[1]}')
    
    main(archivo)
    
    
    



