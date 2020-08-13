#citire
[n,p]=input().split()
Presiuni=input().split()
    
#prelucrare
for i in range(int(p)):
    suma=0
    for j in range(i,int(n)+i):
        suma+=float(Presiuni[j]) #calculam suma presiunilor din n zile anterioare
    Presiuni.append(suma/int(n)) #si adaugam in lista media lor

#afisare
afisare=[str(format(x,'.2f')) for x in Presiuni[int(n):int(n)+int(p)] ] #facem string ca sa putem afisa; afisam doar cele p zile prezise
print(' '.join(afisare))  
print( format(max(Presiuni[int(n):int(n)+int(p)])-min(Presiuni[int(n):int(n)+int(p)]),'.2f')) #afisam diferenta dintre maxim si minim in zilele prezise