variable=input()
lista1=variable.split("-")
lista_producto=[]
lista_precio=[]
lista_stock=[]
sin_stock=[]
total=0
for i in range (len(lista1)):
    lista2= lista1[i].split(":")
    lista_producto.append(lista2[0])
    lista_precio.append(lista2[1])
    lista_stock.append(lista2[2])
lista_precio = [int(x) for x in lista_precio]
lista_stock = [int(x) for x in lista_stock]
for i in range(len(lista_precio)):
    total+= lista_precio[i] * lista_stock[i]
print("El precio total es:", total)
caro=max(lista_precio)
posicion= lista_precio.index(caro)
print("El producto mas caro es:", lista_producto[posicion])
for k in range(len(lista_stock)):
    if lista_stock[k]==0:
        sin_stock.append(lista_stock[k])
print("Los productos con stock a cero es:", sin_stock)