import math
radio=int(input("introduce el radio: "))
altura=int(input("introduce altura: "))
letra=input("que deseas Mayúsculas(M) o minúscula(m): ")
formula=round(((math.pi* radio**2)*altura),3)
if letra not in ("Mm"):
    print("error")
elif letra=="M":
    print("EL VOLUMEN ES:", formula)
else:
    print("el volumen es:", formula)