#citire
[b,n]=input().split()
BazaDate=[]
for i in range(int(b)):
    BazaDate.append(input().split())
Produse=input().split()

#prelucrare
total=0.0
reducere=0.0
for produs in Produse:
    for obiect in BazaDate: #cautam produsul in baza de date
        if produs==obiect[0]: #daca codul de bare coincide
            if obiect[1]=='p': #daca este produs adaugam pretul
                total+=float(obiect[2])
            else: #daca este reducere, adaugam reducerea
                reducere+=float(obiect[2])

total-=(total*reducere/100) #aplicam reducerile

#afisare
print(format(total,'.2f'))