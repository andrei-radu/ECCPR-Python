#citire
n=int(input())
SenzorStanga=[]
for i in range(n):
    SenzorStanga.append(input().split())
SenzorDreapta=[]
for i in range(n):
    SenzorDreapta.append(input().split()) #nu avem nevoie de el, dar datele trebuie citite
    
#prelucrare
contorMasini=0 #contor pt masini
timp=0 #sa aflam timpul in care se deplaseaza pe un metru
for i in range(len(SenzorStanga)-1):
    if SenzorStanga[i][1]=='1' and SenzorStanga[i+1][1]=='1': #daca trece o masina
        timp=int(SenzorStanga[i+1][0])-int(SenzorStanga[i][0]) #nu conteaza ce timp luam pentru ca in enunt spune ca sunt la viteze constante
        contorMasini+=1 #crestem contorul
        
viteza=(1/1000)/(timp/(1000*60*60)) #calculam viteza in km/h

#afisare
print(" ".join([str(int(viteza)),str(contorMasini)]))