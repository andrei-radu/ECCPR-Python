#citire
lin=input().split()
PSprop=int(lin[0])
PFprop=int(lin[1])
n=int(input())
PS=[]
PF=[]
for i in range(n):
    lin=input().split()
    PS.append(int(lin[0]))
    PF.append(int(lin[1]))
    
#prelucrare
def bataie(PSprop,PFprop,PS,PF): #subprogram care returneaza rezultatul unei batalii
    while PSprop>=0 or PS>=0:  #True pentru victorie, Fals pentru pierdere
        PSprop-=PF
        if PSprop<0:
            return False
        PS-=PFprop
        if PS<0:
            return True
        
contor=0 #pentru fiecare batalie castigata marim un contor
for runda in range(n):
    if bataie(PSprop,PFprop,PS[runda],PF[runda]):
        contor+=1

#afisare
print(contor) #pe care il afisam la final