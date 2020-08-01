from math import factorial

#citire
lin=input().split()
n=int(lin[0])
M=int(lin[1])

#prelucrare
def C(n,k): #subprogram pentru calcul combinari
    return (factorial(n)/(factorial(k)*factorial(n-k)))

gasit=False
for k in range(n+1):
    if C(n,k)>=M: #daca indeplinim conditia afisam rezultatul
        print(k) #afisare
        gasit=True
        break

if gasit==False: #cand nu gasim, afisam 0
    print(0)