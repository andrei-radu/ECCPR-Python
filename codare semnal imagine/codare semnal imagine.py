#citire
m=int(input())
n=int(input())
v1=[] #nu are rost sa citim matricea, citim direct ca fiind v1
for i in range(m*n):
    v1.append(int(input()))

#prelucrare
v1.sort()
Contoare=[] #ca sa vedem de cate ori numaram
DejaNumarat=[] #si pe cine numaram
for element in v1:
    contor=0
    if element in DejaNumarat:
        pass #daca am numarat deja aparitiile, nu o mai facem 
    else:
        for el2 in v1:
            if element==el2:
                contor+=1
        Contoare.append(contor)
        DejaNumarat.append(element)

v2=Contoare+DejaNumarat #nu conteaza ordinea, ne intereseaza doar dimensiunea

#afisare
print(len(v1)-len(v2)) #afisam diferenta celor doi vectori