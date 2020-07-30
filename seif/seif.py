#citire
Numere=input()
Numere=Numere.split()

r=int(input())

i=0
sens=[]
pozitii=[]
while i<r:
    linie=input()
    linie=linie.split()
    sens.append(linie[0])
    pozitii.append(linie[1])
    i+=1
    
#prelucrare
Parcurgeri=[]
i=0 #calculam numarul total de parcurgeri (cu - pentru cele spre stanga)
for directie in sens: 
    Parcurgeri.append(int(directie)*int(pozitii[i]))
    i+=1
NrParcurgeri=sum(Parcurgeri)
NrParcurgeri=NrParcurgeri%6    
#folosim modulo 6 pentru a determina, in cazul in care seiful face o rotatie completa
#modulo 6 ajuta si in cazul rotirilor spre stanga deoarece returneaza complementul (nr de rotiri spre dreapta echivalente)

#afisare
print(Numere[NrParcurgeri])