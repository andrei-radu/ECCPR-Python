#Citire
N=int(input())
Copii=[]
for i in range(N):
    Copii.append(input().split())

#prelucrare    
def suprafata(x1,y1,x2,y2): #subprogram care returneaza suprafata
    return (int(x2)-int(x1))*(int(y2)-int(y1))

Suprafete=[]
for copil in Copii: #aflam suprafata desenata de fiecare copil
    Suprafete.append(suprafata(copil[1], copil[2], copil[3], copil[4]))

supmax=max(Suprafete)
index=0 #gasim suprafata maxima si ii retinem indexul 
for i in range(len(Suprafete)):
    if supmax==Suprafete[i]:
        index=i
    
#afisare
afisare=Copii[index]
afisare.append(str(Suprafete[index]))
separator=' ' #concatenam toate informatiile pt a le afisa
print(separator.join(afisare))