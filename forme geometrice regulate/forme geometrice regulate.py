#citire
n=int(input())
Coordonate=[]
for i in range(n):
    Coordonate.append(input().split())

#prelucrare
def Lungimi(c1,c2): #subprogram care intoarce lungimea unei laturi
    return (abs((float(c1[0])-float(c2[0])))+abs((float(c1[1])-float(c2[1]))))

def EsteRegulat(Lungimi): #subprogram care ne spune daca o forma este regulata sau nu
    #daca o forma este regulata, lungimea tuturor laturilor este egala, adica media lor este egala cu latura
    Lmed=sum(Lungimi)/len(Lungimi)
    for latura in Lungimi:
        if latura!=Lmed:
            return 'nu'
    return 'da'

Laturi=[] #Vector cu lungimile laturilor
for i in range(len(Coordonate)-1):
    Laturi.append(Lungimi(Coordonate[i],Coordonate[i+1]))
Laturi.append(Lungimi(Coordonate[-1],Coordonate[0]))

#afisare
print(EsteRegulat(Laturi))