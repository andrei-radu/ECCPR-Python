#citire
n=int(input())
Culori=input().split()
read=input().split()
Copii=[]
while read:
    Copii.append(read)
    read=input().split()
    
#prelucrare si afisare
    #adaugam culorile care lipsesc si pot sa fie obinute
if 'purple' not in Culori and 'red' in Culori and 'blue' in Culori:
    Culori.append('purple')
if 'orange' not in Culori and 'yellow' in Culori and 'red' in Culori:
    Culori.append('orange')
if 'green' not in Culori and 'yellow' in Culori and 'blue' in Culori:
    Culori.append('green')
if 'brown' not in Culori and 'red' in Culori and 'yellow' in Culori and 'blue' in Culori:
    Culori.append('brown')
    
for copil in Copii: #pentru fiecare copil
    ok=True #presupunem ca are toate culorile
    for i in range(2,len(copil)):
        if copil[i] not in Culori: #daca ii lipseste una
            ok=False #il marcam ca fiind fals
    if ok: #daca a avut toate culorile
        print(copil[0]) #ii afisam numele