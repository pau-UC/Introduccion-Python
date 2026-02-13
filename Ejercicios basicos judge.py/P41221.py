numeros=input()
listanumeros=[]
listanumeros=(numeros).split()
if len(listanumeros)==0:
    while len(listanumeros)!=3:
        numero=input()
        if numero.isnumeric():
            listanumeros.append(numero)
if len(listanumeros)==1:
    while len(listanumeros)!=3:
        numero=input()
        if numero.isnumeric():
            listanumeros.append(numero)
if len(listanumeros)==2:
    while len(listanumeros)!=3:
        numero=input()
        if numero.isnumeric():
            listanumeros.append(numero)
for i in range(len(listanumeros)):
    listanumeros[i] = int(listanumeros[i])
suma=sum((listanumeros))
print(suma)