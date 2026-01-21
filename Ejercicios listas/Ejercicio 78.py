# A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
repetir="s"
while not repetir=="n":
    numero=int(input("que numero deseas eliminar: "))
    if numero in lista1:
        lista1.remove(numero)
    else:
        print("el valor introducido no esta en la lista")
    print(lista1)
    repetir=input("Deseas introducir otro valor s/n: ")
    
