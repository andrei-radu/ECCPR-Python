ora=input()
ora=ora.split(':')
h=100*int(ora[0])+int(ora[1])
n=int(input())
i=0
filme=[]
NrFilme=0
while i<n:
    film=input()
    film=film.split()
    ora.clear()
    ora=film[0]
    ora=ora.split(':')
    h1=100*int(ora[0])+int(ora[1])
    if h1<h:
        pass
    else:
        NrFilme+=1
        film[0]=h1
        filme.append(film)
    i+=1

i=0
ore=[]
while i<NrFilme:
    ore.append(filme[i][0])
    i+=1
OraMin=min(ore)
filmales='niciunu'
pret=999
i=0
while i<NrFilme:
    if int(filme[i][0])==int(OraMin) and int(filme[i][1])<int(pret):
        pret=filme[i][1]
        filmales=filme[i][2]
    i+=1
print(filmales)