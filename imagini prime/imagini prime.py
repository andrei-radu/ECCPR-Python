#citire
lin=int(input())
col=int(input())
i=1
linie=[]
Img=[]
while i<=lin*col:
    element=int(input())
    linie.append(element)
    if i%lin==0:
        Img.append(linie)
        linie=[]
    i+=1

#prelucrare   
def NrPrim(nr): #subprogram pt a vedea daca un nr este prim
    i=2
    prim=True
    while i<=nr/2:
        if nr%i==0:
            prim=False
        i+=1
    return prim

lin2=[]
Img2=[]  
for linie in Img:
    for el in linie:
        if NrPrim(el): #completam imaginea binara
            lin2.append(0)
        else:
            lin2.append(1)
    Img2.append(lin2)
    lin2=[]

obiect=0
for linie in Img2:
    for el in linie:
        if el==1: #numaram de cate ori apare 1
            obiect+=1 
            
#afisare
print(obiect)