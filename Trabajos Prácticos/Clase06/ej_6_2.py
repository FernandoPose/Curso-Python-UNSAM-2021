# Ejercicio 6.2

def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1] #? l[::-1] = [-n, ..., -3, -2, -1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp

#%%
l  = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lc = l.copy()                       
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(lc)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#! 1) Se modificó la lista original dado que al pasar l paso una referencia y estaría editando el vector original.
#! 2) No quedó igual ya que una vez realizada la propagación a derecha se crea una nueva lista con los valores resultantes.
#! 3) Se corrige creando una lista copia (lc = l.copy()).
#! 4) n-1 operaciones
#! 5) (n-1) + n + (n-1) + n = 2n + 2(n-1) = 4n-2 operaciones

