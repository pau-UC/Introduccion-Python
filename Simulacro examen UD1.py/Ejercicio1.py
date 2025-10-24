nombre=input("introduce nombre: ")
edad=int(input("introduce tu edad: "))
if edad>0 and edad <100:
    año_actual=2025
    futuro=año_actual + (100-edad)
    print("Hola",nombre.upper(), "cumpliras 100 años en el año", futuro)
else:
    print("edad no valida")