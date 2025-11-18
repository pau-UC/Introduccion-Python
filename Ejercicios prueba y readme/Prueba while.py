edad=int(input("introduce la edad: "))

while edad>99 or edad<0:
    print("Edad incorrecta")
    edad=int(input("Vuelve a introducir la edad: "))
    if edad ==999:
        break
print("La edad es correcta, fin del programa")

