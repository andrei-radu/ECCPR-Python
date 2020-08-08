def FormatareOra(ListaOra): #subprogram pentru a transforma ora din hh:mm in hhmm (int)
    return int(ListaOra[0])*100+int(ListaOra[1]) #deoarece este mai usor de comparat

#citire
OraSosire=input().split(':')
OraSosire=FormatareOra(OraSosire)
n=int(input())
Ghisee=[]
for i in range(n):
    linie=input().split()
    if FormatareOra(linie[0].split(':'))>= OraSosire:
        linie[0]=FormatareOra(linie[0].split(":"))
        Ghisee.append(linie) #adaugam doar ghiseele care sunt deschise dupa ce ajungem noi
    

#prelucrare
oramin=9999
dislike=99
GhiseuAles=''
for element in Ghisee:
    if int(element[0])<=int(oramin): #daca respecta conditia de ora
        if int(element[0])==int(oramin) and int(dislike)>int(element[1]): #verificam dislike-urile in cazul orei egale
            GhiseuAles=element[2]
            dislike=element[1]
        elif int(element[0])<int(oramin): #sau alegem direct ora mai mica
            GhiseuAles=element[2]
            dislike=element[1]
            oramin=element[0]

#afisare
print(GhiseuAles)