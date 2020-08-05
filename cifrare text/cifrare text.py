#citire
text=input()
n=int(input())
Chei=[]
for i in range(n):
    Chei.append(int(input()))
    
#prelucrare
Litere=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z']
LitereMari=[] #liste cu literele din alfabet
for litera in Litere:
    LitereMari.append(litera.upper())

def afla_index(char): #subprogram aflare index
    i=0
    char=char.lower()
    for element in Litere:
        if element==char:
            return i
        else: i+=1

textNou='' #text nou deoarece exista riscul sa rescriem ceva deja schimbat daca folosim text.replace(::1)
i=1
for caracter in text:
    if i>n: i=1 #pentru a putea relua cheia secvential
    if caracter in Litere: #schimbam literele mici
            index_litera_noua=afla_index(caracter)+i
            if index_litera_noua>=26: #in cazul in care trecem de z
                textNou+=Litere[index_litera_noua-26]
            else:
                textNou+=Litere[index_litera_noua]
            i+=1
    elif caracter in LitereMari: #schimbam literele mari
            index_litera_noua=afla_index(caracter)+i
            if index_litera_noua>=26: #in cazul in care trecem de Z
                textNou+=LitereMari[index_litera_noua-26]
            else: 
                textNou+=LitereMari[index_litera_noua]
            i+=1
    else: textNou+=caracter #lasam caracterele care nu sunt litere
    
#afisare
print(textNou)