#citire
N=input()
Temp=input().split()

#prelucrare
def AltSemn(v1,v2): #subprogram care returneaza True daca v1 si v2 au semne diferite, si False daca nu
    if float(v1)>=0 and float(v2)<0:
        return True
    elif float(v2)>=0 and float(v1)<0:
        return True
    else:
        return False

AltStoc=[] #stocam fiecare secventa de numere cu semne alternante
lin=[]
for i in range(1,int(N)-1):
    while AltSemn(Temp[i],Temp[i-1]):
        lin.append(Temp[i-1])
        i+=1
    
    if lin:
        lin.append(Temp[i-1])
        AltStoc.append(lin)
        lin=[]
    i+=1

Zplus=0 #zilele cu temperaturi pozitive
for t in Temp: #numaram cate sunt
    if float(t)>=0:
        Zplus+=1
NrMaxElemente=[len(lista) for lista in AltStoc] #ca sa aflam cea mai lunga seceventa de semne alternative

#afisare
for i in range(len(AltStoc)-1,-1,-1): #parcurgem lista invers, deoarece in cazul unei egalitati ne cere cea mai recenta lista
    if len(AltStoc[i])==max(NrMaxElemente): #cand gasim maximul
        print(len(AltStoc[i])) #afisam nr de elemente
        print(' '.join(AltStoc[i])) #si elementele
        break #si ne oprim
    
procentP=format(Zplus/len(Temp)*100,'.2f') #aflam procentul de zile pozitive
procentN=format( 100 - (Zplus/len(Temp)*100),'.2f') #si de zile negative
print('+:'+str(procentP)+'% -:'+str(procentN)+'%') #si le afisam