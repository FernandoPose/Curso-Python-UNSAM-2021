# Ejercicio 1.8

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
extra = 1000

while saldo > 0:

    if mes < 12: 
        saldo = saldo * (1+tasa/12) - pago_mensual - extra
        total_pagado = total_pagado + pago_mensual + extra  
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    
print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')

