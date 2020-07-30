#citire
n=int(input())
i=0
k=[]
loturi=[]
while i<n:
    k.append(input())
    linie=input()
    linie=linie.split()
    loturi.append(linie)
    i+=1
  
#prelucrare  
LoturiUtile=0
for lot in loturi:
    NrC=0
    NrR=0
    NrT=0
    for comp in lot: #inregistram fiecare componenta
        if comp=='C':
            NrC+=1
        if comp=='T':
            NrT+=1
        if comp=='R':
            NrR+=1
    if NrC>=NrT and NrR>=NrC and NrC!=0 and NrT!=0 and NrR!=0:
        LoturiUtile+=1 #vedem cate loturi sunt utile

#afisare    
print(str(LoturiUtile)+' '+str(max(k)))
    