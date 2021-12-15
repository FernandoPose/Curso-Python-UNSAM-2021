# Ejercicio 9.4

import costo_camion
import informe

print(costo_camion.costo_camion('../Data/camion.csv'))
informe.informe_camion('../Data/camion.csv', '../Data/precios.csv')
