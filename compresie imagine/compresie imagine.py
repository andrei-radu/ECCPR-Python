from math import cos,sqrt
#citire
m=int(input())
n=int(input())
A=[]
for i in range(m):
    lin=[]
    for j in range(n):
        lin.append(int(input()))
    A.append(lin) #citim ca matrice, pentru ca asa ni se cere sa lucram

#prelucrare
def coef1(u): #subprogram care calculeaza coef1
    if u==0: return 1/sqrt(m)
    else: return sqrt(2/m)
def coef2(v): #subprogram care calculeaza coef2
    if v==0: return 1/sqrt(n)
    else: return sqrt(2/n)
    
Af=[] 
for u in range(m): #calculam Af cu formula data
    lin=[]
    for v in range(n):
        suma=0
        for i in range(m):
            for j in range(n):
                suma+=cos(3.14*u/(2*m)*(2*i+1))*cos(3.14*v/(2*n)*(2*j+1))*A[i][j]
        lin.append(coef1(u)*coef2(v)*suma)
    Af.append(lin)
    
for i in range(m): #stergem tot inafara de primul element
    for j in range(n):
        if (i!=0 or j!=0):
            Af[i][j]=0
            
Ar=[]
for i in range(m): #calculam Ar cu formula data
    lin=[]
    for j in range(n):
        suma=0
        for u in range(m):
            for v in range(n):
                suma+=coef1(u)*coef2(v)*cos(3.14*u/(2*m)*(2*i+1))*cos(3.14*v/(2*n)*(2*j+1))*Af[u][v]
        lin.append(suma)
    Ar.append(lin)
    
#afisare
for lin in Ar:
    for el in lin:
        print(int(el))