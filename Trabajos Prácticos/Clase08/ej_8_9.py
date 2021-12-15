# Ejercicio 8.9
# Alumno: Fernando E. Pose (fernandoepose@gmail.com)
# Fecha: 30 - 09 - 2021
# Versión: 1.1.0
# Nota: En caso de queres cambiar el tipo de especie a analizar se debe agregar
#       antes de armar el dataset de debe colocar un input permitiendo al usuario
#       elegir la especie y llamar a la función: armado_dataset con dos nuevos argumentos.

import pandas as pd
import matplotlib.pyplot as plt
import sys

def hacer_boxplot(df_tipas):
    """hacer_boxplot:
            Realiza un boxplot de los diámetros y uno de las alturas por especies de los árboles 
            en veredas y parques de la ciudad.  
    Args:
        df_tipas ([type]): [description]
    Returns:
        [type]: [description]
    """
    
    # Diámetros de los árboles agrupadas por especie
    df_tipas.boxplot('diametro',by = 'ambiente')
    plt.show()
    # Altura de los árboles agrupadas por especie
    df_tipas.boxplot('altura',by = 'ambiente')
    plt.show()
    
    
def armado_dataset(archivo_arboles_veredas, archivo_arboles_parques, especie_parques = 'Tipuana Tipu', especie_veredas = 'Tipuana tipu'):
    """ armado_dataset: 
            La función carga los archivos de árboles en veredas y parques en memoria. Luego filtra las filas
            de los árboles 'tipuana tipu' de cada dataframe. Finalmente renombra las columnas de ambos dataframes.
    Args:
        archivo_arboles_veredas ([string]): Base de datos (archivo csv) de árbolado porteño en veredas de la ciudad
        archivo_arboles_parques ([string]): Base de datos (archivo csv) de árbolado porteño en parques de la ciudad
        especie_parques (str, optional):    Especie a analizar. Defaults to 'Tipuana Tipu'.
        especie_veredas (str, optional):    Especie a analizar. Defaults to 'Tipuana tipu'.
    Returns:
        (df_tipas_parques, df_tipas_veredas): DataFrame de la especie tipas (veredas y parques) para ser analizado
    """
    
    # Cargo ambos datasets
    df_veredas = pd.read_csv(archivo_arboles_veredas)
    df_parques = pd.read_csv(archivo_arboles_parques)
    
    # Columnas analizadas
    cols_sel_veredas = ['diametro_altura_pecho', 'altura_arbol']
    cols_sel_parques = ['diametro', 'altura_tot']

    # Armado de nuevo dataset
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_sel_parques].copy()
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_sel_veredas].copy()
    
    # Renombro columnas
    nColumnas = ['diametro', 'altura']
    
    df_tipas_parques.rename(
        columns={
            cols_sel_parques[1]: nColumnas[0],
            cols_sel_parques[0]: nColumnas[1],
        },
        inplace=True,
    )

    df_tipas_veredas.rename(
        columns={
            cols_sel_veredas[1]: nColumnas[0],
            cols_sel_veredas[0]: nColumnas[1],
        },
        inplace=True,
    )
    
    return (df_tipas_parques, df_tipas_veredas)


def main(archivo_arboles_veredas, archivo_arboles_parques):
    """ main:
            Función principal del programa:
    Args:
        archivo_arboles_veredas ([string]): Base de datos (archivo csv) de árbolado porteño en veredas de la ciudad
        archivo_arboles_parques ([string]): Base de datos (archivo csv) de árbolado porteño en parques de la ciudad
    """
    
    df_tipas_parques, df_tipas_veredas = armado_dataset(archivo_arboles_veredas, archivo_arboles_parques)

    # Agrego a cada dataframe una nueva columna ('ambiente')
    df_tipas_parques['ambiente'] = 'parque'
    df_tipas_veredas['ambiente'] = 'vereda'
    
    # Junto ambos datasets
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    # Realizo los graficos
    hacer_boxplot(df_tipas)
    
    
if __name__ == '__main__':
    
    try: 
        if len(sys.argv) == 3: 
            archivo_arboles_veredas = sys.argv[1]
            archivo_arboles_parques = sys.argv[2]
        else:
            archivo_arboles_veredas = '../Data/arbolado-publico-lineal-2017-2018.csv'
            archivo_arboles_parques = '../Data/arbolado-en-espacios-verdes.csv'
    
    except FileNotFoundError:
        print(f'No existen los archivos en el ordenador')
    
    main(archivo_arboles_veredas, archivo_arboles_parques)
    
    
    



