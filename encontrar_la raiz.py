# objetivo=int(input('ingrese el numero: '))
# epsilon=0.01
# paso=epsilon**2
# respuesta=0.0

# while abs(respuesta**2 - objetivo)>=epsilon and respuesta<=objetivo:
#     respuesta +=paso

# if abs(respuesta**2-objetivo)>=epsilon:
#     print('no se encontro')
# else:
#     print(f' la raiz cuadrada de {objetivo} es {respuesta}')


  ## ### ################################ busqueda binaria

objetivo = int(input('un numero'))
epsilon=0.000001
bajo=0.0
alto=max(1.0,objetivo)
respuesta=(alto+bajo)/2

while abs(respuesta**2 - objetivo)>=epsilon:
    if respuesta**2< objetivo:
        bajo=respuesta
    else:
        alto=respuesta
    respuesta=(alto+bajo)/2
print (f' la rais de {objetivo} es {respuesta}')



