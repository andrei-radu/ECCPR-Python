#citire
k=int(input())
n=int(input())
Meciuri=[]
for i in range(n):
    Meciuri.append(input().split())
    
#prelucrare
Echipe=[]
for meci in Meciuri: #creem un vector care sa contina echipele si in care vom adauga informatiile dupa fiecare meci
    if [meci[0],0,0,0] not in Echipe:
        Echipe.append([meci[0],0,0,0])
    if [meci[4],0,0,0] not in Echipe:
        Echipe.append([meci[4],0,0,0])

for meci in Meciuri: #analizam fiecare meci si adaugam datele conform rezultatului si cerintelor
    if meci[1] > meci[3]: #daca castiga echipa 1
        for echipa in Echipe:
            if meci[0]==echipa[0]:
                echipa[1]+=3
                echipa[2]+=int(meci[1])
                echipa[3]+=int(meci[3])
            if meci[4]==echipa[0]:
                echipa[2]+=int(meci[3])
                echipa[3]+=int(meci[1])
    elif meci[3]>meci[1]: #daca castiga echipa 2
        for echipa in Echipe:
            if meci[0]==echipa[0]:
                echipa[2]+=int(meci[3])
                echipa[3]+=int(meci[1])
            if meci[4]==echipa[0]:
                echipa[1]+=3
                echipa[2]+=int(meci[1])
                echipa[3]+=int(meci[3])
    else: #daca este remiza
            for echipa in Echipe:
                if meci[0]==echipa[0]:
                    echipa[1]+=1
                    echipa[2]+=int(meci[1])
                    echipa[3]+=int(meci[3])
                if meci[4]==echipa[0]:
                    echipa[1]+=1
                    echipa[2]+=int(meci[3])
                    echipa[3]+=int(meci[1])
                    
#afisare
for echipa in Echipe:
    afisare=[str(element) for element in echipa]
    print(' '.join(afisare))