def FormOra(ora): #subprogram care transforma ora in int
    ora=ora.split(':')
    return 100*int(ora[0])+int(ora[1])

#citire
OraSosire=input()
OraSosire=FormOra(OraSosire)
n=int(input())
Autobuze=[]
for i in range(n):
    linie=input().split()
    if FormOra(linie[0])>OraSosire:
        linie[0]=FormOra(linie[0])
        Autobuze.append(linie) #ne intereseaza doar autobuzele care pleaca dupa ce am ajuns noi
        
#prelucrare
Autobuze.sort() #sorteaza dupa ore, daca orele sunt egale dupa pret

#afisare
print(Autobuze[0][2]) #afisam numele primului autobuz care pleaca