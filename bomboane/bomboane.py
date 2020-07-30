#citire
n=input()
n=int(n)

list_bani=input()
list_bani=str.split(list_bani)
bani=[]
for i in list_bani:
    bani.append(i)

i=0
cost_bomboana=[]
aroma_bomboana=[]
while i<n:
    lista=input()
    lista=str.split(lista)
    cost_bomboana.append(lista[0])
    aroma_bomboana.append(lista[1])
    i=i+1

#prelucrare
arome_cumparate=[]
zi=0
fericire=0
portofel=0

while zi<n:
    portofel+=int(bani[zi]) #primeste bani
    if int(cost_bomboana[zi])<=portofel: #daca isi permite bomboana
        portofel-=int(cost_bomboana[zi]) #o cumpara si
        fericire+=int(aroma_bomboana[zi]) #ii creste fericirea
        arome_cumparate.append(aroma_bomboana[zi])
    else: #daca nu si o permite
        j=0
        for x in arome_cumparate: #verifica daca a cumparat una mai mare zilele trecute
            if int(aroma_bomboana[zi])>int(x): j+=1
        if j==(zi): fericire-=int(aroma_bomboana[zi]) #daca da, ii scade fericirea
    zi=zi+1

#afisare
print(fericire)