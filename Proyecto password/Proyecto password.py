# Mostrar las instrucciones del programa.
print("INSTRUCCIONES")
print("1.La longitud del password tiene que tener entre 6 i 8 caracteres")
print("2.Forzar los siguientes valores según la posición indicada")
print("     Posición 1 un número major o igual que 1 i menor o igual que 5")
print("     Posición 2 una letra minúscula")
print("     Posición 3 una letra majúscula")
print("     Posición 4 uno de los siguientes símbolos *, _, @ ")
print("     Posición 5 una letra minúscula")
print("     Posición 6 un número major o igual que 6 i menor o igual que 9")
print("     Posición 7 uno de los siguientes símbolos &, /, # ")
print("     Posición 8 un número menor o igual que 5")
password=input("introduce una palabra clave: ")
comprobador=True
corrector=0
if len(password) >=6 and len(password) <=8:
    if password[0].isnumeric() and int(password[0])>=1 and int(password[0])<=5:
        print("")
    else:
        comprobador=False
        print("Error en el caracter 1")
    if password[1].islower():
        print("")
    else:
        comprobador=False
        print("Error en el caracter 2")
    if password[2].isupper():
        print("")
    else:
        comprobador=False
        print("Error en el caracter 3")
    if password[3] in ["*" or "_" or "@"]:
        print("")
    else:
        comprobador=False
        print("Error en el caracter 4")
    if password[4].islower():
        print("")
    else:
        comprobador=False
        print("Error en el caracter 5")
    if password[5].isnumeric and int(password[5])>=6 and int(password[5])<=9:
        if len(password)==6 and comprobador==True:
            print("El format del PASSWORD és correcte")
            corrector=1
        else:
            print("")
    else:
        comprobador=False
        print("Error en el caracter 6")
    if len(password)==7 and password[6] in ["&" or "/" or "#"]:
        if len(password)==7 and comprobador==True:
            print("El format del PASSWORD és correcte")
            corrector==1
        else:
            print("")
    elif corrector==1:
        print("")
    else:
        comprobador=False
        print("Error en el caracter 7")
    if len(password)==8 and password[7].isnumeric() and int(password[7])<=5 and comprobador==True:
        print("El format del PASSWORD és correcte")
    elif corrector==1:
        print("")
    elif len(password)==8 and password[7].isnumeric() and int(password[7])<=5:
        print("")
    else:
        comprobador=False
        print("Error en el caracter 8")       
else:
    print("Error, el password tiene una longitud de", len(password), "caracteres i no cumple los requisitos")