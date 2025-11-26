concatenar=""
inicio=int(input("introduce inicio: "))
fin=int(input("introduce fin: "))
incremento=int(input("introduce el incremento: "))

for x in range(inicio,fin,incremento):
    if not x%4==0:
        if x%6==0:
            concatenar=concatenar + "*" + str(x) + "*" ","
        else:
            concatenar=concatenar + str(x) + ","
print(concatenar[:-1])