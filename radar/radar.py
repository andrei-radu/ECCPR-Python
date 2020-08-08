from math import pow,atan
#citire
n=int(input())
Obiecte=[]
for i in range(n):
    Obiecte.append(input().split())
    
#prelucrare
def Ec(masa,viteza): #returneaza energia cinetica
    return masa*pow(viteza,2)/2

def Loveste(distanta,unghi): #subprogram pentru a definii daca loveste
    unghimax=atan(6371/distanta)
    if unghi<=float(unghimax):
        return True
    else:
        return False
    
def Clasificare(masa,viteza): #subprogram pentru clasificare
    if masa>=2000 and viteza<=100:
        return 'asteroid'
    elif masa<=2000 and viteza>=150:
        return 'cometa'
    else:
        return 'neidentificat'

def Pericol(masa,viteza):
    if Ec(masa,viteza)>=20000000000: #dupa calcule, atat ramane
        return True
    else:
        return False
    
    
Lovit=[0,0] #obiecte care lovesc, obiecte care lovesc periculos
Clasif=[0,0,0] #asteroid, cometa, neidentificat
ClasLov=[0,0,0] # -||-
ClasPer=[0,0,0] # -||-
for obiect in Obiecte: #ordinea atributelor este:
    #distanta, masa, unghi, viteza
    distanta=float(obiect[0])
    masa=float(obiect[1])
    unghi=float(obiect[2]) #puteau sa fie date direct
    viteza=float(obiect[3]) #dar lene
    clasa=Clasificare(masa, viteza)
    pericol=Pericol(masa,viteza)
    loveste=Loveste(distanta, unghi)
    
    if clasa=='asteroid': #clasificare obiecte
        Clasif[0]+=1
    elif clasa=='cometa':
        Clasif[1]+=1
    else:
        Clasif[2]+=1
    
    if loveste and pericol: #pentru lovit periculos
        Lovit[1]+=1
        if clasa=='asteroid':
            ClasPer[0]+=1
        elif clasa=='cometa':
            ClasPer[1]+=1
        else:
            ClasPer[2]+=1
        
    if loveste: #pentru lovit
        Lovit[0]+=1
        if clasa=='asteroid':
            ClasLov[0]+=1
        elif clasa=='cometa':
            ClasLov[1]+=1
        else:
            ClasLov[2]+=1
            

#afisare
print(Lovit) #trebuiau tranformate in str 
print(Clasif) #si facute cu ' '.join
print(ClasLov) #dar lene
print(ClasPer)