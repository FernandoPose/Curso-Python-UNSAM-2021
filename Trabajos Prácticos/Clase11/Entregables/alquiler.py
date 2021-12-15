# Ejercicio 11.14

import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


def grafico_dispersion(superficie, alquiler):
    plt.scatter(x = superficie, y = alquiler)
    plt.xlabel('x')
    plt.ylabel('y')
    return( plt.show() )


def grafico_modelado(superficie, alquiler, a, b):
    g = plt.scatter(x = superficie, y = alquiler)
    grilla_x = np.linspace(start = min(superficie), stop = max(superficie), num = 1000)
    grilla_y = grilla_x*a + b
    plt.title('y ajuste lineal')
    plt.plot(grilla_x, grilla_y, c = 'green')
    plt.xlabel('x')
    plt.ylabel('y')
    return( plt.show() )


def main():
    # Cargo datos
    superficie  = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler    = np.array([35.0, 29.6, 37.4, 21.0])    
    # Grafico la curva de dispersión
    grafico_dispersion(superficie, alquiler)
    # Calculo a,b del modelo de regresión lineal
    (a, b) = ajuste_lineal_simple(superficie, alquiler)
    # Grafico completo
    grafico_modelado(superficie, alquiler, a, b)
    errores = alquiler - (a*superficie + b)
    print(errores)
    print("ECM:", (errores**2).mean())


if __name__ == '__main__':
    main()