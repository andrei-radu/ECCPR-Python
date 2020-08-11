#citire
n=input()
Valori=input().split()

#prelucrare
Bucket=[0 for i in range(20)] #nu folosim indexul 0

def NumarCifre(nr): #program care intoarce nr de cifre, deoarece bucketurile cerute reprezinta asta
    contor=0
    for cifra in nr:
        contor+=1
    return int(contor)

for valoare in Valori: #pentru fiecare valoare
    Bucket[NumarCifre(valoare)]+=1 #crestem contorul bucketului in care se incadreaza
    
#afisare
for i in range(len(Bucket)):
    if Bucket[i]==0:
        pass #daca nu contine elemente, nu afisam bucketul
    else:
        print(str(i)+' '+str(Bucket[i]))