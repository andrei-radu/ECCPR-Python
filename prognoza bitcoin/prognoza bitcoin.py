#citire
lin=input().split()
n=int(lin[0])
p=int(lin[1])
Preturi=input().split()

#prelucrare
for i in range(p): #pentru numarul de zile procnozate
    suma=0
    for j in range(i,n+i):#calculam media ultimelor n zile
        suma+=float(Preturi[j]) 
    suma/=n
    Preturi.append(format(suma,'.2f')) #o adaugam

#afisare
afisare=Preturi[n:(n+p)] #selectam numai zilele prezise
print(" ".join(afisare)) #le afisam
print(' '.join([max(afisare),min(afisare)])) #afisam maximul si minimul din zilele prezise