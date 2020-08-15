#citire
n=int(input())
Monede=[]
for i in range(n):
    k=input()
    Monede.append(input().split())

#prelucrare
def EsteUtil(lista): #subprogram care ne spune daca un lot este util sau nu
    Contine=[5,15,25,100,300,500]
    for ban in Contine: #verificam daca contine cate o moneda din fiecare tip
        if str(ban) not in lista:
            return False
    if len(lista)<8 or len(lista)>20: #verificam daca are intre 8 si 20 de monede
        return False
    suma=0
    sub1=0
    for ban in lista: #aflam suma si cate monede sunt sub 1 leu
        if int(ban)<100:
            sub1+=1
        suma+=int(ban)
    if sub1/len(lista)<=0.5 or suma>2900: #daca suma e mai mare de 29 de lei si nu sunt majoritare monele sub 1 leu
        return False
    return True #daca totul e ok

Utile=[]
utile=0
for bani in Monede: #verificam pt fiecare lot 
    if EsteUtil(bani):
        Utile.append('1') 
        utile+=1
    else:
        Utile.append('0')

#afisare
print(' '.join(Utile))
print(1-utile/len(Monede)) #afisam procentul