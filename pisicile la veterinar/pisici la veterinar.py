#citire
n,k=input().split()
Pisica=input().split()
Cusca=input().split()

#prelucrare
Pisici=[int(x) for x in Pisica]
Custi=[int(x) for x in Cusca]
Pisici.sort(reverse=True) #luam cele mai mari pisici
Custi.sort()# si cele mai mici custi

i=0 #contor
for pisica in Pisici:
    for cusca in Custi:
        if pisica<cusca:
            i+=1
            Custi.remove(cusca) #folosim cusca
            break

#afisare
print(i)