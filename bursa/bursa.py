#citire
N=int(input())
Zile=input().split()

#prelucrare
Variatie=[ int(Zile[i])-int(Zile[i-1]) for i in range(1,len(Zile))] #creem vectorul de variatie

def SemnAlt(e1,e2): #subprgram care ne spune daca alterneaza semnul a doua elemente
    if e1>=0 and e2<0:
        return True
    elif e2>=0 and e1<0:
        return True
    else:
        return False


i=0
Contor=[] #punem indicele de start si lungimea in el
while i<len(Variatie)-1:
    indice=0
    lungime=0
    if SemnAlt(Variatie[i],Variatie[i+1]): #daca gasim doua numere care sa alterneze ca semn
        indice=i+1 #luam indicele din Zile, nu din Variatie
        lungime+=1
        while SemnAlt(Variatie[i],Variatie[i+1]): #facem asta pana nu mai alterneaza
            lungime+=1
            i+=1
            if(i+1)>=len(Variatie): #exceptie ca sa nu trecem peste nr maxim de variatii
                break
    i+=1
    if indice and lungime: #daca am gasit, le notam
        Contor.append([indice,lungime])
        
NrMax=0
IndexMax=0
for el in Contor: #aflam nr maxim de elemente care variaza, si unde incepe variatia in lista Zile
    if NrMax<=el[1]:
        NrMax=el[1]
        IndexMax=el[0]

poz=0       
for el in Variatie: #numaram cate elemente sunt pozitive
    if el>=0:
        poz+=1

ProcentP=poz/len(Variatie)*100 #aflam procentele
ProcentN=100-ProcentP

#afisare
print(NrMax) #afisam nr de variatii
if NrMax: #daca difera de 0, afisam si valorile actiunilor din zilele respective
    afisare=[ str(x) for x in Zile[IndexMax:IndexMax+NrMax]]
    print(' '.join(afisare))
    print('+:'+format(ProcentP,'.2f')+'% -:'+format(ProcentN,'.2f')+'%') #si procentele