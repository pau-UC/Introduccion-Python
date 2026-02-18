import random
lista_palabrasecreta=["patata","tomate","esternoclidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia"]
lista_partida=[]
lista_ahorcado=["AHORCADO"]
longitud="_"
repetir="s"
aleatorio=random.choice(lista_palabrasecreta)
for i in range(len(aleatorio)):
    lista_partida+=longitud.split(",")
while repetir!="n":
    print(lista_partida)
    letra=input("Introduce una letra: ")
    for i in range(len(aleatorio)):
        if letra==aleatorio[i]:
            lista_partida[i]=letra
    repetir=input("deseas realizar otro ahorcado s/n: ")