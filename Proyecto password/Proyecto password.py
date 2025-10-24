# Mostrar las instrucciones del programa
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
print("     Un número menor o igual que 5")
password= input("introduce una palabra clave: ")

if len(password) >=6 and len(password) <=8:
    if password[0].isnumeric and int(password[0]) >=1 and int(password[0]) <=5:
        if password[1].islower:
            if password[2].isupper:
                if password[3]== "*" or "_" or "@":
                    if password[4].islower:
                        if password[5].isnumeric and int(password[5])>=6 and int(password[5])<=9:
                            if password[6]== "&" or "/" or "#":
                                if password[7].isnumeric and int(password[7])<=5:
                                    print("El format del PASSWORD és correcte")
                            else:
                                print("Error en el caràcter 7")
                        else:
                            print("Error en el caràcter 6")
                    else:
                        print("Error en el caràcter 5")
                else:
                    print("Error en el caràcter 4")
            else:
                print("Error en el caràcter 3")
        else:
            print("Error en el caràcter 2")
    else:
        print("Error en el caràcter 1")
else:
    longitud=len(password)
    print(f"Error, el password tiene una longitud de", longitud, "caracteres i no cumple los requisitos")
