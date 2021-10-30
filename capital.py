capital= int(input('ingrese el capital: '))
tasa=int(input('ingrese la tasa: '))
año=int(input('ingrese los años'))
calculo=0
for i in range(año):
    if calculo<=0:
        calculo=capital*(1+(tasa/100))
    else:
        calculo=calculo*(1+(tasa/100))
print(calculo)