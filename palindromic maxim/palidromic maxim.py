from itertools import permutations
#citire
n=int(input())
Cifre=input().split()

#prelucrare
def palidrom(nr): #subprogram pt a determina daca un nr este palidrom
    if nr==nr[::-1]: # [::-1] intoarce sirul invers
        return True
    else: return False
  
Permutari=permutations(Cifre)    
nrpal=0
for permutare in Permutari:
    nr=''
    for cifra in permutare:
        nr+=cifra
    if int(nr)>nrpal and palidrom(nr):
        nrpal=int(nr)

print(nrpal)