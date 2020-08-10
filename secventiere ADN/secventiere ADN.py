#citire
ADN=input()

#prelucrare si afisare
def EstePereche(N1,N2): #subprogram care determina daca o pereche este corecta
    if N1=='A' and N2!='T':
        return False
    elif N1=='T' and N2!='A':
        return False
    elif N1=='C' and N2!='G':
        return False
    elif N1=='G' and N2!='C':
        return False
    else: return True

ok=True
for i in range(int(len(ADN)/2)):
    if EstePereche(ADN[i], ADN[-1-i]): #comparam mereu nucleotidele cerute, prima cu ultima, a doua cu penultima, etc... 
        pass #daca e corect, trecem mai departe
    else: #daca a gasit o greseala, printeaza indexul din secventa
        print(i+1) #vectorul incepe de la 1, nu de la 0
        ok=False #semnalizam ca nu este o secventa buna
        break #ne oprim
    
if ok: #daca nu a gasit greseli, afiseaza 0
    print(0)