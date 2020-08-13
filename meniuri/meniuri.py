#citire
Mancare=input().split()

#prelucrare
def OrdineCorecta(el1,el2): #subprogram care ne spune daca ordinea a doua farfurii este corecta
    Ordine=['A','C','P','D']
    indexEl1=0
    indexEl2=0
    for i in range(len(Ordine)):
        if el1[0]==Ordine[i]:
            indexEl1=i
        if el2[0]==Ordine[i]:
            indexEl2=i
    if indexEl2>indexEl1:
        return True
    else:
        return False
    
def FelNecuoscut(lista): #subprogram care ne spune daca un meniu contine un fel necunoscut
    for element in lista:
        if element[1]=='0':
            return True
    return False

Meniuri=[]  #lista pentru stocarea meniurilor
i=0  
while i<(len(Mancare)-1):
    lin=[]
    if OrdineCorecta(Mancare[i], Mancare[i+1]): #daca gasim doua feluri in ordine
        lin.append(Mancare[i]) #il adaugam pe primul intr o lista temporara
        while OrdineCorecta(Mancare[i], Mancare[i+1]): #si continuam sa adaugam elemente pana nu mai sunt in ordine
            lin.append(Mancare[i+1])
            i+=1
            if (i+1)>=len(Mancare): #exceptie pentru cand depasim limita felurilor
                break
    if lin: #daca am gasit ceva, lista temporara in meniuri
        Meniuri.append(lin)
        lin=[]
    i+=1
    
NrMeniuriNecunoscute=0
NrFarfuriiFolosite=0
for meniu in Meniuri:
    if FelNecuoscut(meniu): #numaram cate meniuri contin cel putin un fel necunoscut
        NrMeniuriNecunoscute+=1
    NrFarfuriiFolosite+=len(meniu) #si cate farfurii am folosit in meniuri
    
#afisare
print(len(Meniuri)) #afisam nr de meniuri
print(NrMeniuriNecunoscute) #si nr de meniuri necunoscute
print(len(Mancare)-NrFarfuriiFolosite) #si nr de farfurii - nr de farfurii folosite (adica nr de farfurii nefolosite)