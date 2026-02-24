import random
print("")
lista_palabrasecreta=["patata","tomate","esternocleidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia",]
lista_partida=[]
lista_ahorcado=["A","H","O","R","C","A","D","O"]
longitud="_"
repetir="s"
error=0
errores=0
aleatorio=random.choice(lista_palabrasecreta)
for i in range(len(aleatorio)):
    lista_partida+=longitud.split(",")
while repetir=="s":
    while error!=8:
        print(lista_partida)
        letra=input("Introduce una letra: ")
        for i in range(len(aleatorio)):
            if letra==aleatorio[i]:
                lista_partida[i]=letra
            else:
                error+=1
                print(lista_ahorcado[error])
    repetir=input("deseas realizar otro ahorcado s/n: ")