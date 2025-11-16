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
# El programa pide que password vas a utilizar
password=input("introduce una palabra clave: ")
# La variable comprobador se utiliza para al final saber si la contraseña ha seguido todos los pasos
comprobador=True
# Saber la longitud del password para ver si sigue las intrucciones.
if len(password) >=6 and len(password) <=8:
    # Comprobar que la primera letra del password es correcta
    if password[0].isnumeric() and int(password[0])>=1 and int(password[0])<=5:
        print("")
    else:
        # Si no se cumple la condición error en el caracter 1
        comprobador=False
        print("Error en el caracter 1")
    # Comprobar que la segunda letra del password es correcta
    if password[1].islower():
        print("")
    else:
        # Si no se cumple la condición error en el caracter 2
        comprobador=False
        print("Error en el caracter 2")
    # Comprobar que la tercera letra del password es correcta
    if password[2].isupper():
        print("")
    else:
        # Si no se cumple la condición error en el caracter 3
        comprobador=False
        print("Error en el caracter 3")
    # Comprobar que la quarta letra del password es correcta
    if password[3] in ["*", "_", "@"]:
        print("")
    else:
        # Si no se cumple la condición error en el caracter 4
        comprobador=False
        print("Error en el caracter 4")
    # Comprobar que la quinta letra del password es correcta
    if password[4].islower():
        print("")
    else:
        # Si no se cumple la condición error en el caracter 5
        comprobador=False
        print("Error en el caracter 5")
    # si la longitud de la contraseña es 6 y que no ha habido ningun error de caracter, comprobar que la sexta letra del password es correcta y poner que la contraseña es valida
    if len(password)==6 and password[5].isnumeric() and int(password[5])>=6 and int(password[5])<=9 and comprobador==True:
        print("El formato de PASSWORD és correcto")
    # si no se cumple la primera condicion comprobar que la sexta letra del password es correcta
    elif password[5].isnumeric() and int(password[5])>=6 and int(password[5])<=9:
        print("")
        # Si no se cumple las condiciones error en el caracter 6
    else:
        comprobador=False
        print("Error en el caracter 6")
    # si la longitud de la contraseña es 7 y que no ha habido ningun error de caracter, comprobar que la séptima letra del password es correcta y poner que la contraseña es valida
    if len(password)==7 and password[6] in ["&", "/", "#"] and comprobador==True:   
        print("El formato del PASSWORD és correcto")
    # Si la primera condición no se cumple, comprobar si la contraseña es menor que 7 para que no salga error en el caracter 7.      
    elif len(password)<7:
        print("")
    # si no se cumple las otras dos condiciones comprobar que la séptima letra del password es correcta
    elif len (password)>=7 and password[6] in ["&", "/", "#"]:
        print("")
    # Si no se cumple las condiciones error en el caracter 7
    else:
        comprobador=False
        print("Error en el caracter 7")
    # si la longitud de la contraseña es 8 y que no ha habido ningun error de caracter, comprobar que la octava letra del password es correcta y poner que la contraseña es valida 
    if len(password)==8 and password[7].isnumeric() and int(password[7])<=5 and comprobador==True:
        print("El formato del PASSWORD és correcto")
    # Si la primera condición no se cumple, comprobar si la contraseña es menor que 8 para que no salga error en el caracter 8
    elif len(password)<8:
        print("")
    # Comprobar que la octava letra del password es correcta.
    elif len (password)==8 and password[7].isnumeric() and int(password[7])<=5:
        ("")
    # Si no se cumple las condiciones error en el caracter 8.
    else:
        comprobador=False
        print("Error en el caracter 8")       
else:
    # Si no tiene un longitud entre 6 y 8 caracteres el programa indicará error.
    print("Error, el password tiene una longitud de", len(password), "caracteres i no cumple los requisitos")