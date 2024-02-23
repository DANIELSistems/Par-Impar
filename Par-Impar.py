import math

#input

X=int(input("digite el valor de X:" ))

#processing

r=X%2

if r==0:
    rta="PAR"

else:
    rta="IMPAR"

#OUTPUT
    
print("el numero "+ str(X)+ " es " + rta)

