#citire
n=int(input())
Vector=[]
for i in range(n):
    Vector.append(float(input()))
prag=float(input())

#prelucrare
Filtru=[]
for element in Vector:
    if element>prag:
        Filtru.append('1') #daca depaseste pragul adaugam 1 (ca string pt usurinta)
    else:
        Filtru.append('0') #daca nu, adaugam 0

filtru=''.join(Filtru) #unim toata lista intr-un sir
filtru=filtru.split('0') #pe care il despartim de zerouri

#afisare
print(len(filtru)) #afisam lungimea listei despartita de zerouri, adica nr de secvente de 1