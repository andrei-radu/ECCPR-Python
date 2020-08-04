from math import sqrt,pow
#citire
n=int(input())
coordonate=[]
for i in range(n):
    coordonate.append(input().split())
start=input().split()

#prelucrare
def calcul_distanta(pozitie,lista): #subprogram care calculeaza D
    x=int(lista[0])
    y=int(lista[1])
    z=int(lista[2])
    xp=int(pozitie[0])
    yp=int(pozitie[1])
    zp=int(pozitie[2])
    return sqrt(pow((x-xp),2)+pow((y-yp),2)+pow((z-zp),2))

distanta=0.0
actuala=start
for i in range(n):
    Distante=[]
    for j in range(n-i):
        Distante.append(calcul_distanta(actuala, coordonate[j]))
    distantamin=min(Distante) #aflam distanta minima din punctul de unde ne aflam
    
    for j in range(n-i):
        if Distante[j]==distantamin:
            distanta+=distantamin #adaugam distana pana la o planeta
            actuala=coordonate[j] #ne deplasam pana acolo
            coordonate.pop(j) #o scoatem din lista de coordonate
            break

#afisare
print(format(distanta,'.2f'))