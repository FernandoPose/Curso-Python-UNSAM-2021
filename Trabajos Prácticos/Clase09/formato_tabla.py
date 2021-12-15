# Ejercicio 9.5


class FormatoTabla:
    
    def encabezado(self, headers):
        
        raise NotImplementedError()

    def fila(self, rowdata):
        raise NotImplementedError()
    

class FormatoTablaTXT(FormatoTabla):
    
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    
    def encabezado(self, headers):
        print(','.join(headers))
    
    def fila(self, data_fila):
        print(','.join(data_fila))
     
class FormatoTablaHTML(FormatoTabla):
    
    def encabezado(self, headers):    
        print(f'<tr>', end = '')
        for c in headers:
            print(f'<th>{c}</th>', end = '')
        print(f'</tr>')
    
    def fila(self, data_fila):
        print(f'<tr>', end = '')
        for c in data_fila:
            print(f'<td>{c}</td>', end = '')
        print(f'</tr>')
        
        
def crear_formateador(fmt):
    
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    
    return formateador