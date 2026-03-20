
import random
import time
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
    print("Has selecionado la categoria de deportes")
    lista_palabrasecreta=["deportista","ronaldo","waterpolo","competicion","estrategia","maraton","estilos","natacion","bobsleigh","pertiga"]
elif categoria==2:
    print("Has selcionado la categoria de geografia")
    lista_palabrasecreta=["zimbabue","afluente","turkmenistan","bangladesh","prusia","hispania","kiribati","singapur","golfo","florida",]
elif categoria==3:
    print("Has selecionado la categoria de historia")
    lista_palabrasecreta=["normandia","napoleon","imperialismo","revolucion","versalles","bismarck","america","lepanto","templarios","dunkerque",]
elif categoria==4:
    print("Has selecionado la categoria de ciencias")
    lista_palabrasecreta=["relatividad","einstein","gravedad","esternocleidomastoideo","ventriculo","eclipse","electrones","alcalinoterreos","alpha","trigonometria",]
elif categoria==5:
    print("Has selecionado la categoria de entretenimiento")
    lista_palabrasecreta=["oscar","interestelar","titanic","yoda","chewbacca","sauron","vader","youtube","marvel","gandalf",]
elif categoria==6:
    print("Has selecionado la categoria de arte y literatura")
    lista_palabrasecreta=["hamlet","quijote","picasso","shakespeare","frankenstein","cervantes","gioconda","guernica","maquiavelo","iliada"]
else:
    print("tienes que introducir un numero entre 1 y 6")
if categoria>=1 and categoria<=6:
    lista_partida=[]
    lista_ahorcado=[]
    longitud="_"
    repetir="s"
    error=0
    errores=0
    aciertos=0
    while repetir=="s":
        lista_partida=[]
        letras_introducidas=[]
        lista_ahorcado=[]
        lista_introducir=[]
        lista_aciertos=[]
        lista_errorres=[]
        error=0
        aleatorio=random.choice(lista_palabrasecreta)
        inicio=time.time()
        for i in range(len(aleatorio)):
            lista_partida+=longitud.split(",")
        while error!=8 and lista_partida!=list(aleatorio):
            print(lista_partida)
            letra=input("Introduce una letra: ")
            if letra in aleatorio:
                for i in range(len(aleatorio)):
                    if letra==aleatorio[i]:
                        lista_partida[i]=letra
                        if not letra in lista_aciertos:
                            lista_aciertos.append(letra)
            else:
                if not letra in lista_errorres:
                    lista_errorres.append(letra)
                error+=1
                if error==1:
                    lista_ahorcado.append("A")
                if error==2:
                    lista_ahorcado.append("H")
                if error==3:
                    lista_ahorcado.append("O")
                if error==4:
                    lista_ahorcado.append("R")
                if error==5:
                    lista_ahorcado.append("C")
                if error==6:
                    lista_ahorcado.append("A")
                if error==7:
                    lista_ahorcado.append("D")
                if error==8:
                    lista_ahorcado.append("O")
                print(lista_ahorcado)
        final=time.time()
        tiempo=final-inicio
        minutos= tiempo//60
        segundos= tiempo%60
        print(f"El tiempo que ha durado esta partida ha sido de {minutos} minutos y {segundos} segundos")
        if error==8:
            errores+=1
            print("Has perdido, se han agotado tus intentos, la palabra era", aleatorio)
        if lista_partida==list(aleatorio):
            print("Muy bien has acertado la palabra")
            aciertos+=1
        print(f"Has acertado {len(lista_aciertos)} letras de la palabras")
        print("Te has equivocado en", error, "letras de la palabra")
        with open("text.txt", "a") as text_file:
            text_file.write("Fecha de la partida; " + time.strftime("%y-%m-%d") + "\n")
            text_file.write("Hora de la partida; " + time.strftime("%H-%M-%S") + "\n")
            text_file.write(f"Palabra secreta ahorcado; {aleatorio}\n")
            text_file.write(f"Aciertos; {len(lista_aciertos)}\n")
            text_file.write(f"Errorres; {error}\n")
            text_file.write("                                                  \n")
        introducir=input("introduce alguna palabra nueva separada por espacios: ")
        lista_introducir=introducir.split()
        lista_palabrasecreta.remove(aleatorio)
        for palabra in lista_introducir:
            lista_palabrasecreta.append(palabra)
        repetir=input("deseas realizar otro ahorcado s/n: ")
        while repetir!="s" and repetir!="n":
            print("por favor introduce s o n")
            repetir=input("deseas realizar otro ahorcado s/n: ")
        error=0
    print("Muy bien has acertado", aciertos, "palabras y has fallado", errores, "palabras.")
    print("Adios hasta la proxima")