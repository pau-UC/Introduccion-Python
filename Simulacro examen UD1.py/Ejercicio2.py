frase=input("introduce la frase: ")
numero1=float(input("introduce un número: "))
numero2=float(input("introduce otro número: "))
numero3=float(input("introduce otro número: "))

# Apartado1

frase=frase.lower()

#apatado2
totalsuma=numero1+numero2+numero3

totalmedia= round(totalsuma/3,2)

totalproducto=numero1*numero2*numero3
print("frase en minusculas:", frase)
print("la suma es:", totalsuma)
print("la media es:", totalmedia)
print("el producto es:", totalproducto)

if totalsuma>totalproducto:
    print("Falso")
else:
    print("Verdadero")