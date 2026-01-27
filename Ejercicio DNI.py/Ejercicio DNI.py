
dni=input("Introduce los números del DNI: ")
resto=0
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
if len(dni)==8:
    resto=int(dni)%23
    for i in range(len(letras)):
        if letras[i]==letras[resto]:
            dni+= "-" + letras[i]
print(dni)
print(resto)
