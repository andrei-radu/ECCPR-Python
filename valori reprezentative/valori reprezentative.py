#citire
dim1=int(input())
Semnal1=[]
for i in range(dim1):
    Semnal1.append(int(input()))

dim2=int(input())
Semnal2=[]
for i in range(dim2):
    Semnal2.append(int(input()))
    
#prelucrare
Semnal=Semnal1+Semnal2 #concatenare semnale
ValoriReprezentative=[]
for val1 in Semnal:
    contor=0
    for val2 in Semnal:
        if val1>val2:
            contor+=1
        if contor>=5: #adaugam valoare ca fiind reprezentativa
            ValoriReprezentative.append(val1)
            break #nu are rost sa continuam testarea

#afisare
print(format((sum(ValoriReprezentative)/len(ValoriReprezentative)),'.2f'))