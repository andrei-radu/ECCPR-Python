#citire
Numere=[]
numar=input()
while numar:#citim pana se apasa un Enter fara nimic altceva
    Numere.append(numar)
    numar=input()
    
#prelucrare
Judete=['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS', 'CL', 'CJ', 'CT', 'CV', 'DB', 'DJ', 'GL', 'GR', 'GJ', 'HR', 'HD', 'IL', 'IS', 'IF', 'MM', 'MH', 'MS', 'NT', 'OT', 'PH', 'SM', 'SJ', 'SB', 'SV', 'TR', 'TM', 'TL', 'VS', 'VL', 'VN']
def judet(initiale): #subprogram pentru determinarea indicativului din nr de inmatriculare
    if initiale in Judete:
        return True
    else:
        return False
    
cifre=['0','1','2','3','4','5','6','7','8','9']
def ecifra(n): #subprogram pentru a determina daca este o cifra
    if n in cifre:
        return True
    else:
        return False
  
def numere(nr): #subprogram pentru determinarea nr din nr de inmatriculare
    contor=0
    for cifra in str(nr):
        if ecifra(cifra):
            contor+=1
    if contor==2 or contor==3:
        return True
    else:
        return False

MAJ='Q W E R T Y U I O P A S D F G H J K L Z X C V B N M'.split()
def majuscule(maj): #subprogram pentru determinare literelor din numar de inmatriculare
    if len(maj)!=3: #daca nu are 3 majuscule nu mai conteaza
        return False
    for litera in maj:
        if litera not in MAJ:
            return False
    return True
    
#afisare
for Numar in Numere:
    numar=Numar.split()
    if judet(numar[0]) and numere(numar[1]) and majuscule(numar[2]):
        print(Numar)