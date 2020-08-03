#citire
lin=input().split()
m=int(lin[0])
n=int(lin[1])
p=int(lin[2])

v=[]
for i in range(m):
    lin=input().split()
    v.append(lin)

w=[]
for i in range(n):
    lin=input().split()
    w.append(lin)

X=input().split()

#prelucrare
S=[]
for j in range(n):
    suma=0
    for i in range(m):
        suma+=int(X[i])*int(v[i][j])
    S.append(suma) #calculam Sj dupa regula lor

Y=[]   
for k in range(p):
    suma=0
    for j in range(n):
        suma+=int(S[j])*int(w[j][k])
    Y.append(suma) #calculam Yk dupa regula lor

#afisare
for index in range(len(Y)):
    if Y[index]==max(Y):
        print(index+1) #afisam index+1 deoarece pt ei indexarea incepe cu 1, nu cu 0