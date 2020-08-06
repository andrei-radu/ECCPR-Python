#citire
N=int(input())
Autobuze=input().split()

#prelucrare
suma=0
for i in range(N): 
    if str(i) not in Autobuze:
        suma+=i #daca nu se alfa printre cele care au trecut, il adunam la suma

#afisare
print(suma)