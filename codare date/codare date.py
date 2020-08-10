#citire
n=int(input())
Numere=[]
for i in range(n):
    Numere.append(input().split())
    
#prelucrare
def Invers(nr): #subprogram care creaxa x'
    ultimacifra=''
    nrnou=''
    if len(nr)%2==1: #exceptie pentru cand are numar impar de cifre
        ultimacifra+=nr[len(nr)-1] #retinem ultima cifra
        nr=nr[:-1] #si o scoatem din numar ca sa fie pare 
    i=0
    while i<len(nr): #inversam intre ele cifrele, 2 cate 2
        nrnou+=nr[i+1]
        nrnou+=nr[i]
        i+=2
    nrnou+=ultimacifra #adaugam ultima cifra, fie nimic, fie ce era 
    return nrnou 
        
def Rest(nr): #subprogram care returneaza x''
    nrnou=nr[0]
    for i in range(1,len(nr)):
        nrnou+=str(int(nr[i])%2)
    return nrnou

def Suma(nr): #subprogram care calculeaza suma cifrelor
    s=0
    for cifra in nr:
        s+=int(cifra)
    return s

SumaCifre=[] #vector in care retinem sumele cifrelor
for numar in Numere:
    nr=''.join(numar) #creem numarul din cifrele date
    SumaCifre.append(Suma(Rest(Invers(nr)))) #aflam suma dupa ce calculam x' si x''

#afisare
print(max(SumaCifre)) #afisam suma maxima