#citire
linie=input().split()
P=int(linie[0])
S=int(linie[1])
Informatii=[]
for i in range(P):
    Informatii.append(input().split())
    
#prelucrare
def EvolutieContinua(lista): #subprogram pt a verifica evolutia continuu ascendenta
    for i in range(1,len(lista)-1): #1 si len-1 pentru ca 0 este numele si ultima ar iesii din vector
        if int(lista[i])>int(lista[i+1]):
            return False
    return True

def ProcenteCastigate(lista): #subprogram pt determinarea procentului castigat
    return int(lista[len(lista)-1])-int(lista[1]) #intoarce ultimul procent - primul procent

PartideCrescatoare=[] #inregistram partidele crescatoare
ElectoratCastigat=['habemus papa'] #memoram pardicul cu cresterea cea mai mare
procent=-101  #pentru memorarea procentului
for partid in Informatii:
    
    if EvolutieContinua(partid):#retinem numele partidelor strict crescatoare in sondaje
        PartideCrescatoare.append(partid[0]) 
    
    if procent<ProcenteCastigate(partid): #verificam daca procentul de crestere este mai mare
        procent=ProcenteCastigate(partid) #daca da, il memoram
        ElectoratCastigat.pop() #scoatem partidul cu procentul anterior
        ElectoratCastigat.append([partid[0],str(procent)+'%']) #si il adaugam pe cel nou

#afisare
if PartideCrescatoare: #daca avem macar un partid crescator
    print(' '.join(PartideCrescatoare)) #il afisam
else:
    print('Nu exista') #daca nu, printam `nu exista`
print(' '.join(ElectoratCastigat[0])) #afisam partidul cu cea mai mare crestere