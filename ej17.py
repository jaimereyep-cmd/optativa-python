frutas = [
    ("Manzana", 3, 2.7),
    ("Naranjas", 4, 3.7),
    ("Kiwi", 2.5, 5),
    ("peras", 3, 2.5),
    ("uvas", 2, 3.8),
]

total_compra = 0
total_cantidades = 0

for producto, cantidad, precio in frutas:
    producto = producto.upper()

    total_producto = round(cantidad * precio, 2)

    print(f"{producto}: {cantidad} * {precio} = {total_producto}")

    total_compra += total_producto
    total_cantidades += cantidad

print(f"El total de la compra es: {total_compra}")
print(f"Total cantidades: {total_cantidades}")