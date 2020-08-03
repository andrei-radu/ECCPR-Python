#citire
n=int(input())
V=[]
for i in range(n):
    V.append(int(input()))
x=int(input())

#prelucrare si afisare
V.sort()
while len(V)>=1:
    mijloc=int(len(V)/2) #aflam mijlocul
    print(V[mijloc]) #afisam elementul din mijloc
    if V[mijloc]==x or mijloc==0:
        break #daca gasim pe x sau daca ramane un singur nr in vector, ne oprim
    elif V[mijloc]>x: #cautam in subvectorul din stanga
        if mijloc%2==0:
            V=V[:mijloc+1] #primele elemente +centrul pt nr par de elemente
        else:
            V=V[:mijloc] #sau doar primele elemente pt nr impar de elemente
    else: #cautam in subvectorul din dreapta
        if mijloc%2==0:
            V=V[-mijloc-1:] #ultimele elemente +centrul daca e par
        else:
            V=V[-mijloc:] #ultimele elemente daca e impar