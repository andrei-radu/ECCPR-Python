#citire
D=int(input())
N=int(input())
Patratele=[]
for i in range(N):
    Patratele.append(input().split(','))
d=int(input())

#prelucrare
Linii=[0 for i in range(D*(D+1))] #creem un vector pentru linii
Coloane=[0 for i in range(D*(D+1))] #si unul pentru coloane
for patrat in Patratele:
    x=int(patrat[0])-1 #luam coordonatele de inceput ale patratului
    y=int(patrat[1])-1
    Coloane[x*D+y]+=1 #salvam liniile si coloanele folosite pentru fiecare patrat
    Coloane[(x+1)*D+y]+=1
    Linii[y*D+x]+=1
    Linii[(y+1)*D+x]+=1
    
cnt=0 #contor pentru perimetru
for lin in Linii: #numaram cate linii sunt folosite o singura data
    if lin==1:    #adica reprezinta marginea 
        cnt+=1
        
for col in Coloane: #asemenea pt coloane
    if col==1:
        cnt+=1

#afisare
print(str(d*cnt))
