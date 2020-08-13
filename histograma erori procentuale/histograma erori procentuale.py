#citire
ValOpt=input()
Valori=input().split()

#prelucrare
Histograma=[ '['+str(x)+'% - '+str(x+5)+'%)' for x in range(0,100,5)]
Histograma.append('100%+') #creem histograma (doar fontul) conform cerintei

def Eroare(vopt,v): #subprogram care returneaza valoarea in procente a erorii
    return (float(v)-float(vopt))/float(vopt)*100

contor=[0 for i in range(21)] #contor, defapt adevarata histograma
for val in Valori: #pentru fiecare valoare, crestem histograma reala 
    er=Eroare(ValOpt,val)
    if er>=100: #exceptie, ar putea genera erori asa ca o luam separat
        contor[20]+=1 #exemplu 200/5 = 40, iese din indexul contorului (max 20)
    else:
        contor[int(er/5)]+=1
        
#afisare
for i in range(21): #afisam histograma conform cerintei
    print(Histograma[i]+' = '+str(contor[i]))