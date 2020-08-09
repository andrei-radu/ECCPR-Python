#citire
N=int(input())
Zaruri=[]
for i in range(N):
    Zaruri.append(input().split())
    
#prelucrare
suma=0
for zar in Zaruri: #pentru fiecare zar
    for j in range(1,7): #pentru toate fetele
        if str(j) not in zar: #daca o fata nu se vede
            suma+=j #o adaugam la suma
            
#afisare
print(suma)