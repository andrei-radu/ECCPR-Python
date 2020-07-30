#citire
n=int(input())
i=0
Zile=[]
while i<n:
    Zile.append(input())
    i+=1
    
#prelucrare
for element in Zile:
    contor=0
    for el2 in Zile:
        if el2==element:
            contor+=1 #numara dublurile
    while contor>1: #cat timp exista dubluri
        Zile.remove(element) #sterge dublura
        contor-=1

ZileNr=[] #contor pt a usura sortarea
for element in Zile: #transformama ziua in numar 1LLZZ
    ZileNr.append(10000+int(element[3]+element[4])*100+int(element[0]+element[1]))
    #10000 pt a evita disparitia lui 0 din lunile inainte de 10

ZileNr.sort()

#afisare
for element in ZileNr:
    element=str(element) #transformam in string pentru a putea afisa cum cere problema
    print(element[3]+element[4]+'-'+element[1]+element[2])