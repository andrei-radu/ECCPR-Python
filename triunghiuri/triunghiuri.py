from math import sqrt
#citire
n=int(input())
Triunghiuri=[]
for i in range(n):
    Triunghiuri.append(input().split())
    
#prelucrare
def EsteTriunghiOarecare(laturi): #subprogram care determina daca este un triunghi oarecare
    a=float(laturi[0])
    b=float(laturi[1])
    c=float(laturi[2])
    
    if a>=b+c or b>=a+c or c>=a+b:
        return False #daca nu respecta conditia dimensiunilor
    elif a==b or b==c or a==c:
        return False #daca este isoscel sau echilateral
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        return False #daca este dreptunghic
    else:
        return True
    
def Raport(laturi): #subprogram care face raportul Arie/Perimetru
    a=float(laturi[0])
    b=float(laturi[1])
    c=float(laturi[2])
    
    P=a+b+c
    A=sqrt(P/2*(P/2-a)*(P/2-b)*(P/2-c))
    return float(format(A/P,'.3f'))

afisare=['0','0']
i=0
for triunghi in Triunghiuri:
    if EsteTriunghiOarecare(triunghi) and float(Raport(triunghi))>float(afisare[1]):
        afisare=[str(i),str(Raport(triunghi))] #salvam indexul si valoarea celui mai mare raport
    i+=1
    
#afisare
print(' '.join(afisare))