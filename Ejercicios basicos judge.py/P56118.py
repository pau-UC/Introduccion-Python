numero=input()
listanumeros=[]
listanumeros = numero.split()
for i in range(len(listanumeros)):
    listanumeros[i]=int(listanumeros[i])
maximo=max(listanumeros)
print(maximo)