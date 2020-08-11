from math import sqrt,pow
#citire
m=int(input())
n=int(input())
A=[]
for i in range(m*n):
    A.append(int(input()))

#prelucrare
def Dist(lista,medie): #suprogram care calculeaza d
    suma=0
    for element in lista:
        suma+=pow(element-medie,2)
    return sqrt(suma/10)


hA=[0 for i in range(10)] #creem histograma
for element in A:
    hA[element]+=1 #si o populam conform cerintei

medie=sum(hA)/len(hA) #calculam media
d=Dist(hA,medie) #calculam d

contor=0
for element in hA: #numaram cate elemente sunt mai mari ca d
    if element>=d:
        contor+=1
    
#afisare
print(contor)