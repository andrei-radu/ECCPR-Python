#citire
text=input()
perechi=input()
perechi=perechi.split()

#prelucrare
for litera in text:
    for pereche in perechi:
        if litera==pereche[0]:
            text=text.replace(litera, pereche[2])
	#pereche[0] trebuie inlocuita, pecreche[1] este virgula
	#pereche[2] reprezinta litera cu care se inlocuieste

#afisare
print(text)