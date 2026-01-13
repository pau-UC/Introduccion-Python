listanumeros=[]
listanonumeros=[]
listatodo=[]
frase=input("Introduce valores separados por un guion: ")
listatodo=frase.split("-")
for x in listatodo:
    if x.isnumeric():
        listanumeros.append(int(x))
    else:
        listanonumeros.append(x)
# for i in range(len(listatodo)):
# if listatodo[i].isnumeric():
# listanumeros.append(int(listatodo[i]))
# else:
# listanonumeros.append(listatodo[i])
print(listanumeros)
print(sum(listanumeros))