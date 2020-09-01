#citire
n=int(input())
Nr=[]
for i in range(n):
    Nr.append(int(input()))
    
#prelucrare
i=0
CombOrd=[]
for i in range(len(Nr)):
    lin=[]
    for j in range(i,n-i):
        lin.append(Nr[j])
    CombOrd.append(lin)
    lin=[]
    for j in range(n-i):
        lin.append(Nr[j])
    CombOrd.append(lin)

Sir=[]
for comb in CombOrd:
    if sum(comb)%3==0:
        Sir.append(comb)

suma=0
lungime=0
for sir in Sir:
    if len(sir)>=lungime:
        lungime=len(sir)
        if sum(sir)>=suma:
            suma=sum(sir)
            
#afisare
if suma==0: print(0)
else:
    print(str(lungime)+" "+str(suma))