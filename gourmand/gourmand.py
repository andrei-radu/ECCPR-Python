#citire
N=int(input())
Emotii=[]
for i in range(N):
    Emotii.append(input().split())
Oameni=[]
read=input().split()
while read:
    Oameni.append(read)
    read=input().split()
    
#prelucrare
def Scor(emotie): #subprogram care ne da scorul dupa emotie
    for emot in Emotii:
        if emotie==emot[0]:
            return int(emot[1])

Mancare=[]
for mancare in Oameni: #creem un vector care contine fiecare mancare si produsul punctelor
    if [mancare[2],1.0] not in Mancare:
        Mancare.append([mancare[2],1.0])

Contor=[ 0 for i in range(len(Mancare))] #numaram de cate ori apare fiecare mancare
for i in range(len(Mancare)): #pentru fiecare mancare
    for oameni in Oameni: #cautam sa ii adaugam scorul si sa crestem contorul
        if Mancare[i][0]==oameni[2]:
            Mancare[i][1]*=Scor(oameni[1])
            Contor[i]+=1

for i in range(len(Mancare)):
    Mancare[i][1]=format(pow(Mancare[i][1],1/Contor[i]),'.2f') #aplicam formula de calcul pt fiecare mancare

def Intoarce(lista): #subprogram care returneaza ordinea inversa a elementelor 
    for el in lista:
        temp=el[0]
        el[0]=el[1]
        el[1]=temp
    return lista

Mancancare=Intoarce(Mancare) #intoarcem ca sa avem scorurul primul
Mancare.sort(reverse=True) #sortam in ordine inversa dupa scor
Mancare=Intoarce(Mancare) #intoarcem la loc lista

#afisare
for mancare in Mancare:
    print(' '.join(mancare))