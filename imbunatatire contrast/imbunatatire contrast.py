#citire
lin=int(input())
col=int(input())
ImgOrg=[]
for i in range(lin*col):
    ImgOrg.append(int(input()))
    
#prelucrare
ImgFil=[int(x*0.9+2) for x in ImgOrg] #creem imaginea filtrata conform cerintei
Dif=[ImgFil[i]-ImgOrg[i] for i in range(lin*col)] #aflam matricea diferenta
medie=sum(Dif)/len(Dif) #facem media elementelor matricei diferenta

#afisare
print(format(medie,'.2f'))