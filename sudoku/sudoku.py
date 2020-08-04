#citire
Sudoku=[]
for i in range(9):
    Sudoku.append(input().split())
    
#prelucrare
corect=True
Transpus=[ [Sudoku[j][i] for j in range(len(Sudoku))] for i in range(len(Sudoku[0]))]

def compara(lista):
    i=1
    lista.sort()
    for element in lista:
        if int(element)!=i:
            return False
        else:
            i+=1
    return True


for linie in Sudoku: #verificam liniile
    if compara(linie)==False:
        corect=False
        break

for linie in Transpus: #verificam coloanele
    if compara(linie)==False:
        corect=False
        break
#nu mai are sens sa verific altceva deoarece daca sunt indeplinite conditiile de linie si coloana, tabla este sigur corecta    
    
#afisare
if corect==True:
    print('Corect')
else:
    print('Gresit')