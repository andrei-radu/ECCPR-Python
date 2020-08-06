#citire
Nmics=int(input())
Valori=[]
for i in range(Nmics):
    Valori.append(input().split())
    
#prelucrare si afisare
for deltaD in range(3): #ni se cer doar 3 medii
    D=0
    Semnal=[] #pentru noul semnal, deoarece avem nevoie de cel vechi
    for linie in Valori:
        lin=linie.copy() #facem o copie deoarece avem nevoie de aceeasi linie si mai tarziu
        for i in range(D):
            lin.pop(-1) #eliminam ultimul element
            lin.insert(0,0) #si adaugam 0 pe primul
        Semnal.append(lin)
        D=D+deltaD #schimbam D dupa fiecare iteratie
    
    medie=[]
    for coloana in range(len(Semnal[0])):
        med=0.0
        for linie in range(len(Semnal)):
            med+=float(Semnal[linie][coloana])  #calculam media dupa o coloana
        medie.append(format(med/len(Semnal),'.2f')) #formatam dupa cerinta, cu 2 zecimale
    
    print(' '.join(medie)) #afisam media dupa care o calculam pe urmatoarea si tot asa