#citire
n=int(input())
V=[]
for i in range(n):
    V.append(float(input()))
w=int(input())

#prelucrare
def TreceriZero(lista): #subprogram care intoarce nr de treceri prin zero
    contor=0
    for i in range(1,len(lista)):
        if (lista[i]>0 and lista[i-1]<0) or (lista[i]<0 and lista[i-1]>0):
            contor+=1
    return contor

Vector=[] #creem vectori pentru fiecare w numere
while V:
    lin=[]
    for i in range(w):
        if V: #cat timp exista un element, il adaugam
            lin.append(V[0])
            V.pop(0)
        else: #daca a ramas fara elemente, ne oprim
            break
    Vector.append(lin)

Contoare=[] # lista ca sa retinem nr de treceri prin zero
for linie in Vector:
    medie=sum(linie)/len(linie) #aflam media pentru fiecare w numere
    Vtemp=[(element-medie) for element in linie] #creem un vector temportat conform cerintei
    Contoare.append(TreceriZero(Vtemp)) #aflam numarul de treceri prin 0 si il stocam
    
#afisare
for cont in Contoare:
    print(cont)