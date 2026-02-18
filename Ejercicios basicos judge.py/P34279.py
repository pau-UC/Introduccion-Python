tiempo=input()
lista=[]
lista=tiempo.split()
lista[2]=int(lista[2])+1
for i in range(len(lista)):
    lista[i] = int(lista[i])
if lista[2]>=60:
    lista[2]=0
    lista[1]+=1
if lista[1]>=60:
    lista[1]=0
    lista[0]+=1
if lista[0]>=24:
    lista[0]=0
print(f"{lista[0]:02d}:{lista[1]:02d}:{lista[2]:02d}")