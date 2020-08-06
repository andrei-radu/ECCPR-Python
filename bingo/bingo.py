#citire
linie=input().split()
n=linie[0]
k=linie[1]
Matrice=input().split()
Strigate=input().split()

#prelucrare
castig=True #ca sa vedem daca castigam sau nu
contor=0 #contor pentru a numara cate nr ne lipsesc

for nr in Matrice: #luam fiecare numar
    if nr not in Strigate: #daca nu il gasim
        castig=False #am pierdut
        contor+=1 #numaram cate nu am gasit

#afisare
if castig:
    print('BINGO!') #daca am castigat afisam bingo
else:
    print(contor) #daca pierdem afisam cate nr ne lipsesc