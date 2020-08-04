#citire
n=int(input())
Elevi=[]
for i in range(n):
    Elevi.append(input().split())
barem=int(input())

#prelucrare
contor=0
timpi=[]
for elev in Elevi: #numaram elevii care indeplinesc conditia
    if int(elev[2])<barem:
        contor+=1
        timpi.append(elev[2])
timpi.sort() #sortam timpii pentru a afisa elevii in ordine crescatoare dupa el

#afisare
print(contor) #afisam nr de elevi
for i in range(contor):
    for elev in Elevi:
        if elev[2]==timpi[i]:
            print(' '.join(elev)) #si fiecare elev dupa timpul lui