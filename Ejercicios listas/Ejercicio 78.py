# A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
repetir="s"
while not repetir=="n":
    numero=input("que numero deseas eliminar: ")
    if numero.isnumeric():
        if numero in lista1:
            lista1.remove(numero)
            print(lista1)
        else:
            print("el valor introducido no esta en la lista")
    else:
        print("Introduce un valor númerico")
    repetir=input("Deseas introducir otro valor s/n: ")
    
