n=int(input())
Emotii=[]
for i in range(n):
    lin=input().split()
    lin[1]=int(lin[1])
    Emotii.append(lin)

Date=[]
read=input().split()
while read:
    Date.append([read[1],read[2]])#nu ne intereseaza numele persoanei
    read=input().split()
    
#prelucrare
Meserii=[] #aflam care sunt toate meseriile
for i in range(len(Date)):
    if Date[i][1] not in Meserii:
        Meserii.append(Date[i][1])

Scor=[0 for i in range(len(Meserii))] #pentru a aduna toate punctajele 
Contoare=[0 for i in range(len(Meserii))] #pentru a vedea cate persoane sunt in domeniu
for i in range(len(Meserii)):
    for j in range(len(Date)):
        if Meserii[i]==Date[j][1]: #daca se potriveste meseria
            for emotie in Emotii: 
                if emotie[0]==Date[j][0]: #cautam emotia
                    Scor[i]+=emotie[1] #ii adaugam puncatjul
            Contoare[i]+=1 #crestem contorul

#afisare
afisare=[]
for i in range(len(Meserii)): #creem un vector pentru a afisa dupa cerinta
    afisare.append([Meserii[i],str(format(Scor[i]/Contoare[i],'.2f'))])

for element in afisare:
    print(' '.join(element))