#citire
lin1=input()
lin1=lin1.split()
m=int(lin1[0])
n=int(lin1[1])
p=int(lin1[2])

i=0
Nume=[] #vector pentru numele studentului
Note=[] #vector pentru notele acestuia
temp=0
while i<m:
    Nume.append(input())
    temp=input()
    temp=temp.split()
    Note.append(temp)
    i+=1

#prelucrare
Integralist=[] #vector pentru determinarea studentilor integralisti
Medie=[] #vector pentru stocarea mediei fiecatui student
i=0
for elev in Nume:
    integralist=1; #presupunem ca este integralist
    medie=0
    for nota in Note[i]: #ii calculam suma notelor
        medie+=int(nota)
        if(int(nota)<5):
            integralist=0 #daca are o materie sub 5, nu mai este integralist
    Medie.append(float(medie/n)) #ii facem media si o adaugam in vector
    if(integralist): #ii adaugam calitatea de integralist
        Integralist.append(1)
    else:
        Integralist.append(0)
    i+=1
    
nrburs=0;
i=0
nume=''
maxim=0
for med in Medie: 
    if(med>8)and(Integralist[i]): #numaram cate burse se pot lua
        nrburs+=1
    if(med>8)and(Integralist[i])and(med>maxim): #cautam media cea mai mare a unui integralist
        nume=Nume[i]
        maxim=med
    i+=1

#afisare   
if (nrburs-1)>p: print(p) #nr de burse, ori cate sunt disponibile
else: print(nrburs-1) #ori cati studenti iau bursa

print(nume+' '+format(maxim,'.2f')) #studentul cu media cea mai mare