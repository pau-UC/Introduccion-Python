# A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
lista=[]
repetir=""
while not repetir=="n":
    letra=input("introduce una letra: ")
    if letra.isalpha():
        if letra=="á":
            letra="a"
        if letra=="é":
            letra="e"
        if letra=="í":
            letra="i"
        if letra=="ó":
            letra="o"
        if letra=="ú":
            letra="u"
        lista.append(letra)
        repetir=input("Deseas repetir s/n: ")
listafinal=set(lista)
print(listafinal)