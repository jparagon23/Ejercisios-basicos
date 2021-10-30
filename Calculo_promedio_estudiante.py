# promedio de estudiante
import statistics
notas=int(input('cuantas notas vas a ingresar: '))
notas_examenes=[]
i=0
for i in range(notas):
    nota_e=int(input('ingrese la nota que obtuvo: '))
    notas_examenes.append(nota_e)

promedio=statistics.mean(notas_examenes)
print('el promedio es:',promedio)

