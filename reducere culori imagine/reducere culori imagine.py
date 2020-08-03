#citire
m=int(input())
n=int(input())
s=int(input())
A=[]
for i in range(m*n):
    A.append(input().split())

#prelucrare
Interval=[]
for i in range(s): # aflam limita superioara pt fiecare interval
    limita_superioara=(i+1)*256/s
    Interval.append(limita_superioara)

M=[]
for linie in A:
    lin=[]
    for element in linie:
        i=0 #vedem in ce interval se incadreaza fiecare valoare
        for limsup in Interval:
            if int(element)<=int(limsup):
                lin.append(str(i))
                break
            else:
                i+=1
    M.append(lin)

#afisare
separator=' '
for lin in M:
    print(separator.join(lin))