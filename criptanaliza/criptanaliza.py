#citire
lin=input().split()
n=lin[0]
k=lin[1]
Numere=input().split()

#prelucrare
def prim(nr): #subprogram pt determinare nr prim
    nr=int(nr)
    for i in range(2,nr):
        if nr%i==0:
            return False
    return True

Prime=[]
for nr in Numere:
    if int(nr)>=int(k) and prim(nr): #daca e mai mare ca k si e si prim il retinem
        Prime.append(int(nr))
        
#afisare
if len(Prime):
    print(min(Prime)) #afisam nr prim minim
else:
    print(-1) #sau -1 daca nu avem niciun nr prim