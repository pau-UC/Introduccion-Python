import random
print("Instrucciones:")
print("simepre ha de poner la letra en minuscula y sin accentos")
print("Al acabar el programa se eliminara la palabra elegida aleatoriamente y podras añadir una palabra nueva")
print("Hay diferentes temas para jugar")
print("1. Introduce un 1 si usted desea que la categoria sea deportes")
print("2. Introduce un 2 si usted desea que la categoria sea geografia")
print("3. Introduce un 3 si usted desea que la categoria sea historia")
print("4. Introduce un 4 si usted desea que la categoria sea ciencias")
print("5. Introduce un 5 si usted desea que la categoria sea entretenimiento")
print("6. Introduce un 6 si usted desea que la categoria sea arte y literatura")
categoria=int(input("Introduce la categoria que quires realizar: "))
if categoria==1:
    lista_palabrasecreta=["deportista","ronaldo","waterpolo","competicion","estrategia","maraton","mariposa","natacion",""]
elif categoria==2:
    lista_palabrasecreta=["zimbaue","afluente","turkmenistan","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia",]
elif categoria==3:
    lista_palabrasecreta=["normadia","","esternocleidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia",]
elif categoria==4:
    lista_palabrasecreta=["patata","tomate","esternocleidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia",]
elif categoria==5:
    lista_palabrasecreta=["patata","tomate","esternocleidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia",]
elif categoria==6:
    lista_palabrasecreta=["patata","tomate","esternocleidomastoideo","marmota","aeropuerto","libreria","submarino","sublime","alpha","controversia",]
else:
    print("tienes que introducir un numero entre 1 y 6")
if categoria>=1 and categoria<=6:
    lista_partida=[]
    lista_ahorcado=["A","H","O","R","C","A","D","O"]
    longitud="_"
    repetir="s"
    error=0
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
        repetir=input("deseas realizar otro ahorcado s/n: ")