#citire
n=int(input())
Linii=[]
for i in range(n):
    Linii.append(input().split(','))
    
#prelucrare
def Special(nr): #subprogram care returneaza un cod pentru fiecare tip de numar
    for cifra in nr:
        if cifra=='(': #daca trebuie afisat fara (
            return 1
        if cifra==')': #daca trebuie puse zerouri
            return 2
    return 0 #daca nu este nimic special la el

def NrSpec(nr): #un subprogram care returneaza nr fara paranteze
    ret=''
    for cifra in nr:
        if cifra!='(' and cifra!=')':
            ret+=cifra
    return ret


Afisare=[]
for linie in Linii:
    lin=[]
    for element in linie: #pentru fiecare cifra
        if Special(element)==1: #daca trebuie pus fara (
            lin.append(NrSpec(element))
        elif Special(element)==2: #daca trebuie puse un numar de zerouri
            zerouri=int(NrSpec(element))
            for i in range(zerouri):
                lin.append('0')
        else: #sau daca nu trebuie facut nimic
            lin.append(element)
    Afisare.append(lin)
        
#afisare
for linie in Afisare:
    print(','.join(linie)) #le afisam cu , intre ele