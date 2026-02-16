frase=input()
lista=[]
lista=frase.split()
if lista[0]>lista[1]:
    print(lista[0], ">", lista[1])
elif lista[0]<lista[1]:
    print(lista[0], "<", lista[1])
else:
    print(lista[0], "=", lista[1])