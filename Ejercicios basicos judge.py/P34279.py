tiempo=input()
lista=[]
lista=tiempo.split()
listamas1=int(lista[2])+1
if int(listamas1[2])>=60:
    int(listamas1[2])=0
    int(listamas1[1])+1
if int(listamas1[1]>=60):
    int(listamas1[1])=0
    int(listamas1[0])+1
if int (listamas1[0])>=24:
    int(listamas1[0])=0