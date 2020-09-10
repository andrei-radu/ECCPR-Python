#citire
A=[]
m=int(input())
s=int(input())
for i in range(m*m):
    A.append(input().split()) #citim ca vector, deoarece este mai simplu
       
#prelucrare
Blocuri=[] #creem un vector pentru blocurile finale
limita=int(m/s) #calculam limita de blocuri (pe lungime sau latime)
for linie in range(limita): #un indice pentru a ne spune linia blocului curent
    for coloana in range(limita): #si coloana blocului curent
        bloc=[] #creem un bloc gol
        for i in range(linie*s,(linie+1)*s): #mergem in matricea A la linia corespunzatoare blocului
            for j in range(coloana*s,(coloana+1)*s): #si la coloana corespunzatoare
                bloc.append(A[i*m+j]) #adaugam ce gasim acolo: A[i*m+j] este defapt A[i][j]
        Blocuri.append(bloc) #adaugam blocul astfel creat

M=[]  
for bloc in Blocuri: #pentru fiecare bloc definim cele 3 valori maxime
    max1=0
    max2=0
    max3=0
    for combinatie in bloc: #pe care le aflam
        if int(combinatie[0])>int(max1): max1=combinatie[0]
        if int(combinatie[1])>int(max2): max2=combinatie[1]
        if int(combinatie[2])>int(max3): max3=combinatie[2]
    M.append([str(max1),str(max2),str(max3)]) #si le adaugam in matricea M
    
#afisare
for el in M: 
    print(" ".join(el))