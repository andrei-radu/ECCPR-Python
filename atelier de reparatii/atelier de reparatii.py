#citire
lin=input().split()
Componente=[int(x) for x in lin] #transformam in int ce am citit
N=int(input())
Laptopuri=[]
for i in range(N):
    lin=input().split()
    laptop=[int(x) for x in lin]
    Laptopuri.append(laptop)
    
#prelucrare 
LaptopuriReparate=0 #contor pentru a numara cate laptopuri reparam
for laptop in Laptopuri:
    ok=True #presupunem ca putem repara
    for i in range(len(laptop)):
        if laptop[i]==0 and Componente[i]==0: #daca are o componenta stricata si nu avem pe stoc
            ok=False #nu mai putem repara
    if ok: #daca putem repara
        for i in range(len(laptop)):
            if laptop[i]==0: #pentru fiecare componenta stricata scoatem din stoc o piesa
                Componente[i]-=1
        LaptopuriReparate+=1 #si consideram un laptop reparat
    else:
        for i in range(len(laptop)):#altfel, dezmembram laptopul pt a putea folosi piesele lui bune
            if laptop[i]==1:
                Componente[i]+=1
                
#afisare
print(LaptopuriReparate)