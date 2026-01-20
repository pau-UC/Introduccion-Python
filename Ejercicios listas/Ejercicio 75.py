# Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados:
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
valores=len(lista1)
numeros=0
letras=0
mayus=0
suma=0
for i in lista1:
    if i.isnumeric():
        numeros+=1
        suma+=int(i)
    if i.isalpha():
        letras+=1
        if i.isupper():
            mayus+=1
print("Numero de valores:", valores)
print("Cantidad de numeros:", numeros)
print("Cantidad de letras:", letras)
print("Cantidad de mayusculas:", mayus)
print("Suma total de numeros:", suma)