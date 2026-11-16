precio = int(input("Introduce el precio de la comida: "))
propina = int(input("Introduce el porcentaje de propina: "))
importe_propina = precio * propina / 100

total = precio + importe_propina

print(f"el total es = {total}")