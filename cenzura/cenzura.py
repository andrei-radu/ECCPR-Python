#citire
text=input()
n=int(input())
cuvinte=[] #vector pentru cuvintele ce trebuie cenzurate
lin=input()
lin=lin.split()
for element in lin:
    cuvinte.append(element)

#prelucrare    
i=0
for cuvant in cuvinte:
    cenzura=''
    for litera in cuvant:
        cenzura+='*' #pentru fiecare litera din cuvantul cenzurat se adauga o steluta
    text=text.replace(cuvant,cenzura) #se inlocuiesc cuvintele cu cenzura

#afisare
print(text)