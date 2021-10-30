aux=0
aux2=0

n=int(input('ingrese el numero'))
i=10

while i<=n:
    aux=n%10
    print(aux)
    n=n//10
    print(n)
    aux2=aux2*10+aux
    print(aux2)
aux2=aux2*10+n
print(aux2)
