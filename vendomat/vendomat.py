#citire
N=int(input())
Stoc=input().split()
n=int(input())
Cereri=[]
for i in range(n):
    Cereri.append(input().split())
    
#prelucrare
def Aprov(lista): #subprogram pentru a determina daca este o aprovizionare
    for element in lista:
        if element!='0': #se putea si cu sum(lista)==0, daca erau int
            return False
    return True

nerealizate=0 #contor pentru vanzari nerealizabile
aprovizionari=0 #contor pentru aprovizionari
for cerere in Cereri:
    ok=True #presupunem ca o vanzare este buna
    
    if Aprov(cerere): #verificam daca este aprovizionare
        aprovizionari+=1 #daca da, crestem contorul
        for i in range(N):
            Stoc[i]=int(Stoc[i])+10 #si adaugam cate 10 elemente
        continue # si trecem la urmatoarea cerere
    
    for i in range(N): #verificam daca avem stoc suficient
        if int(cerere[i])>int(Stoc[i]):
            ok=False
    if ok: #daca da, scadem obiectele vandute
        for i in range(N):
            Stoc[i]=int(Stoc[i])-int(cerere[i])
    else: #daca nu, crestem contorul pentru vanzari nerealizate
        nerealizate+=1
        
#afisare
print(nerealizate)
print(aprovizionari)