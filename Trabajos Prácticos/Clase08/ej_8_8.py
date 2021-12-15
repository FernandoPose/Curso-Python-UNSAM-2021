# Ejercicio 8.8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def hacer_boxplot(df_lineal_seleccion, cols_sel):
    
    # Altura de los árboles agrupadas por especie
    df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
    plt.show()
    
    # Diámetros de los árboles agrupadas por especie
    df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
    plt.show()
    
    # Pairplot (seaborn)
    sns.pairplot(data = df_lineal_seleccion, hue = 'nombre_cientifico')
    plt.show()
    
def main(nombre_archivo):
    
    # Cargo el dataset (solo las columnas pedidas)
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    datos = pd.read_csv(nombre_archivo)[cols_sel]
    
    # Creo el dataframe final
    df_lineal = pd.DataFrame(datos)
    
    # Obtengo e imprimo las 10 especies mas frecuentes
    cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
    print(cant_ejemplares.head(10))
    
    # Selecciono especies
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    print(df_lineal_seleccion)

    # Realizo los gráficos
    hacer_boxplot(df_lineal_seleccion, cols_sel)
    
if __name__ == '__main__':
    nombre_archivo = '../Data/arbolado-publico-lineal-2017-2018.csv'
    main(nombre_archivo)