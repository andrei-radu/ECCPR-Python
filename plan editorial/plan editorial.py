#citire
[P,n]=input().split()

#prelucrare
def Incape(p,n): #subpogram care ne spune daca pagina P contine problema nr n
    problema=1
    for i in range(1,int(P)+1):
        for j in range(1,i+1):
            problema+=1
            if problema==int(n):
                return True
    return False

def calculC(P): #subprogram care calculeaza nr de cifre necesare
    problema=1
    for i in range(1,int(P)+1):
        for j in range(1,i+1):
            problema+=1
    NrCifre=0
    for i in range(1,problema):
        while i>0:
            NrCifre+=1
            i=int(i/10)
    return NrCifre
    
#afisare
if Incape(P,n):
    print(calculC(P))
else:
    print(0)