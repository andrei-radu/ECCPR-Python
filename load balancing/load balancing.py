#citire
lin=input().split()
k=int(lin[0])
n=int(lin[1])
Date=input().split()

#prelucrare
Linii=[ [] for x in range(k)]
i=0
for element in Date:
    if i<k:# pune elementul pe linia corespunzatoare
        Linii[i].append(element)
        i+=1
    else: #cand trece de ultima linie, pune pe prima si se repeta
        Linii[0].append(element)
        i=1

def suma(linie): #subprogram pt calculul sumei unei linii
    s=0         #necesar deoarece avem nevoie de linie de stringuri pentru afisare
    for el in linie:
       s+=int(el)
    return s

#afisare
separator=' '
for linie in Linii:
    if suma(linie):# pentru evitarea afisarii liniilor goale
        print(separator.join(linie))