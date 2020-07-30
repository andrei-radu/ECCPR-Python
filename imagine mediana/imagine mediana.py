#citire
lin=int(input())
col=int(input())
i=1
linie=[]
A=[]
while i<=lin*col:
    element=int(input())
    linie.append(element)
    if i%lin==0:
        A.append(linie)
        linie=[]
    i+=1

#prelucrare
Azero=[] # o construim noi
i=0
while i<lin+2: #+2 pentru bordare: margine sus si margine jos
    j=0
    while j<col+2: #+2 pt bordare: margine dreapta si margine stanga
        if i==0 or i==lin+1 or j==0 or j==col+1:
            element=0 #daca e pe margine, pune 0
        else:
            element=A[i-1][j-1] #altfel pune elementul din A
        linie.append(element)
        j+=1
    Azero.append(linie)
    linie=[]
    i+=1

Af=[] # o construim noi
i=1
while i<lin+1:
    j=1
    while j<col+1:
        median=[] #adaugam valorile din enunt
        median.append(Azero[i-1][j])
        median.append(Azero[i][j-1])
        median.append(Azero[i][j])
        median.append(Azero[i][j+1])
        median.append(Azero[i+1][j])
        
        median.sort() #il sortam
        element=median[int((col+2)/2)] #luam valoarea de la mijloc
        linie.append(element)
        
        j+=1
    Af.append(linie)
    linie=[]
    i+=1

#afisare
for linie in Af:
    for el in linie:
        print(el)