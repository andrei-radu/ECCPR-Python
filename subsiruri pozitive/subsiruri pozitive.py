#citire
n=int(input())
Valori=input()
Valori=Valori.split()

#prelucrare
SubsiruriPoz=[]
SubsiruriNeg=[]
IndexPoz=[]
lungimi=[]
i=0
while i<n: #creez subsirurile de elemente de acelasi semn
    temp=[]
    if i!=n: #pt evitarea iesirii din index la while
        while float(Valori[i])>0:
            temp.append(float(Valori[i]))
            i+=1
            if i==n: break #same
    if sum(temp,0)>0: #daca a adaugat elemente poz
        SubsiruriPoz.append(temp)
        IndexPoz.append(i-len(temp))
        lungimi.append(len(temp))
        temp=[]
    if i!=n: #pt evitarea iesirii din index la while
        while float(Valori[i])<0:
            temp.append(float(Valori[i]))
            i+=1
            if i==n: break #same
    if sum(temp,0)<0: #daca a adaugat elemente neg
        SubsiruriNeg.append(temp)
        temp=[]

#afisare
suma=0
for subs in SubsiruriPoz:
    suma+=sum(subs)
if suma==0: # in cazul in care nu este niciun sir pozitiv afisam -1 si 0
    print(-1)
    print(0)        
else:
    lungimemax=max(lungimi)
    contor=0
    i=0
    iteratie=0
    sumamax=0
    for subsir in SubsiruriPoz: #vedem daca exista mai multe subsiruri cu aceasi lungime
        if len(subsir)==lungimemax:
            contor+=1
            iteratie=i #si retinem la ce index se alfa (cazul in care e doar unul)
            if sum(subsir)>sumamax: #conditie cu strict mai mare pentru a il retine pe primul
                iteratieSum=i #retinem indexul in cazul in care sunt mai multe si trebuie facuta suma
                sumamax=sum(subsir)
        i+=1
    if contor==1: #daca e doar unul il afisam
        print(IndexPoz[iteratie])
        print(lungimemax)
    else: #daca sunt mai multe care indeplinesc conditia, il afisam pe primul
        print(IndexPoz[iteratieSum])
        print(lungimemax)      