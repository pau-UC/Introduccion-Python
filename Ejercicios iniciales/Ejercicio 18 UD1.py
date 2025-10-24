# Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
niños=float(input("introduce el número de niños que iran al cine: "))
adultos=float(input("introduce el número de adultos que iran a la fiesta: "))
niños_euros=12*0.5*niños
adultos_euros=12*0.9*adultos
total_a_pagar=adultos_euros+niños_euros
print("tendreis que pagar", total_a_pagar)