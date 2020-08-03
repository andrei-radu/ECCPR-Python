#citire
n=int(input())
Numere=[]
for i in range(n):
    Numere.append(int(input()))

#prelucrare
Zerouri=[]
for nr in Numere:
    nrbin=str(bin(nr)) #il facem string pentru a putea fi mai usor de analizat
    contor=10-len(nrbin) #pentru ca trebuie sa fie pe 8 biti (10 deoarece avem codul 0b pt nr binare in python), contorul ia de la inceput nr de zerouri pana in primul 1
    for cifra in nrbin:
        if cifra=='0': #se mareste contorul pt fiecare 0
            contor+=1
    Zerouri.append(contor)

#afisare
for i in range(n): #afisam toate nr care au nr maxim de zerouri
    if Zerouri[i]==max(Zerouri):
        print(Numere[i])