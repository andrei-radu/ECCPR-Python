#citire
D=int(input())
N=int(input())
Patratele=[]
for i in range(N):
    Patratele.append(input().split(','))
d=int(input())

#prelucrare
Linii=[0 for i in range(D*(D+1))]
Coloane=[0 for i in range(D*(D+1))]
for patrat in Patratele:
    x=int(patrat[0])-1
    y=int(patrat[1])-1
    Coloane[x*D+y]+=1
    Coloane[(x+1)*D+y]+=1
    Linii[y*D+x]+=1
    Linii[(y+1)*D+x]+=1
    
cnt=0
for lin in Linii:
    if lin==1:
        cnt+=1
        
for col in Coloane:
    if col==1:
        cnt+=1

#afisare
print(str(d*cnt))