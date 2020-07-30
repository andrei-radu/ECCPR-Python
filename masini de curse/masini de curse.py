#citire
lin1=input()
lin1=lin1.split()
n=int(lin1[0])
k=int(lin1[1])

i=0
pozitie=[]
viteze=[]
while i<k:
    lin=input()
    lin=lin.split()
    pozitie.append(int(lin[0]))
    viteze.append(int(lin[1]))
    i+=1

#prelucrare
timpi=[]
distante=[] 
for element in pozitie:
    distante.append(n-element) #calculam distanta ce trebuie parcursa ca fiind distanta totala - pozitia de inceput
    timpi.append(0) #umplem vectorul timpi

i=0
while i<k:
    timpi[i]=distante[i]/viteze[i] #calculam timpul ca fiind distanta/viteza
    i+=1
timpmin=min(timpi) #aflam timpul minim

i=0
masini=[] #aflam care sunt masinile care ajung in timpul minim
while i<k:
    if timpi[i]==timpmin:
       masini.append(i+1) #+1 deoarece indexul incepe de la 0 si nu exista masina 0
    i+=1
       
#afisare
print(masini)