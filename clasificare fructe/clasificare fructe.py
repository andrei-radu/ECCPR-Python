from math import sqrt,pow #folosim sqrt pt radical si pow pt putere
#citire
lin1=input().split()
n=int(lin1[0])
k=int(lin1[1])
Mc=int(lin1[2])
Rc=int(lin1[3])
Gc=int(lin1[4])
Bc=int(lin1[5])

i=0
Tip=[]
M=[]
R=[]
G=[]
B=[]
while i<n:
    lin=input().split()
    Tip.append(int(lin[0]))
    M.append(int(lin[1]))
    R.append(int(lin[2]))
    G.append(int(lin[3]))
    B.append(int(lin[4]))
    i+=1

#prelucrare
distante=[]
for i in range(0,n):
    ec=sqrt(pow(Mc-M[i],2)+pow(Rc-R[i],2)+pow(Gc-G[i],2)+pow(Bc-B[i],2))
    distante.append(ec) #adaugam rezultatul calcului specificat de ei 
    
DistMin=min(distante) #cautam distanta minima

#afisare
for i in range(0,n):
    if distante[i]==DistMin: 
        print(Tip[i]) #afisam tipul fructului care are distanta minima