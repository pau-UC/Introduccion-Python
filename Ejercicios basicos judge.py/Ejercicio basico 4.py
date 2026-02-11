numeros=input()
listanumeros=[]
listanumeros=(numeros).split()
if len(listanumeros)==1:
    numero=input()
    listanumeros.append(numero)
if len(listanumeros)==2:
    numero=input()
    listanumeros.append(numero)
for i in range(len(listanumeros)):
    listanumeros[i] = int(listanumeros[i])
suma=sum((listanumeros))
print(suma)