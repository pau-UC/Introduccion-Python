# Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
frase=input("introduce la frase: ")
longitud= len(frase)

if longitud>11:
    print("La frase tiene más de 11 caracteres")
elif longitud<11:
    print("la frase tiene menos de 11 caracteres")
else:
    print("la frase tiene 11 caracteres")