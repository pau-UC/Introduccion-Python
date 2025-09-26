#  Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=float(input("introduce un lado que no sea las bases: "))
base_menor=float(input("introduce la base menor: "))
base_mayor=float(input("introduce la base mayor: "))
altura=float(input("introduce la altura: "))
perimetro=lado*2+base_menor+base_mayor
area=(base_mayor+base_menor)*altura/2
print("El perímetro es", perimetro)
print("el área es", area)