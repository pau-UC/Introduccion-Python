# Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro.
print("Menú"), print("1. Bocadillo de calamares- 9 €"), print("2. Bocadillo de chistorra - 4.5 €"), print("3. Bikini de jamón - 2.5 €"), print(""), print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €"), print("2. Patatas gruesas - 1.75 €"), print("3. Patatas rústicas - 2 €")
pagar=0
pedidos=0
repetir="s"
total=0
while repetir=="s":
    pedidos+=1
    eleccion1=int(input("Que numéro del menú vas a pedir: "))
    if eleccion1==1:
        pagar=pagar+9
    if eleccion1==2:
        pagar=pagar+4.5
    if eleccion1==3:
        pagar=pagar+2.5
    eleccion2=int(input("Que numéro del acompañamiento vas a pedir: "))
    if eleccion2==1:
        pagar=pagar+1.5
    if eleccion2==2:
        pagar=pagar+1.75
    if eleccion2==3:
        pagar=pagar+2
    eleccion3=int(input("Que numéro del menú vas a pedir: "))
    if eleccion3==1:
        pagar=pagar+2
    if eleccion3==2:
        pagar=pagar+1.5
    if eleccion3==3:
        pagar=pagar+1
    repetir=input("deseas repetir la operacion s/n: ")
print("el numero de pedidos realizados es", pedidos)
print("total a pagar", pagar)
total_iva=pagar*1.1
print("Total con IVA", total_iva)
if total_iva>=20 and total_iva<=30:
    total=total_iva*0.95
if total_iva>30:
    total=total_iva*0.85
print("Total con descuento aplicado", round(total,2))