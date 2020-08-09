#citire
n=int(input())
Loturi=[]
for i in range(n):
    k=int(input())
    Loturi.append(input().split())

#prelucrare
def NumarPiese(lot): #subprgram care returneaza numarul de piese dintr-un lot
    surub=0         # simplica utilizarea celuilalt subprogram
    piulita=0
    raft=0
    holtz=0
    balama=0
    
    for piesa in lot:
        if piesa=='S': surub+=1
        elif piesa=='P': piulita+=1
        elif piesa=='R': raft+=1
        elif piesa=='H': holtz+=1
        else: balama+=1
    
    return [surub,piulita,raft,holtz,balama]

def eBun(lot): #subprogram care decide daca un lot este util sau nu

    for piesa in lot:
        if piesa==0:
            return False
    if lot[2]%4!=0:
        return False
    elif lot[0]!=lot[1]:
        return False
    elif lot[4]%2!=0:
        return False
    elif lot[3]%2!=0 or lot[3]>lot[1]:
        return False
    else:
        return True
    
LotBun=[]
for lot in Loturi:
    if eBun(NumarPiese(lot)): #daca un lot este bun, il notam
        LotBun.append(1)
    else: #daca nu, ii punem 0
        LotBun.append(0)
        
#afisare
raport=sum(LotBun)/len(LotBun) #facem raportul celor bune/total
afisare=[str(cifra) for cifra in LotBun] #il transformam in string
print(' '.join(afisare)) #il afisam
print(1-raport) #afisam raportul celor rele/total