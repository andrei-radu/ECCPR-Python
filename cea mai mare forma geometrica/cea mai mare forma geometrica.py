#citire
N=int(input())
Forme=[]
for i in range(N):
    Forme.append(input().split())
    
#prelucrare
def Arie(forma): #subprogram care intoarce Aria unei forme
    if forma[0]=='dreptunghi':
        return float(forma[1])*float(forma[2])
    elif forma[0]=='cerc':
        return 3.14*float(forma[1])*float(forma[1])
    else: #deci e patrat
        return float(forma[1])*float(forma[1])
    
maxim=0
Afisare=[] #stocam informatiile despre forma cu arie maxima
for forma in Forme: #aflam aria maxima 
    if Arie(forma)>maxim:
        Afisare=forma #ii salvam informatiile
        maxim=Arie(forma)

#afisare
print(' '.join(Afisare))