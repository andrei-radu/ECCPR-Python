from math import factorial
#citire
[k,M]=input().split()

#prelucrare
def Aranjamente(n,k): #suprogram care returneaza nr de Aranjamente
    return factorial(int(n))/factorial(int(n)-int(k))

n=int(k)
maxim=0
while Aranjamente(n, k)<=int(M): #cautam nr maxim care respecta conditia
    if Aranjamente(n,k)<=int(M):
        maxim=n #il stocam
        n+=1

#afisare
print(maxim)