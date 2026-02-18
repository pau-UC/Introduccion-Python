import random
Lista_palabrasecreta=["patata","tomate","esternoclidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia"]
Lista_partida=[]
Lista_ahorcado=[]
longitud="_"
aleatorio=random.randint(Lista_palabrasecreta)
for i in range(len(aleatorio)):
    lista_partida+=longitud.split(",")
print(Lista_partida)