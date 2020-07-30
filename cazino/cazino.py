NrMaini=int(input())

i=0
CartiJucate=[]
while i<NrMaini:
    CartiJucate.append(input())
    i+=1
    
ok=1
for carte in CartiJucate:
    contor=0
    if ok==0: break
    for carte2 in CartiJucate:
        if carte==carte2: contor+=1
    if contor>=3: 
        print(carte)
        ok=0
if ok: print("JOC OK")