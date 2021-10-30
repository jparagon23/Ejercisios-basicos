primero=2
ultimo=1000

for i in range(primero,ultimo):
    primo=True
    j=2
    while (i>j) and primo==True:
        if i%j==0:
            primo=False
            break
        else:
            j=j+1
    
    if primo==True:
        print(i,'es primo')



        
            