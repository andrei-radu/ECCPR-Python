from itertools import combinations
#citire
n=int(input())
Lungimi=input().split()

#prelucrare
def Pitagora(tuplu): 
#subprogram care returneaza aria, daca este triunghi dreptunghic
#altfel returneaza 0
    a=int(tuplu[0])
    b=int(tuplu[1])
    c=int(tuplu[2])
    if pow(a,2)+pow(b,2)==pow(c,2):
        return a*b/2
    elif pow(a,2)+pow(c,2)==pow(b,2):
        return a*c/2
    elif pow(b,2)+pow(c,2)==pow(a,2):
        return b*c/2
    else: return 0

Nr=combinations(Lungimi,3) #luam toate combinatiile de 3 numere posibile
arie=0 #contor pentru aria totala
for comb in Nr: #pentru fiecare combinatie
    if Pitagora(comb): #daca este triunghi dreptunghic, ii adaugam aria
        arie+=Pitagora(comb)

#afisare
print(int(arie))