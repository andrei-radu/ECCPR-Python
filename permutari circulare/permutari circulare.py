#citire
n=int(input())

#prelucrare
b=bin(n)
Cifre=[]
for i in range(2,len(b)):#luam cifrele de 0 si 1 si le adaugam intr-un vector
    Cifre.append(b[i])
Cifre.sort(reverse=True) #sortam vectorul invers, adica 1 si apoi 0, astfel obtinem cel mai mare nr binar
b='0b'+''.join(Cifre) #il facem sub forma standard de binar

#afisare
print(int(b,2)) #afisam nr in baza 10 obtinut