# Ejercicio 3.17

cTabla = list()

for col,row in enumerate(range(10)):
    xTabla = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for val in range(10):
        if val == 0:
            xTabla[val] = 0
        else:
            xTabla[val] = (xTabla[val - 1] + col)  
    cTabla.append(xTabla)

print( f' {0:>7d} {1:>2d} {2:>2d} {3:>2d} {4:>2d} {5:>2d} {6:>2d} {7:>2d} {8:>2d} {9:>2d}' )
print(f'-----------------------------------')
for col, row in enumerate(cTabla):
    print( f" {f'{col:d}:':<4s} {row[0]:>2d} {row[1]:>2d} {row[2]:>2d} {row[3]:>2d} {row[4]:>2d} {row[5]:>2d} {row[6]:>2d} {row[7]:>2d} {row[8]:>2d} {row[9]:>2d}")

