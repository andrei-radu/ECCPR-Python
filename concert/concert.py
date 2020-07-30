#citire
lin1=input()
lin1=lin1.split()
n=int(lin1[0])
Pb=float(lin1[1])
Cm=float(lin1[2])

lin2=input()
lin2=lin2.split()
i=0
for x in lin2:
    lin2[i]=int(x)
    i+=1
zi_start=int(100*lin2[1]+lin2[0]) # formatam zilele ca fiind
zi_end=int(100*lin2[3]+lin2[2])   #LLZZ unde L=luna Z=zi

concerte=[]
i=0
while i<n:
    concerte.append(input())
    i+=1

#prelucrare
cost_min=1000.1
nume='Acasa pe canapea'
for x in concerte:
    x=x.split()
    zi=int(x[2]*100+x[1]) #luam ziua concertului
    if zi>=zi_start and zi<=zi_end :
        pass #daca nu se incadreaza trecem peste
    else: #daca se incadreaza calculam costul
        cost=float(2.0*float(x[4])*Pb*Cm/3.0+float(x[3]))
        if cost<cost_min: #aflam care este cel mai ieftin concert
            nume=x[0]
            cost_min=cost

#afisare
print(nume +' '+ str(format(cost_min,'.2f')))