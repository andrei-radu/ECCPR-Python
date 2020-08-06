from math import sqrt,pow
#citire
n=int(input())
Valori=input().split()

#prelucrare
suma=0.0
for x in Valori:
    suma+=float(x)
R=suma/n #aflam media rezistentelor

suma=0.0
for Ri in Valori:
    suma+=pow(float(Ri)-R,2)
S=sqrt(suma/n)  #calculam dupa formula data

contor=0
for x in Valori: #vedem cate se incadreaza
    if float(x)>=R-S and float(x)<=R+S:
        contor+=1
procent=contor/n*100 #aflam procentul

print(format(procent,'.2f')) #formatarea pentru 2 zecimale