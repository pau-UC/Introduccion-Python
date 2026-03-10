contraseña=input("Introduce las contraseñas: ")
lista=contraseña.split("-")

for i in lista:
    numletras=0
    numnumeros=0
    numcaracteres=0
    for j in i:
        if i.isnumeric():
            numnumeros+=1
        if i.isalpha():
            numletras+=1
        else:
            numcaracteres+=1
    if numcaracteres==0 and len(i)>=8 and numnumeros>1 and numletras>1:
        print("la contraseña", i, "es segura")
    if numcaracteres==0 and len(i)<8 and(numnumeros>=1 or numletras>=1):
        print("la contraseña", i, "es debil")
    if numcaracteres>=1:
        print("la contraseña", i, "es invalida")