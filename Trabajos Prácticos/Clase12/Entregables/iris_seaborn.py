# Ejercicio 12.10

import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt 


# Cargo el dataset
iris_dataset = load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
#pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

# Agrego target al dataframe
iris_dataframe['target'] = iris_dataset['target']

# Grafico matriz de dispersión
sns.pairplot(iris_dataframe, hue='target')
plt.show()


