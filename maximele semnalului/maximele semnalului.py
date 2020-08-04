#citire
n=int(input())
V=[]
for i in range(n):
    V.append(float(input()))

#prelucrare
Maxime=[]
for i in range(n):
    if i==0 and V[0]>V[1]:#exceptie pt primul element
        Maxime.append(V[0])
        i+=1
    else:
        i+=1

    if i==n-1 and V[n-1]>V[n-2]:#exceptie pt ultimul element
        Maxime.append(V[n-1])
        break
        
    if V[i]>V[i-1] and V[i]>V[i+1]:#cazul general
        Maxime.append(V[i])
    i+=1

medie=sum(Maxime)/len(Maxime)
contor=0 #numaram elementele mai mari ca media
for element in Maxime:
    if element>medie:
        contor+=1

#afisare
print(contor)