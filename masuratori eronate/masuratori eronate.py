from math import sqrt,pow
#citire
n=int(input())
Valori=input().split()
for i in range(n): #transformam in float
    Valori[i]=float(Valori[i])

#prelucrare
def medie(lista): #subprogram pt medie
    return sum(lista)/len(lista)
    
def DevStd(lista): #subprogram care calculeaza deviatia standard
    miu=medie(lista)
    suma=0
    for element in lista:
        suma+=pow(element-miu,2)
    return sqrt(suma/len(lista))

def raport(dev,med): # subprogram pt raportul dintre deviatia medie si media aritmetica
    return float(dev)/float(med)

def ValDep(lista):
    distanta=[]
    for element in lista: #aflam fiecare distanta in valoare absoluta
        distanta.append(abs(medie(lista)-element))
    for i in range(len(lista)-1): #lungimea listei este cu 1 mai mare ca index
        if distanta[i]==max(distanta):
            lista.pop(i) #eliminam elementul cel mai departat
            break
    return lista

med=1 #valori initiale pentru a putea face calculul
dev=2
nrElim=0
while raport(dev,med)>0.1: #cat timp raportul este mai mare de 10%
    med=medie(Valori) #aflam media
    dev=DevStd(Valori) #aflam deviatia standard
    Valori=ValDep(Valori) #eliminam valoarea cea mai departata
    nrElim+=1
    
#afisare
print(nrElim-1) #deoarece face automat o eliminare