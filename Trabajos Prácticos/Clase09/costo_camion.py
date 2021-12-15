# costo_camion.py

import informe

def costo_camion(nombre_archivo):
    cCamion = informe.leer_camion(nombre_archivo)
    return sum([s.cajones * s.precio for s in cCamion])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usoe: %s archivo_camion' % args[0])
    filename = args[1]
    print('Costo total:', costo_camion(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)