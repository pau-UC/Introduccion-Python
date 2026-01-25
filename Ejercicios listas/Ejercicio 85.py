# Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
listaingles=[]
listacata=[]
listacaste=[]
repetir="s"
while not repetir=="n":
    estudiante=input("Introduce el nombre del estudiante: ")
    ingles=int(input("Introduce la nota de ingles: "))
    caste=int(input("Introduce la nota de castellano: "))
    cata=int(input("Introduce la nota de catalán: "))
    listacaste.append(caste)
    listaingles.append(ingles)
    listacata.append(cata)
    repetir=input("Deseas introducir otro alumno s/n: ")
listaingles.sort()
listacaste.sort()
listacata.sort()
print(listaingles)
print(listacaste)
print(listacata)
mediaingles=sum(listaingles)/len(listaingles)
mediacaste=sum(listacaste)/len(listacaste)
mediacata=sum(listacata)/len(listacata)
print("La media de ingles és:", mediaingles)
print("La media de castellano es:", mediacaste)
print("La media de catalán es:", mediacata)