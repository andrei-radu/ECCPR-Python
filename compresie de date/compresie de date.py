#citire
n=int(input())
Linii=[]
for i in range(n):
    Linii.append(input().split(','))
    
#prelucrare
NewLin=[] #lista noua de liste
for linie in Linii: 
    new=[] #lista goala in care sa stocam informatia noua
    contor=0 #contor pt zerouri
    for i in range(len(linie)):
        if linie[i]=='0': #daca e 0, crestem contorul
            contor+=1
        elif contor!=0: #daca nu e zero si au fost zerouri inainte
            val=new.pop() #luam ultima valoare
            new.append('('+val+','+str(contor)+')') #si o adaugam cu nr de zerorui
            new.append(linie[i]) #adaugam si valoarea curenta
            contor=0 #resetam contorul
        else: #daca nu e zero si nici nu au fost zerouri inainte
            new.append(linie[i])   #adaugam valoarea
    if contor!=0: #verificam daca ultimul a fost un zero si nu am adaugat elementul cu nr lui de zerouri
        val=new.pop()
        new.append('('+val+','+str(contor)+')')
    NewLin.append(new) #adaugam in noua lista informatiile
    
#afisare
for linie in NewLin:
    print(','.join(linie))