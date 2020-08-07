#citire
n=int(input())
Comenzi=[]
for i in range(n):
    Comenzi.append(input().split())

#prelucrare
i=1 #contor pt instructiune
Registre=[0 for x in range(16)] #creem cele 16 registre: 0-16
for comanda in Comenzi:
    
    if comanda[0]=='lconst': #comanda pt lconst
        Registre[int(comanda[1])]=int(comanda[2])
    
    if comanda[0]=='add': #comanda pt add
        Registre[int(comanda[1])]=Registre[int(comanda[2])]+Registre[int(comanda[3])]
        
    if comanda[0]=='mul': #comanda pt mul
        Registre[int(comanda[1])]=Registre[int(comanda[2])]*Registre[int(comanda[3])]
        
    if comanda[0]=='div': #comanda pt div
        if Registre[int(comanda[3])]==0: #cazul cu /0
            print('Exception: line '+str(i))
            break
        else: #cazul cand e corect
            Registre[int(comanda[1])]=int(Registre[int(comanda[2])]/Registre[int(comanda[3])])
    
    if comanda[0]=='print': #comanda pt print
        print(Registre[int(comanda[1])])
    
    i+=1    #crestem nr instructiunii