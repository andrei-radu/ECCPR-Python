#citire
lin=input()
lin=lin.split()
D=int(lin[0])
k=int(lin[1])

i=0
n=[] #vector pentru nr de carti
p=[] #vector pentru grosimea lor
while i<k:
    lin=input()
    lin=lin.split()
    n.append(int(lin[0])) 
    p.append(int(lin[1]))
    i+=1

#prelucrare    
m=[]
while sum(n)>0:
    i=0
    copieD=D
    raft=[]
    while i<k: #cat timp exista carti
        if n[i]!=0 and p[i]<=copieD: #daca exista carte si incape
            raft.append(p[i]) #o pune pe raft
            copieD-=p[i] #vedem cat loc ramane disponibil
            n[i]-=1 #scadem cartea pusa
        else:i+=1 #altfel, incearca o carte de dimensiune mai mica
    m.append(raft) #

#afisare    
for Raft in m:
    print(Raft)